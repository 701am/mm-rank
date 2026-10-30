#!/usr/bin/env python3
"""Expected CTR heuristic by position."""
import json, sys

def expected_ctr(pos):
    # Rough heuristic; label as estimate
    table = {1: 28.0, 2: 15.0, 3: 11.0, 4: 8.0, 5: 6.0, 6: 4.5, 7: 3.5, 8: 2.5, 9: 2.0, 10: 1.5}
    return table.get(int(pos), 1.0)

if __name__ == "__main__":
    pos = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    print(json.dumps({"position": pos, "expected_ctr_pct_heuristic": expected_ctr(pos)}))
