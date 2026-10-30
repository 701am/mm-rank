#!/usr/bin/env python3
"""Fetch page text."""
import sys, urllib.request

def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"ERROR: {e}"

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    print(fetch(url)[:5000])
