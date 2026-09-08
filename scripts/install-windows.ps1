param(
    [switch]$SkipBackup,
    [switch]$InstallDesignStudio,
    [switch]$InstallBackendLab,
    [switch]$InstallAllPlugins
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

function Install-PluginFolder([string]$Name) {
    $source = Join-Path $repoRoot ("plugins\" + $Name)
    $dest = Join-Path $codexHome ("plugins\" + $Name)
    if (-not (Test-Path $source)) { throw "Plugin source missing: $source" }
    Backup-IfExists $dest ("plugins\" + $Name)
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dest) | Out-Null
    if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
    Copy-Item -Recurse -Force $source $dest
    Write-Host "Installed local plugin folder: $Name"
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
    Write-Host "Existing config.toml preserved. Merge desired balanced defaults manually if needed."
}

Get-ChildItem (Join-Path $repoRoot ".codex\profiles\*.config.toml") | ForEach-Object {
    $dest = Join-Path $codexHome $_.Name
    Backup-IfExists $dest $_.Name
    Copy-Item -Force $_.FullName $dest
}

Install-PluginFolder "pavan-codex-os"
if ($InstallAllPlugins -or $InstallDesignStudio) { Install-PluginFolder "pavan-design-studio" }
if ($InstallAllPlugins -or $InstallBackendLab) { Install-PluginFolder "pavan-backend-lab" }

Write-Host ""
Write-Host "PAVAN CODEX OS installed."
Write-Host "Global instructions: $globalAgents"
Write-Host "Agents: $agentsDest"
Write-Host "Core plugin: pavan-codex-os"
Write-Host "Profiles: pavan-economy, pavan-balanced, pavan-deep"
if (-not $InstallDesignStudio -and -not $InstallAllPlugins) { Write-Host "Design Studio not installed (use -InstallDesignStudio or -InstallAllPlugins when wanted)." }
if (-not $InstallBackendLab -and -not $InstallAllPlugins) { Write-Host "Backend Lab not installed (use -InstallBackendLab or -InstallAllPlugins when wanted)." }
if (-not $SkipBackup) { Write-Host "Backups (when needed): $backupRoot" }
Write-Host "Restart Codex after install. Local plugin folders may still need import/enablement through the Codex plugin UI depending on your build."
