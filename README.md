# SuperCheap MCP Registry metadata

Public metadata for the published `io.github.hardtab/supercheap-shopping` entry, version `0.1.0`.

- Website: https://supercheap.market/
- Remote endpoint: https://supercheap.market/mcp (Streamable HTTP, customer OAuth required)
- Connection guide: https://supercheap.market/us-en/use-supercheap-with-ai/
- Support: https://supercheap.market/support/ · support@supercheap.market

## Status

Version `0.1.0` is published in the [Official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.hardtab%2Fsupercheap-shopping/versions/0.1.0). Independent lookup on 1 October 2026 verified the exact namespace, version, website and Streamable HTTP endpoint; the Registry reports `status=active` and `isLatest=true`, published at `2026-10-01T05:19:07.625706Z`. [Protected publication run 36818380344](https://github.com/hardtab/supercheap-mcp/actions/runs/36818380344) succeeded on metadata revision `a77b0411b1f7516c95654dd7206f7db4b68e7484` after human approval. Authenticated client acceptance remains unverified. This repository contains no server implementation, customer data, reviewer fixtures or long-lived credentials.

On 1 October 2026, Backend release `2fc707d63d67177f3c8ff9b52ab5012677fa7d57` was deployed and accepted by [main CI](https://github.com/hardtab/supercheap-backend/actions/runs/36806943701). Public readiness returned HTTP 200 with that release and digest `sha256:c3a07b373e71a3e5aefda980b473b395795644dd8f5b11fd788f72b8432c8cd6`; OAuth metadata advertises CIMD support. The exact read-only publisher preflight passed again after acceptance. [Production audit](https://github.com/hardtab/supercheap-backend/actions/runs/36811167290) passed and confirmed the existing 30 September lifecycle aggregate survived container replacement, with valid daily and TTL indexes. [Container checks](https://github.com/hardtab/supercheap-backend/actions/runs/36811153235) also passed; the checkout log confirms exact source `2fc707d63d67177f3c8ff9b52ab5012677fa7d57`. These checks establish runtime and public metadata readiness; authenticated client acceptance remains unverified.

## Directory listings

Directory evidence verified on 2–3 October 2026:

- [Smithery](https://smithery.ai/servers/hardtab/supercheap-shopping) — authenticated scan completed successfully on 1 October 2026 and reports 33 tools.
- [Glama](https://glama.ai/mcp/connectors/io.github.hardtab/supercheap-shopping) — Connected on 3 October 2026 after PR 26; Inspector shows 33 tools. `market_list` (TH/THB and US/USD, checkout-enabled), `catalog_search_products` (US/en shoulder bag, limit 3, expand suppliers false → 3 of 5), and `catalog_get_product` (existing fixture with variants) called successfully.
- [mcpi](https://mcpi.app/servers/supercheap) — card imported from the root endpoint `https://supercheap.market/mcp` and public OAuth metadata; owner claim and contract snapshot pending.

Glama confirms authenticated tool discovery and bounded catalog reads. Cart, checkout, refresh, revoke, and other clients remain unverified. [PR 26](https://github.com/hardtab/supercheap-backend/pull/26) (merged `979aaad`) and [PR 27](https://github.com/hardtab/supercheap-backend/pull/27) (ledger `f073`) record production deployment and live evidence.

## Protected publication

Environment configuration was verified on 1 October 2026: required human reviewer, exactly the `main` branch allowed, and administrator bypass disabled. [Publication run 36811212516](https://github.com/hardtab/supercheap-mcp/actions/runs/36811212516) used exact metadata revision `7caa540794754e83afccb4767207da994d79c42a`; after manual approval, it failed at CLI manifest validation before requesting an OIDC identity because the pinned container lacked trusted system CA roots for Registry TLS. The workflow update binds only the GitHub-hosted runner's trusted system CA bundle read-only into the pinned container and sets `SSL_CERT_FILE`. The [validation-only run 36818178152](https://github.com/hardtab/supercheap-mcp/actions/runs/36818178152) passed on the repaired revision. The subsequent protected publication run 36818380344 succeeded after human review. The earlier failed run did not publish a listing.

The workflow runs only by manual dispatch from `main` in this exact repository, with `confirm_publish=true`. Before each dispatch, verify that the `mcp-registry-publish` environment still requires a human reviewer, allows exactly the `main` branch, and has administrator bypass disabled. The reviewer must inspect that exact run, manifest and workflow before approval. Automation must never approve or bypass its own deployment. A sole owner may manually approve their own dispatch; independent-review prevention is optional additional protection.

Review changes through pull requests before merging to `main`. The GitHub OIDC publisher permission covers `io.github.hardtab/*`, so the exact repository, branch, manifest and approval controls are significant.

The hosted runner checks the environment and public customer-only OAuth/readiness boundary before requesting a short-lived Registry identity. The official Registry publisher is checksum-pinned; its runtime image is digest-pinned. Public artifacts and the single system CA bundle are mounted read-only; the workflow stops before OIDC login if the runner bundle is missing, unreadable, or empty. CLI credentials exist only in root-owned tmpfs inside a disposable container. No publisher token, PAT or signing key belongs in this repository.

After publication, the workflow verifies the final official HTTPS Registry origin/version path and the exact declared remote set, title and website. That lookup proves listing publication only. Verify OAuth, buyer tools, refresh and revocation independently in each supported client before claiming client acceptance.

## Files

- `server.json`: published public Registry manifest.
- `.github/workflows/mcp-registry-publish.yml`: protected manual publisher, not triggered by pushes or pull requests.

- `.github/workflows/mcp-registry-validate.yml`: manual validation using the same publisher, container and CA bundle, with read-only repository permissions and no OIDC login or publication. Run this before retrying protected publication.
