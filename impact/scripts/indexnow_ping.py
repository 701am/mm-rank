#!/usr/bin/env python3
"""POST to IndexNow. Refuses to run without a key and at least one URL."""
import argparse, json, urllib.request

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--host', required=True)
    p.add_argument('--key', required=True)
    p.add_argument('--key-location', default='')
    p.add_argument('--url', action='append', dest='urls', required=True)
    p.add_argument('--endpoint', default='https://api.indexnow.org/indexnow')
    p.add_argument('--dry-run', action='store_true')
    args = p.parse_args()
    payload = {'host': args.host, 'key': args.key, 'urlList': args.urls}
    if args.key_location:
        payload['keyLocation'] = args.key_location
    if args.dry_run:
        print(json.dumps({'dry_run': True, 'payload': payload}, indent=2))
        return
    data = json.dumps(payload).encode()
    req = urllib.request.Request(args.endpoint, data=data, method='POST', headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            print(json.dumps({'status': r.status, 'body': r.read().decode()[:2000]}))
    except Exception as e:
        print(json.dumps({'error': str(e)}))

if __name__ == '__main__':
    main()
