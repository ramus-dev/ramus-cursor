"""Validate the distributable Cursor package without third-party dependencies."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
p = json.loads((root / ".cursor-plugin/plugin.json").read_text())
assert re.fullmatch(r"[a-z0-9]+(?:[.-][a-z0-9]+)*", p["name"])
assert re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", p["version"])
assert p["repository"] == "https://github.com/ramus-dev/ramus-cursor"
assert p["license"] == "MIT"
for value in [p["logo"], p["mcpServers"], *p["skills"]]:
    path = Path(value)
    assert not path.is_absolute() and ".." not in path.parts, value
    assert (root / path).exists(), value
    assert (root / path).resolve().is_relative_to(root), value
mcp = json.loads((root / p["mcpServers"]).read_text())
assert mcp["mcpServers"] == {"ramus": {
    "type": "streamable-http", "url": "https://api.ramus.dev/api/mcp"}}
for skill in p["skills"]:
    text = (root / skill / "SKILL.md").read_text()
    match = re.fullmatch(r"---\n(.*?)\n---\n(.+)", text, re.S)
    assert match, skill
    # This package deliberately uses two plain, single-line metadata fields.
    metadata = dict(line.split(": ", 1) for line in match[1].splitlines())
    assert metadata["name"] == Path(skill).name
    assert 1 <= len(metadata["description"]) <= 1024
    assert match[2].strip()
assert (root / "LICENSE").read_text().startswith("MIT License")
assert (root / p["logo"]).read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
print("PASS: manifest, paths, skill metadata, logo, license and MCP config")
