#!/usr/bin/env python3
"""Add vault files to an MM Rank state dir without clobbering."""
import argparse, json
from pathlib import Path
import shutil

SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSETS = SKILL_ROOT / 'assets' / 'vault'
COPIES = {'memory.md': 'memory.template.md', 'intake.md': 'intake.template.md', 'kpis.md': 'kpis.template.md'}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--dir', required=True)
    p.add_argument('--name', default='')
    args = p.parse_args()
    state = Path(args.dir).expanduser().resolve()
    state.mkdir(parents=True, exist_ok=True)
    for d in ['pr', 'snapshots', 'imports']:
        (state / d).mkdir(exist_ok=True)
    for dest_name, src_name in COPIES.items():
        dest = state / dest_name
        src = ASSETS / src_name
        if dest.exists():
            print(f'keep {dest}')
            continue
        if src.exists():
            shutil.copyfile(src, dest)
            print(f'wrote {dest}')
    cfg = state / 'config.json'
    if cfg.exists():
        data = json.loads(cfg.read_text())
        data['vault_path'] = str(state)
        if args.name: data['client_name'] = args.name
        data['product'] = data.get('product') or 'MM Rank'
        cfg.write_text(json.dumps(data, indent=2) + '\n')
    print(f'vault ready: {state}')

if __name__ == '__main__':
    main()
