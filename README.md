# SuperCheap MCP Registry metadata

Public metadata for the published `io.github.hardtab/supercheap-shopping` entry, version `0.1.0`.

- Website: https://supercheap.market/
- Remote endpoint: https://supercheap.market/mcp (Streamable HTTP, customer OAuth required)
- Connection guide: https://supercheap.market/us-en/use-supercheap-with-ai/
- Support: https://supercheap.market/support/ · support@supercheap.market

## Status

Version `0.1.0` is published in the [Official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.hardtab%2Fsupercheap-shopping/versions/0.1.0). A direct lookup on 8 October 2026 returned the exact namespace and version with `status=active`, `isLatest=true`, and the Streamable HTTP endpoint `https://supercheap.market/mcp`. This repository contains public Registry metadata and publisher workflows; it contains no server implementation, customer data, reviewer fixtures or long-lived credentials.

## Backend release evidence — 8 October 2026

[Fast release 37712311854](https://github.com/hardtab/supercheap-backend/actions/runs/37712311854) recorded backend acceptance for source `9427574c653d8939101cac7ac3ed6146b5e9a0eb` and image `sha256:5c8c55f13e8da037ee63d0a2ab74470e98359f4bccc13da54388ab094609f365`. The long `quality` and Yandex watcher checks were skipped, so this is not a full-CI pass. A later public readiness request timed out; this dated acceptance record does not establish current runtime health or availability.

## Directory listings and client evidence — 8 October 2026

- [Official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.hardtab%2Fsupercheap-shopping/versions/0.1.0) — version `0.1.0`, `active` and `isLatest` on the 8 October direct lookup.
- [mcpservers.org](https://mcpservers.org/servers/hardtab/supercheap-mcp) — public SuperCheap card with the customer OAuth endpoint and Registry metadata.
- [Smithery](https://smithery.ai/servers/hardtab/supercheap-shopping) — its 7 October authenticated scan succeeded and the listing reports 35 tools. This verifies tool discovery, not the full buyer checkout.
- [Glama](https://glama.ai/mcp/connectors/io.github.hardtab/supercheap-shopping) — the public listing reports 35 tools. In an Inspector test on 8 October, a selected-line quote and `checkout_prepare_payment` succeeded while an unselected cart line remained. No order, Stripe payment link or charge was created. A later Test Profile check at 18:06:29 failed with `OAuth access token has expired`; a refresh-token exchange and a current authenticated SuperCheap Inspector connection are not confirmed.
- [MCPI](https://mcpi.app/servers/supercheap) — the public card received a 35-tool customer metadata snapshot on 8 October. The temporary publication key was revoked. The snapshot is metadata publication, not buyer acceptance.

Glama's successful Inspector actions establish only the selected-line quote and payment-preparation behavior for that test. They do not establish current OAuth connectivity, refresh, order creation, or Stripe payment-link creation.

## Other directory intake — 8 October 2026

- MCP Market: the existing repository-mode submission receipt confirmed entry into its free queue, but the [public search](https://mcpmarket.com/search?q=SuperCheap) currently has no exact SuperCheap card. Queue position/status has not been independently read since submission. Its current GitHub-repository submission page offers a $0 Free Queue (average 4–6 weeks) and a $29 one-time expedited option. An earlier 7 October observation recorded $69 for the separate Remote MCP mode; that mode was not selected in the 8 October recheck, so its current price is unconfirmed. No payment was made or approved.
- PulseMCP: the [public search](https://www.pulsemcp.com/servers?q=supercheap) returns no results and says submissions and listing changes are paused. No import of this Registry entry is confirmed.
- Arcade: an Early Access interest survey was acknowledged; no beta acceptance or public Arcade listing is confirmed.

## Protected publication

Environment configuration was verified on 1 October 2026: required human reviewer, exactly the `main` branch allowed, and administrator bypass disabled. [Publication run 36811212516](https://github.com/hardtab/supercheap-mcp/actions/runs/36811212516) used exact metadata revision `7caa540794754e83afccb4767207da994d79c42a`; after manual approval, it failed at CLI manifest validation before requesting an OIDC identity because the pinned container lacked trusted system CA roots for Registry TLS. The workflow update binds only the GitHub-hosted runner's trusted system CA bundle read-only into the pinned container and sets `SSL_CERT_FILE`. The [validation-only run 36818178152](https://github.com/hardtab/supercheap-mcp/actions/runs/36818178152) passed on the repaired revision. The subsequent protected publication run 36818380344 succeeded after human review. The earlier failed run did not publish a listing.

The workflow runs only by manual dispatch from `main` in this exact repository on the self-hosted `hardtab-docker-ci` runner pool. `operation` defaults to `validate`, which does not receive OIDC permission or publisher credentials. Publication requires selecting `operation=publish`, setting `confirm_publish=true`, and approval by the protected `mcp-registry-publish` environment. Before each dispatch, verify that the environment still requires a human reviewer, allows exactly the `main` branch, and has administrator bypass disabled. The reviewer must inspect that exact run, manifest and workflow before approval. Automation must never approve or bypass its own deployment. A sole owner may manually approve their own dispatch; independent-review prevention is optional additional protection.

Review changes through pull requests before merging to `main`. The GitHub OIDC publisher permission covers `io.github.hardtab/*`, so the exact repository, branch, manifest and approval controls are significant.

The self-hosted runner checks the environment and public customer-only OAuth/readiness boundary before requesting a short-lived Registry identity. The official Registry publisher is checksum-pinned; its runtime image is digest-pinned and runs as `linux/amd64`. Public artifacts and the runner's trusted system CA bundle are mounted read-only; the workflow stops before OIDC login if the bundle is missing, unreadable, or empty. CLI credentials exist only in root-owned tmpfs inside a disposable container. No publisher token, PAT or signing key belongs in this repository.

After publication, the workflow verifies the final official HTTPS Registry origin/version path and the exact declared remote set, title and website. That lookup proves listing publication only. Verify OAuth, buyer tools, refresh and revocation independently in each supported client before claiming client acceptance.

## Files

- `server.json`: published public Registry manifest.
- `.github/workflows/registry-operations.yml`: one manual workflow. Choose `validate` (the default) for unauthenticated validation, or choose `publish` and confirm explicitly to request reviewer-gated publication.
