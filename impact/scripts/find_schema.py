#!/usr/bin/env python3
"""Find JSON-LD @types on a page."""
import argparse, json, re, urllib.request

def fetch(url, timeout):
    req = urllib.request.Request(url, headers={'User-Agent': 'mm-rank-schema/1.1'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', errors='replace')

def types_from_obj(obj):
    found = []
    if isinstance(obj, dict):
        t = obj.get('@type')
        if isinstance(t, str): found.append(t)
        elif isinstance(t, list): found.extend(str(x) for x in t)
        for v in obj.values(): found.extend(types_from_obj(v))
    elif isinstance(obj, list):
        for v in obj: found.extend(types_from_obj(v))
    return found

def main():
    p = argparse.ArgumentParser()
    p.add_argument('url')
    p.add_argument('--timeout', type=float, default=15)
    args = p.parse_args()
    html = fetch(args.url, args.timeout)
    blocks = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, flags=re.I|re.S)
    types = []
    for raw in blocks:
        try: types.extend(types_from_obj(json.loads(raw)))
        except: pass
    print(json.dumps({'url': args.url, 'jsonld_blocks': len(blocks), 'jsonld_types': sorted(set(types))}, indent=2))

if __name__ == '__main__':
    main()
