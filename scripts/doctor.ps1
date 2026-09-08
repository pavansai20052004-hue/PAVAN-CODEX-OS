$ErrorActionPreference = "Continue"
$codexHome = Join-Path $HOME ".codex"

Write-Host "PAVAN CODEX OS doctor"
Write-Host "---------------------"

foreach ($cmd in @("git", "python", "node", "java", "codex")) {
    $found = Get-Command $cmd -ErrorAction SilentlyContinue
    if ($found) { Write-Host ("[OK]   " + $cmd + " -> " + $found.Source) }
    else { Write-Host ("[INFO] " + $cmd + " not found on PATH") }
}

$checks = @(
    (Join-Path $codexHome "AGENTS.md"),
    (Join-Path $codexHome "config.toml"),
    (Join-Path $codexHome "agents")
)
foreach ($path in $checks) {
    if (Test-Path $path) { Write-Host "[OK]   $path" }
    else { Write-Host "[MISS] $path" }
}

$plugins = Join-Path $codexHome "plugins"
if (Test-Path $plugins) {
    $names = Get-ChildItem $plugins -Directory | Select-Object -ExpandProperty Name
    Write-Host ("Local plugin folders: " + ($names -join ", "))
}

Write-Host ""
Write-Host "Usage tip: keep Fast mode off when maximizing hours; use deeper reasoning only when the task needs it."
Write-Host "Run /mcp in supported Codex clients to inspect active MCP servers."
