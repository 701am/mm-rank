# MM Rank — The Organic Growth Engine by Media Matchers

**MM Rank is a daily organic SEO desk that lives inside your AI agent.**

It measures what is actually visible, ranks every possible action on one scale, executes the single highest-leverage move, verifies the result, and files the record. One action per run. No content quotas. No invented rankings.

Built for solo founders, small SEO teams, and agencies who want staff-level discipline without a staff.

**Public price: $99** (full pack + free built-with-you first site vault).

---

## What MM Rank is

Most AI SEO tools give you a long report and leave you to decide what to do next. MM Rank does the deciding.

On every run it:

1. **Measures** — public pages, robots/sitemap, titles, headers, and any Search Console or crawl data you paste.
2. **Scores** — every candidate action on one formula: impact × confidence × learn / cost.
3. **Executes** — exactly one move (a title refresh, a redirect patch, an editorial draft, a technical fix).
4. **Verifies** — against the quality bars for that lane.
5. **Registers** — a run record so the next session starts smarter.

Repair, refresh, and claim-correction beat new pages when the numbers say so. A run that records “nothing beats the bar” is a success.

The pack ships with the daily operator, forced-mode shortcuts, a full diagnostic suite, and two companions (brand voice + humanizer).

---

## How the daily loop works

```
Foundation → Measure → Select → Execute one → Verify → Register
```

| Step | What happens |
|------|--------------|
| **Foundation** | Creates or reads the site vault. Loads brand, truth ledger, content ledger, radar, action log. Does not overwrite files that already have content. |
| **Measure** | Probes the homepage and a few templates. Reads robots, sitemaps, titles. Parses a GSC file if you pointed at one. Labels four vitals: speed, relevance, clicks, links. |
| **Select** | Builds 5–12 candidates from evidence only. Scores them. Repair / refresh beat new pages when scores sit within 15%. |
| **Execute** | The winner only. Ships a draft, a patch plan, a brief, or a page outline — not a manifesto. |
| **Verify** | Gates in the lane file and `quality-bars.md`. Failed work is logged as failed. |
| **Register** | Run record + action log + human queue. Next run starts from the updated record. |

A run that records “nothing beats the bar” is finished work. Do not invent a blog post to fill the hour.

---

## How to onboard a new site

First run on a domain takes about 15 minutes. After that, daily runs are short.

### 1. Install the skills
See the Install section below. Restart your agent or start a new chat so the skills are discovered.

### 2. Start a run
In any new chat with the agent, say:

```
Run MM Rank on example.com
```

Or more specifically:

```
MM Rank measure on example.com
```

The agent will:

- Create a state vault (`.seo/` in the site repo, or `artifacts/mm-rank/<domain-slug>/`).
- Bootstrap the foundation files (brand, truth ledger, content ledger, radar, action log).
- Read the homepage, nav, robots.txt, sitemap, and one money page.
- Write a first vitals snapshot and recommend the single best next action.

### 3. Fill the foundation (optional but high-leverage)
The first run works with public pages alone. To make later runs sharper, drop these into the vault when you have them:

| File | What it unlocks |
|------|-----------------|
| Search Console export (CSV) | Striking-distance queries, CTR vs expected, decay |
| Crawl export (Screaming Frog / Sitebulb) | Orphans, status codes at scale |
| Brand one-liner + competitors | Better editorial voice and angle selection |
| Pricing / claims you stand behind | Truth ledger so the agent never invents |

You can also say:

```
MM Rank setup on example.com
```

The agent will print exactly which integrations are missing and what each one unlocks.

### 4. Daily use
After the first vault exists, just say:

```
Run MM Rank
```

or

```
Best next SEO move on example.com
```

The agent reads the existing vault, measures light, picks one action, and registers the result. You review the draft or patch, ship it, and the next run starts from the updated record.

---

## What’s in the box

### Daily operator
- **impact** — Full loop: foundation → measure → select → one action → verify → register.
- **seo-ops** — Compatibility alias that loads the same loop.

### Forced-mode skills
Each one is a forced lane. Still measures. Still files a record. Skips the beauty contest across lanes.

- **impact-measure** — Baseline only. Four vitals, no execute.
- **impact-write** — One editorial piece that earns its place.
- **impact-aeo** — Citability packaging for AI Overviews / ChatGPT / Perplexity.
- **impact-tech** — One technical defect, smallest correct patch.
- **impact-offpage** — One outreach brief (does not send mail).

