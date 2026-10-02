param(
  [string]$Network = "studionet",
  [string]$Contract = "contracts/reality_checkpoint.py",
  [switch]$Deploy
)
$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

if (-not (Test-Path -LiteralPath $Contract)) { throw "Contract file not found: $Contract" }
genvm-lint check $Contract
if ($LASTEXITCODE -ne 0) { throw "GenVM validation failed" }
genvm-lint schema $Contract
if ($LASTEXITCODE -ne 0) { throw "GenVM schema extraction failed" }

if (-not $Deploy) {
  Write-Host "Preflight passed. To submit a deployment transaction, rerun with -Deploy."
  exit 0
}

if ($Network -ne "studionet") { throw "Canonical deployment is restricted to studionet in this script." }
$rpc = "https://studio.genlayer.com/api"
if (-not (Get-Command genlayer -ErrorAction SilentlyContinue)) { throw "GenLayer CLI not installed; see docs/DEPLOYMENT.md." }
Write-Host "Deploying $Contract to Studionet RPC $rpc"
genlayer deploy --contract $Contract --rpc $rpc
if ($LASTEXITCODE -ne 0) { throw "GenLayer deployment command failed with exit code $LASTEXITCODE" }
