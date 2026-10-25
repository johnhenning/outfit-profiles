# Outfit profiles

Public, reusable templates for [Outfit](https://github.com/johnhenning/outfit). No personal hostnames, usernames, account sessions, credentials or private keys belong here.

`outfit.yaml` is schema version 1. It defines packages, platform package mappings, software categories, roles, presets, named profiles, and allowlisted static dotfiles. The file uses JSON syntax, which is valid YAML, to make its types unambiguous.

Profiles:

- `workstation`: desktop apps plus development tools.
- `dev`: headless development environment, including WSL.
- `compute`: headless baseline and monitoring.
- `media`: media processing baseline; configure a server and storage explicitly.

Presets can add dev, desktop, entertainment and cloud/ML tools. Advanced setup allows per-category alternatives and exclusions. Python uses uv; mise is excluded.

CLI implementation and platform command recipes belong in Outfit. This repository supplies only data and static config; it cannot define shell installers or executable hooks. Unsupported/unverified installers are marked manual rather than executed speculatively. Homebrew mappings are checked against official metadata in `catalog-validation.json`; other providers still require clean-machine verification.

Clone alongside Outfit, then preview:

```sh
../outfit/bin/outfit plan --source . --profile compute --target debian-amd64
../outfit/bin/outfit setup --source .
```

Dotfiles use explicit source/target mappings. Local-only includes preserve machine overrides. Existing SSH configs require manual merging. Optional personal overlays use separate profile names and may add packages/configs; collisions are rejected instead of silently replacing public definitions. Store secret values in 1Password and version only references.

Profile release archives contain `outfit.yaml` at the archive root, are independently versioned, and are pinned by SHA-256 in direct-profile bootstrap scripts.
