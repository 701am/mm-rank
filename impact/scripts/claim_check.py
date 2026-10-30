#!/usr/bin/env python3
"""Flag live-page phrases that look like unsourced claims vs the truth ledger."""
import argparse, json, re
from pathlib import Path

PATTERNS = (r'\bonly\b', r'\b#1\b', r'\bguaranteed\b', r'\bbest\b', r'\bleading\b', r'\bnever\b', r'\balways\b')

def snippets(text):
    found = []
    low = text.lower()
    for pat in PATTERNS:
        for m in re.finditer(pat, low, flags=re.I):
            start = max(0, m.start() - 40)
            end = min(len(text), m.end() + 40)
            found.append({'pattern': pat, 'excerpt': text[start:end].strip()})
    return found

def main():
    p = argparse.ArgumentParser()
    p.add_argument('html_or_text')
    p.add_argument('--dir', default='')
    args = p.parse_args()
    raw = Path(args.html_or_text).read_text(encoding='utf-8', errors='replace')
    hits = snippets(raw)
    print(json.dumps({'hits': len(hits), 'unsourced': hits[:30]}, indent=2))

if __name__ == '__main__':
    main()
