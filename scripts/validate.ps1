$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Push-Location $root
try {
    if (Get-Command py -ErrorAction SilentlyContinue) {
        py -3 scripts/validate_repo.py
    } elseif (Get-Command python -ErrorAction SilentlyContinue) {
        python scripts/validate_repo.py
    } else {
        throw "Python 3 was not found on PATH."
    }
} finally {
    Pop-Location
}
