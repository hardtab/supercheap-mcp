# SuperCheap MCP Registry metadata

Public metadata for the proposed `io.github.hardtab/supercheap-shopping` entry, version `0.1.0`.

- Website: https://supercheap.market/
- Remote endpoint: https://supercheap.market/mcp (Streamable HTTP, customer OAuth required)
- Connection guide: https://supercheap.market/us-en/use-supercheap-with-ai/
- Support: https://supercheap.market/support/ · support@supercheap.market

## Status

Metadata and a manual publisher are prepared. The first protected publication run is waiting for human approval. Registry publication and authenticated client acceptance are not yet confirmed. This repository contains no server implementation, customer data, reviewer fixtures or long-lived credentials.

On 1 October 2026, Backend release `2fc707d63d67177f3c8ff9b52ab5012677fa7d57` was deployed and accepted by [main CI](https://github.com/hardtab/supercheap-backend/actions/runs/36806943701). Public readiness returned HTTP 200 with that release and digest `sha256:c3a07b373e71a3e5aefda980b473b395795644dd8f5b11fd788f72b8432c8cd6`; OAuth metadata advertises CIMD support. The exact read-only publisher preflight passed again after acceptance. [Production audit](https://github.com/hardtab/supercheap-backend/actions/runs/36811167290) passed and confirmed the existing 30 September lifecycle aggregate survived container replacement, with valid daily and TTL indexes. [Container checks](https://github.com/hardtab/supercheap-backend/actions/runs/36811153235) also passed; the checkout log confirms exact source `2fc707d63d67177f3c8ff9b52ab5012677fa7d57`. These checks establish runtime and public metadata readiness; authenticated client acceptance remains unverified.

## Protected publication

Environment configuration was verified on 1 October 2026: required human reviewer, exactly the `main` branch allowed, and administrator bypass disabled. [Publication run 36811212516](https://github.com/hardtab/supercheap-mcp/actions/runs/36811212516) was dispatched from exact metadata revision `7caa540794754e83afccb4767207da994d79c42a` and is waiting for human review. The manifest and workflow in this README update remain unchanged. Configuration must be checked again before the exact run is approved.

The workflow runs only by manual dispatch from `main` in this exact repository, with `confirm_publish=true`. Configure the `mcp-registry-publish` environment with a required human reviewer, disable administrator bypass in its settings, and allow exactly the `main` branch. The reviewer must inspect the exact run, manifest and workflow before approval. Automation must never approve or bypass its own deployment. A sole owner may manually approve their own dispatch; independent-review prevention is optional additional protection.

Review changes through pull requests before merging to `main`. The GitHub OIDC publisher permission covers `io.github.hardtab/*`, so the exact repository, branch, manifest and approval controls are significant.

The hosted runner checks the environment and public customer-only OAuth/readiness boundary before requesting a short-lived Registry identity. The official Registry publisher is checksum-pinned; its runtime image is digest-pinned. Public artifacts are mounted read-only; CLI credentials exist only in root-owned tmpfs inside a disposable container. No publisher token, PAT or signing key belongs in this repository.

After publication, the workflow verifies the final official HTTPS Registry origin/version path and the exact declared remote set, title and website. That lookup proves listing publication only. Verify OAuth, buyer tools, refresh and revocation independently in each supported client before claiming client acceptance.

## Files

- `server.json`: proposed public Registry manifest.
- `.github/workflows/mcp-registry-publish.yml`: protected manual publisher, not triggered by pushes or pull requests.