### Diagnostic pack (reports, not the daily loop)
- **seo** — Universal orchestrator that routes to the right specialist.
- **seo-audit** — Full site health report.
- **seo-page** — Deep single-URL teardown.
- **seo-technical**, **seo-content**, **seo-schema**, **seo-geo**, **seo-local**, **seo-plan**, **seo-content-brief**, **seo-pr**.
- **seo-cluster** — SERP-overlap clustering + hub-and-spoke architecture.
- **seo-sxo** — Search experience / page-type mismatch diagnosis.
- **seo-drift** — Baseline + change detection.
- **seo-images** — Image SEO audit.
- **seo-sitemap** — Sitemap analysis and drafting.

### Companions
- **humanizer** — Strips AI writing patterns before anything leaves the building.
- **client-context** — Brand voice, products, competitors, truth ledger.

All Python tools use only the standard library. No paid APIs required. Measurements are labeled. No invented rankings, CWV field data, or backlink counts.

---

## Install

The skills use the open Agent Skills format (`SKILL.md`). They work in Claude Code, Claude Cowork, OpenCode, and OpenWork without modification.

### Claude Code
```bash
# Personal (available in every project)
mkdir -p ~/.claude/skills
cp -a impact impact-* seo* humanizer client-context ~/.claude/skills/

# Or project-scoped (commit with the repo)
mkdir -p .claude/skills
cp -a impact impact-* seo* humanizer client-context .claude/skills/
```

Claude Code picks up new skills without a restart. Run `/skills` or ask “what skills are available?”

### Claude Cowork
Cowork uses the same skill system as Claude. Install to `~/.claude/skills/` (or upload as a plugin bundle). Skills appear in Cowork sessions the same way they do in Claude Code.

### OpenCode / OpenWork
OpenCode (and OpenWork, which is built on it) reads skills from several locations, including Claude-compatible paths:

```bash
# Personal
mkdir -p ~/.agents/skills
cp -a impact impact-* seo* humanizer client-context ~/.agents/skills/

# Or Claude-compatible path (also read by OpenCode / OpenWork)
mkdir -p ~/.claude/skills
cp -a impact impact-* seo* humanizer client-context ~/.claude/skills/

# Project-scoped
mkdir -p .opencode/skills
cp -a impact impact-* seo* humanizer client-context .opencode/skills/
```

### Auto-detect installer
From this repo root:

```bash
bash install.sh
```

The script detects Claude, OpenCode/OpenWork, or Grok and copies every skill folder into the right location.

---

## How to talk to it

| You say | What happens |
|---------|--------------|
| Run MM Rank on example.com | Full loop, one best action |
| MM Rank measure on example.com | Vitals only |
| MM Rank write for example.com | One editorial URL |
| MM Rank aeo on https://example.com/guide | Citability fix |
| MM Rank tech on example.com | One technical patch |
| MM Rank offpage on example.com | One outreach brief |
| Audit example.com | Full diagnostic report (no execute) |
| Analyze this page: [url] | Single-URL teardown |
| Cluster the SERP for “best CRM” | Hub-and-spoke architecture |
| What’s missing for example.com? | Integration checklist |

---

## State and vaults

MM Rank keeps durable state so each run starts smarter than the last.

Preferred location (when working inside the site repo):

```
.seo/
├── config.json
├── brand.md
├── truth-ledger.md
├── content-ledger.md
├── radar.md
├── action-log.md
├── human-queue.md
└── runs/
```

Fallback locations:
- This environment → `artifacts/mm-rank/<domain-slug>/`
- Anywhere else → `./.mm-rank/<domain-slug>/`

Domain slug is the registrable domain, lowercase, dots to hyphens (`example.com` → `example-com`).

---

## Scoring

Candidate JSON in, ranked list out.

```
score = (impact × confidence × learn) / max(cost, 0.25)
```

- `impact` 0–5 expected movement across vitals (repair on a converting template scores high)
- `confidence` 0–1 how directly measured (pasted GSC row = 0.9; homepage sniff = 0.4)
- `learn` starts at 1.0; after 4+ logged actions of that class, use hit-rate from the action log
- `cost` estimated hours including review (0.25–16)

Minimum bar to execute on a default run — score ≥ 2.0 and confidence ≥ 0.35. Otherwise register “nothing beats the bar” with the top three held.

Priority bias when scores tie — correct > repair > refresh > consolidate > prune > aeo > distribute > offpage > editorial > programmatic > tools.

Never pick editorial, programmatic, or tools if a correct / repair / refresh candidate is within 15% of its score.

---

## What this pack will not do

- Buy links, PBNs, or citation blasts
- Guarantee AI Overview inclusion
- Forecast traffic or revenue multiples
- Overwrite live production
- Run a content quota (“write 12 posts this month”) as success

---

## Support

First vault is built with you. Ongoing questions via the Media Matchers channel.

---

## License

MIT. See [LICENSE](LICENSE).

Adapted and extended from the excellent open-source work in [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo). The daily MM Rank loop, scoring model, forced-mode skills, and Media Matchers packaging are original.

Built by David Krug / Media Matchers.
