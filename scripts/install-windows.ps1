param(
    [switch]$SkipBackup
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$codexHome = Join-Path $HOME ".codex"
$backupRoot = Join-Path $codexHome ("pavan-codex-os-backup-" + (Get-Date -Format "yyyyMMdd-HHmmss"))

function Backup-IfExists([string]$Path, [string]$RelativeName) {
    if ((Test-Path $Path) -and -not $SkipBackup) {
        $dest = Join-Path $backupRoot $RelativeName
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dest) | Out-Null
        Copy-Item -Recurse -Force $Path $dest
    }
}

New-Item -ItemType Directory -Force -Path $codexHome | Out-Null

$globalAgents = Join-Path $codexHome "AGENTS.md"
Backup-IfExists $globalAgents "AGENTS.md"
Copy-Item -Force (Join-Path $repoRoot "AGENTS.md") $globalAgents

$agentsDest = Join-Path $codexHome "agents"
Backup-IfExists $agentsDest "agents"
New-Item -ItemType Directory -Force -Path $agentsDest | Out-Null
Copy-Item -Force (Join-Path $repoRoot ".codex\agents\*.toml") $agentsDest

$configDest = Join-Path $codexHome "config.toml"
if (-not (Test-Path $configDest)) {
    Copy-Item -Force (Join-Path $repoRoot ".codex\config.toml") $configDest
} else {
    Write-Host "Existing config.toml preserved. Review .codex/config.toml in this repo and merge desired settings manually."
}

$pluginSource = Join-Path $repoRoot "plugins\pavan-codex-os"
$pluginDest = Join-Path $codexHome "plugins\pavan-codex-os"
Backup-IfExists $pluginDest "plugins\pavan-codex-os"
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $pluginDest) | Out-Null
if (Test-Path $pluginDest) { Remove-Item -Recurse -Force $pluginDest }
Copy-Item -Recurse -Force $pluginSource $pluginDest

Write-Host "PAVAN CODEX OS installed."
Write-Host "Global instructions: $globalAgents"
Write-Host "Agents: $agentsDest"
Write-Host "Plugin: $pluginDest"
if (-not $SkipBackup) { Write-Host "Backups (when needed): $backupRoot" }
Write-Host "Restart Codex to reload configuration."
