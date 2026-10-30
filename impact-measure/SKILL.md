---
name: impact-measure
description: MM Rank measure mode. Baseline a site with public pages and pasted Search Console or crawl files. No execute. Use for MM Rank measure, just measure, SEO baseline, vitals snapshot, or record the current organic state.
license: MIT
metadata:
  version: "1.3.0"
  type: workflow
  family: seo
  product: MM Rank
  vendor: Media Matchers
  parent: impact
---

# MM Rank measure

Measure only. No select. No execute.

## Do

1. Bootstrap state if config.json is missing
2. Probe homepage and up to four templates
3. Read robots, sitemap, titles
4. If the user pasted a GSC CSV, parse it
5. Label the four vitals — good / watch / leak / unknown — with evidence
6. Write the run record. Decision line is measure only

Unknown is allowed. Pretend-good is not.
