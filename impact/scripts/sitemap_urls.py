#!/usr/bin/env python3
"""Extract URLs from sitemap."""
import sys, urllib.request, re

def urls(sitemap):
    try:
        with urllib.request.urlopen(sitemap, timeout=10) as r:
            text = r.read().decode('utf-8', errors='ignore')
        return re.findall(r'<loc>(.*?)</loc>', text)[:50]
    except Exception as e:
        return []

if __name__ == "__main__":
    sm = sys.argv[1] if len(sys.argv) > 1 else "https://example.com/sitemap.xml"
    for u in urls(sm):
        print(u)
