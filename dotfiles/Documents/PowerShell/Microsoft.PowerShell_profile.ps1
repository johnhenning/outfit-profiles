# Outfit baseline. Use the local file for machine-specific configuration.
$localProfile = Join-Path $PSScriptRoot 'profile.local.ps1'
if (Test-Path $localProfile) { . $localProfile }
