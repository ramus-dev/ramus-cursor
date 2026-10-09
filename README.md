# Ramus for Cursor

For humans and agents: inspect and control disposable cloud Android emulators.
This plugin bundles the Ramus MCP connection and an MCP-first skill, with a CLI
fallback for local APK uploads, adb and hot reload.

## Setup and local verification

Clone this repository into the local plugin directory:

```sh
mkdir -p ~/.cursor/plugins/local
git clone https://github.com/ramus-dev/ramus-cursor.git ~/.cursor/plugins/local/ramus
```

If that destination already exists, inspect it before replacing anything. Then
restart Cursor or run **Developer: Reload Window**. Confirm the Ramus skill
and MCP server in **Customize**, connect the server, and complete OAuth
sign-in. Team policy must allow local plugin imports. External symlinks
are not supported; an installed marketplace copy takes precedence.

Try: “Start the Ramus demo on Android, show me a screenshot and share the
browser watch link.” Verify a tap with a fresh snapshot, read device logs,
and end the session. Runtime verification in Cursor is still pending.

MCP needs a Ramus account. CLI fallback needs Node.js 22+ and separate CLI
credentials (or a CLI trial). A Cursor OAuth connection does not configure
CLI authentication. PR previews need the Ramus GitHub App on the repository.
Android only; x86_64 images without Google Play.

## Data and support

The plugin sends APKs and device inputs to the hosted Ramus service and
returns screenshots and logs. Watch links grant device control to their
holders. Current plans and limits: https://ramus.dev.

- Documentation: https://ramus.dev/docs/agents
- Privacy: https://ramus.dev/privacy
- Terms: https://ramus.dev/terms
- Support: hello@ramus.dev

## Open-source scope

This MIT-licensed repository contains the Cursor plugin manifest, skill,
logo and MCP connection configuration. It connects to Ramus's hosted MCP
service; it does not contain or self-host the Ramus backend.

## Validate

Run `python3 scripts/validate.py` for package checks. See
[verification](docs/verification.md) for tested behavior and remaining checks.

## Marketplace submission

Submit https://github.com/ramus-dev/ramus-cursor at
https://cursor.com/marketplace/publish after local Cursor verification.
A public repository is not itself an approved marketplace listing.
