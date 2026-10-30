#!/usr/bin/env python3
"""Check AI crawler rules in robots.txt."""
import sys, urllib.request

def check(origin):
    try:
        with urllib.request.urlopen(origin.rstrip('/') + '/robots.txt', timeout=10) as r:
            text = r.read().decode('utf-8', errors='ignore')
        bots = ['GPTBot', 'ClaudeBot', 'PerplexityBot', 'Google-Extended']
        found = [b for b in bots if b in text]
        return {"origin": origin, "ai_bots_mentioned": found}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    origin = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    import json
    print(json.dumps(check(origin), indent=2))
