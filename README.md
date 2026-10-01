# SuperCheap MCP Registry metadata

Public metadata for the proposed `io.github.hardtab/supercheap-shopping` entry, version `0.1.0`.

- Website: https://supercheap.market/
- Remote endpoint: https://supercheap.market/mcp (Streamable HTTP, customer OAuth required)
- Connection guide: https://supercheap.market/us-en/use-supercheap-with-ai/
- Support: https://supercheap.market/support/ · support@supercheap.market

## Status

Metadata and a manual publisher are prepared. Registry publication and authenticated client acceptance are not yet confirmed. This repository contains no server implementation, customer data, reviewer fixtures or long-lived credentials.

## Protected publication

Environment configuration was verified on 1 October 2026: required human reviewer, exactly the `main` branch allowed, and administrator bypass disabled. Publication has not been dispatched. Configuration must be checked again before the exact run is approved.

The workflow runs only by manual dispatch from `main` in this exact repository, with `confirm_publish=true`. Configure the `mcp-registry-publish` environment with a required human reviewer, disable administrator bypass in its settings, and allow exactly the `main` branch. The reviewer must inspect the exact run, manifest and workflow before approval. Automation must never approve or bypass its own deployment. A sole owner may manually approve their own dispatch; independent-review prevention is optional additional protection.

Review changes through pull requests before merging to `main`. The GitHub OIDC publisher permission covers `io.github.hardtab/*`, so the exact repository, branch, manifest and approval controls are significant.

The hosted runner checks the environment and public customer-only OAuth/readiness boundary before requesting a short-lived Registry identity. The official Registry publisher is checksum-pinned; its runtime image is digest-pinned. Public artifacts are mounted read-only; CLI credentials exist only in root-owned tmpfs inside a disposable container. No publisher token, PAT or signing key belongs in this repository.

After publication, the workflow verifies the final official HTTPS Registry origin/version path and the exact declared remote set, title and website. That lookup proves listing publication only. Verify OAuth, buyer tools, refresh and revocation independently in each supported client before claiming client acceptance.

## Files

- `server.json`: proposed public Registry manifest.
- `.github/workflows/mcp-registry-publish.yml`: protected manual publisher, not triggered by pushes or pull requests.
