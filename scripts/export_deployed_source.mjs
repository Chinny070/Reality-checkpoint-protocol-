// Export exact deployed source bytes through the GenLayer SDK client.
// Usage: node scripts/export_deployed_source.mjs <contract-address> <output-file>
import { dirname, join } from "node:path";
import { pathToFileURL } from "node:url";
import { mkdir, writeFile } from "node:fs/promises";

const [address, output] = process.argv.slice(2);
if (!address || !output) throw new Error("usage: node scripts/export_deployed_source.mjs <address> <output-file>");
const globalModules = join(process.env.APPDATA ?? "", "npm", "node_modules", "genlayer");
const [{ createClient }, { studionet }] = await Promise.all([
  import(pathToFileURL(join(globalModules, "node_modules", "genlayer-js", "dist", "index.js")).href),
  import(pathToFileURL(join(globalModules, "node_modules", "genlayer-js", "dist", "chains", "index.js")).href),
]);
const client = createClient({ chain: studionet, endpoint: "https://studio.genlayer.com/api" });
await client.initializeConsensusSmartContract();
const source = await client.getContractCode(address);
await mkdir(dirname(output), { recursive: true });
await writeFile(output, source, "utf8");
console.log(JSON.stringify({ address, output, bytes: Buffer.byteLength(source, "utf8") }));
