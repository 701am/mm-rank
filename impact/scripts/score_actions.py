#!/usr/bin/env python3
"""Score candidate actions."""
import json, sys

def score(impact, confidence, learn, cost):
    return (impact * confidence * learn) / max(cost, 0.25)

if __name__ == "__main__":
    # Example usage
    candidates = [
        {"name": "refresh title", "impact": 4, "confidence": 0.8, "learn": 1.0, "cost": 0.5},
        {"name": "new guide", "impact": 3, "confidence": 0.5, "learn": 1.0, "cost": 4.0},
    ]
    for c in candidates:
        c["score"] = score(c["impact"], c["confidence"], c["learn"], c["cost"])
    print(json.dumps(sorted(candidates, key=lambda x: -x["score"]), indent=2))
