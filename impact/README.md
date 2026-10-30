# MM Rank by Media Matchers — User Manual

The Organic Growth Engine.

This pack is an organic-search desk for Claude Code, Claude Cowork, OpenCode, OpenWork, and Grok. You install the folders, name a site, and the model follows these skills: measure what it can see, rank the work, do one action, check it, file the record.

## Install

Copy every skill folder into the skills directory for your agent. See the root README.md for paths.

Or run from the repo root:

```bash
bash install.sh
```

## Talk to it

| You say | What loads |
|---|---|
| Run MM Rank on example.com | Full loop, one action |
| MM Rank measure on example.com | Baseline only |
| MM Rank write for example.com | One editorial piece |
| Audit example.com | Full diagnostic report |

## State

1. Site git repo → `.seo/` at the repo root
2. This environment → `artifacts/mm-rank/<domain-slug>/`
3. Anywhere else → `./.mm-rank/<domain-slug>/`

## Onboarding a new site

1. Install the skills.
2. Start a new chat and say: `Run MM Rank on example.com`
3. The agent creates the vault, reads the public site, and returns the single best next action.

Built by David Krug / Media Matchers.
