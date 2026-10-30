#!/usr/bin/env python3
"""Probe many URLs. Args or a text file, one URL per line."""
import argparse, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

def probe(url, timeout):
    proc = subprocess.run([sys.executable, str(HERE / 'health_probe.py'), url, '--timeout', str(timeout), '--json'], capture_output=True, text=True)
    if proc.returncode != 0:
        return {'url': url, 'ok': False, 'error': proc.stderr.strip() or proc.stdout.strip()}
    try:
        return json.loads(proc.stdout)
    except:
        return {'url': url, 'ok': False, 'error': 'unreadable probe output'}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('urls', nargs='*')
    p.add_argument('--file')
    p.add_argument('--timeout', type=float, default=20)
    args = p.parse_args()
    urls = list(args.urls)
    if args.file:
        urls.extend(line.strip() for line in Path(args.file).read_text().splitlines() if line.strip() and not line.startswith('#'))
    if not urls:
        raise SystemExit('pass URLs or --file')
    print(json.dumps([probe(u, args.timeout) for u in urls], indent=2))

if __name__ == '__main__':
    main()
