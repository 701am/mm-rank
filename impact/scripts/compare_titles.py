#!/usr/bin/env python3
"""Compare a candidate title against current title length and overlap."""
import argparse, json, re

def tokens(s):
    return set(re.findall(r'[a-z0-9]+', s.lower()))

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--current', required=True)
    p.add_argument('--candidate', required=True)
    args = p.parse_args()
    ct, cdt = tokens(args.current), tokens(args.candidate)
    print(json.dumps({
        'current': args.current,
        'candidate': args.candidate,
        'current_chars': len(args.current),
        'candidate_chars': len(args.candidate),
        'shared_tokens': sorted(ct & cdt),
        'new_tokens': sorted(cdt - ct),
        'length_band_ok': 35 <= len(args.candidate) <= 65,
    }, indent=2))

if __name__ == '__main__':
    main()
