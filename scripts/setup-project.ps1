param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("react", "python-fastapi", "spring-boot")]
    [string]$Type,

    [Parameter(Mandatory=$true)]
    [string]$ProjectPath,

    [switch]$Force
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $repoRoot ("project-overlays\" + $Type + "\AGENTS.md")
$targetDir = (Resolve-Path $ProjectPath).Path
$target = Join-Path $targetDir "AGENTS.md"

if ((Test-Path $target) -and -not $Force) {
    throw "AGENTS.md already exists at $target. Re-run with -Force only if you intend to replace it."
}

Copy-Item -Force $source $target
Write-Host "Applied $Type Codex overlay to $target"
