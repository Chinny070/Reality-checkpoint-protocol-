// Submit a Studionet write with JSON argument arrays, preserving JSON-as-string
// ABI values. The current GenLayer CLI parser coerces JSON-shaped arguments to
// containers and cannot represent several contract `*_json: str` parameters.
// The signer is read only from the GenLayer CLI's OS credential store.

import { createRequire } from "node:module";
import { join } from "node:path";
import { pathToFileURL } from "node:url";
import { readFile } from "node:fs/promises";

const args = process.argv.slice(2);
function option(name, fallback = undefined) {
  const index = args.indexOf(name);
  if (index < 0) return fallback;
  if (index + 1 >= args.length) throw new Error(`missing value for ${name}`);
  return args[index + 1];
}

const method = option("--method");
const argsFile = option("--args-file");
const accountName = option("--account", "my-studionet-wallet");
const contractAddress = option("--address");
const endpoint = option("--rpc", "https://studio.genlayer.com/api");
const retries = Number(option("--wait-retries", "180"));
const interval = Number(option("--wait-interval", "5000"));
if (!method || !argsFile || !contractAddress) {
  throw new Error("usage: node scripts/live_write.mjs --address 0x... --method METHOD --args-file PATH [--account NAME] [--rpc URL]");
}

const globalModules = join(process.env.APPDATA ?? "", "npm", "node_modules", "genlayer");
const requireFromCli = createRequire(join(globalModules, "package.json"));
const keytar = requireFromCli("keytar");
const credentialKey = await keytar.getPassword("genlayer-cli", `account:${accountName}`);
if (!credentialKey) throw new Error(`GenLayer OS credential is unavailable for account '${accountName}'; unlock it with genlayer account unlock --account ${accountName}`);

const genlayerJsUrl = pathToFileURL(join(globalModules, "node_modules", "genlayer-js", "dist", "index.js"));
const chainsUrl = pathToFileURL(join(globalModules, "node_modules", "genlayer-js", "dist", "chains", "index.js"));
const [{ createAccount, createClient }, { studionet }] = await Promise.all([
  import(genlayerJsUrl.href), import(chainsUrl.href),
]);
const account = createAccount(credentialKey);
const client = createClient({ chain: studionet, endpoint, account });
const callArgs = JSON.parse(await readFile(argsFile, "utf8"));
if (!Array.isArray(callArgs)) throw new Error("args file must contain a JSON array");

const hash = await client.writeContract({
  address: contractAddress,
  functionName: method,
  args: callArgs,
  value: 0n,
});
console.log(JSON.stringify({ submitted: true, hash, account: account.address, method }));
const receipt = await client.waitForTransactionReceipt({ hash, status: "FINALIZED", retries, interval, fullTransaction: true });
console.log(JSON.stringify({ finalized: true, receipt }, (_, value) => typeof value === "bigint" ? value.toString() : value, 2));
const lifecycle = receipt.statusName ?? receipt.status_name;
const consensusResult = receipt.result_name ?? receipt.resultName;
const leaders = receipt.consensus_data?.leader_receipt ?? receipt.consensusData?.leaderReceipt ?? [];
const leader = leaders.find((entry) => entry.mode === "leader");
if (lifecycle !== "FINALIZED" || consensusResult !== "MAJORITY_AGREE" || leader?.execution_result !== "SUCCESS") {
  process.exitCode = 2;
}
