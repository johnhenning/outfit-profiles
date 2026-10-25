# Outfit profiles

Public, reusable templates for [Outfit](https://github.com/johnhenning/outfit). No personal hostnames, usernames, account sessions, credentials or private keys belong here.

`outfit.yaml` is schema version 1. It defines packages, platform package mappings, software categories, roles, presets, named profiles, and allowlisted static dotfiles. The file uses JSON syntax, which is valid YAML, to make its types unambiguous.

Profiles:

- `workstation`: Chrome and VS Code plus basic development tools.
- `dev`: headless development environment, including WSL.
- `compute`: headless baseline and monitoring.
- `media`: media processing baseline; configure a server and storage explicitly.

The common CLI baseline is Git, curl, GitHub CLI, uv and jq. Development adds
Ruff, pre-commit, Node and pnpm; the headless development role also includes
tmux, ripgrep and fd. GUI-only defaults are skipped for headless roles.

Defaults do not select a password manager, premium Mac utilities, a shell
framework/theme, a custom terminal, Rust/C++ tools, containers, or cloud/ML
providers. Those are optional choices, not assumptions about every machine.
The catalog retains alternatives such as Firefox, Chromium, Cursor and other
terminals; their presence in the catalog does not install them.

Presets add deliberate optional groups:

- `desktop`: Chrome.
- `dev`: the basic development set and VS Code where a desktop is available.
- `ai-assistants`: ChatGPT and Claude desktop apps where supported.
- `build`: CMake, Ninja and Rust.
- `containers`: Docker tooling.
- `entertainment`: Spotify and Steam.
- `cloud-ml`: AWS/Azure CLIs and the existing ML tools; opt in only as needed.

Advanced setup allows per-category alternatives and exclusions. A preferred app
replaces inherited choices in its category, while explicit includes retain extra
apps. Preferences choose packages to install; they do not set OS app associations.
Python uses uv; mise is excluded.

CLI implementation and platform command recipes belong in Outfit. This repository supplies only data and static config; it cannot define shell installers or executable hooks. Unsupported/unverified installers are marked manual rather than executed speculatively. Homebrew mappings are checked against official metadata in `catalog-validation.json`; other providers still require clean-machine verification.

Clone alongside Outfit, then preview:

```sh
../outfit/bin/outfit plan --source . --profile compute --target debian-amd64
../outfit/bin/outfit setup --source .
```

Dotfiles are opt-in: use `shell-config`, `tmux-config`, `git-config` (Git ignore
rules only), `ssh-config`, or `powershell-config` presets. No public profile
selects them automatically. For example:

```sh
../outfit/bin/outfit plan --source . --profile dev --preset shell-config,tmux-config,git-config --target debian-amd64
```

The shell template preserves the editor setting, falls back to `vi`, and does
not activate a shell framework or theme. Templates use explicit source/target
mappings and local-only includes. Existing SSH configs require manual merging.
Personal overlays use separate profile names and may add packages/configs;
collisions are rejected instead of silently replacing public definitions. Keep
personal account data and machine details in a private overlay, and secret values
in a credential manager such as 1Password. Version only references to secrets.

Migrating from alpha.1: public browser/editor defaults change from Firefox/Cursor
to Chrome/VS Code. Explicitly select your preferred alternatives to retain them.
Optional tools and dotfiles are no longer implicit. Plans only describe desired
actions; changing profiles does not uninstall existing apps or remove old configs.
Previously released one-line installers remain pinned to their published bundle
until a coordinated profile/runtime release updates those pins.

Profile release archives contain `outfit.yaml` at the archive root, are independently versioned, and are pinned by SHA-256 in direct-profile bootstrap scripts.
