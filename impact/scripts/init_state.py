#!/usr/bin/env python3
"""Bootstrap IMPACT state directory."""
import os, json, sys
from pathlib import Path

def init(domain, base=".seo"):
    slug = domain.lower().replace(".", "-")
    path = Path(base) / slug
    path.mkdir(parents=True, exist_ok=True)
    config = {
        "version": "1.1.0",
        "product": "MM Rank",
        "vendor": "Media Matchers",
        "domain": domain,
        "homepage": f"https://{domain}",
    }
    (path / "config.json").write_text(json.dumps(config, indent=2))
    for name in ["brand.md", "truth-ledger.md", "content-ledger.md", "radar.md", "action-log.md", "human-queue.md"]:
        (path / name).write_text(f"# {name.replace('.md','').replace('-',' ').title()}\n\n")
    print(json.dumps({"state_path": str(path), "domain": domain}))

if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv) > 1 else "example.com"
    init(domain)
