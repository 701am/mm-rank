#!/usr/bin/env python3
"""Extract internal and external hrefs from a page."""
import argparse, json, ssl, urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag != 'a': return
        for k, v in attrs:
            if k.lower() == 'href' and v:
                self.hrefs.append(v.strip())

def fetch(url, timeout):
    req = urllib.request.Request(url, headers={'User-Agent': 'mm-rank-links/1.1'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', errors='replace'), r.geturl()

def main():
    p = argparse.ArgumentParser()
    p.add_argument('url')
    p.add_argument('--timeout', type=float, default=15)
    args = p.parse_args()
    html, final = fetch(args.url, args.timeout)
    parser = LinkParser()
    parser.feed(html)
    base = urlparse(final)
    internal, external = [], []
    for href in parser.hrefs:
        abs_url = urljoin(final, href)
        if urlparse(abs_url).netloc == base.netloc:
            internal.append(abs_url)
        else:
            external.append(abs_url)
    print(json.dumps({'url': args.url, 'internal_count': len(internal), 'external_count': len(external)}, indent=2))

if __name__ == '__main__':
    main()
