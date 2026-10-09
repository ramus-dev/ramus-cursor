# Verification

Verified on 2026-10-09. The package is ready for local Cursor testing; it is
not yet approved or listed in the Cursor Marketplace.

## Passed

- Dependency-free package validation: manifest and version, relative paths,
  skill metadata, MIT notice, PNG logo, and expected HTTPS MCP configuration.
- Public OAuth resource discovery: expected resource
  `https://api.ramus.dev/api/mcp` and authorization server `https://api.ramus.dev`.
- Authenticated hosted MCP smoke test through the existing Ramus connector:
  list sessions, start the Meridian demo, inspect the UI, tap Hourly with a
  fresh ref and generation, verify Hourly forecast, return a screenshot,
  read device logs, end the session, and confirm the live-session list is empty.

This exercises the hosted MCP service, not Cursor's OAuth implementation.
No credentials, private APKs or live control URLs are included in this repo.

## Still required before marketplace submission

1. Use a current, signed-in Cursor installation with local imports allowed.
2. Install as described in README and reload. Confirm the plugin's skill
   and MCP server appear in Customize.
3. Complete Ramus OAuth in Cursor and repeat the demo smoke test there.
4. Test a local APK upload with the CLI fallback and separately configured
   CLI credentials. PR, adb, hot reload, camera and microphone workflows
   were not exercised in this smoke test.
5. Submit this public repository at https://cursor.com/marketplace/publish.
   Complete publisher fields and review any agreements in the actual form.
6. Address Cursor's manual review and test installation from the final listing.

The installed Cursor version was 1.6.45. The local Cursor app was signed out and reported an unresponsive extension
host during inspection. Cursor discovery and OAuth remain unverified.
