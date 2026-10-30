# CMS patches

Smallest correct change for common CMS issues.

## WordPress
- Noindex on staging: add `noindex` via robots.txt or Yoast/RankMath
- Broken canonical: check theme or SEO plugin settings
- Missing sitemap: enable in SEO plugin or use a dedicated plugin

## Shopify
- Duplicate content from collections: use canonical tags
- Missing product schema: enable in theme or app

## Webflow
- Missing meta descriptions: set per page in CMS
- Broken redirects: use Webflow redirect settings

## Custom
- Missing headers: add via server config or middleware
- No sitemap: generate and submit
