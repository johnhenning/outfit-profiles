# Outfit public profile guide

- This repo contains public template data and static dotfiles, not CLI/provider code or personal machine details.
- Schema version is 1. Read docs/profile-format.md and the Outfit runtime contract before changing manifest fields.
- Never commit private hostnames, usernames, IP addresses, keys, tokens, auth caches, or resolved secret files. Use generic placeholders and 1Password references in examples.
- Keep defaults minimal. Software discovered on one machine is an optional catalog candidate, not a mandatory install.
- Python uses uv. Do not add mise activation or duplicate Python managers to defaults.
- Add a package mapping only after checking an official vendor/package-manager source. Record manual or unsupported steps honestly.
- Dotfiles are static, explicitly allowlisted and preserve local includes. No executable hooks, remote scripts, or secret template evaluation.
- Validate with Outfit: `outfit catalog --source . --json` and `outfit plan --source . --profile PROFILE --target TARGET --json`.
- CI must preview workstation/dev/compute/media for macos-arm64, debian-amd64, fedora-amd64 and windows-amd64. Never use apply in CI.
- Tag independent profile releases; preserve compatibility with the engine's supported schema. Keep changes and migration notes in CHANGELOG.md.
