# SuperCheap MCP

Use the SuperCheap MCP server as an AI shopping assistant. Search products in the selected market, compare SuperCheap product details and variants, manage favorites and a customer cart, and request current delivery and checkout quotes. Public catalog browsing is available without sign-in; customer OAuth protects account-specific actions such as cart and checkout. Products and delivery options depend on the selected market. Review the final amount and complete payment on the hosted Stripe checkout page.

Localized listing descriptions for all 12 supported languages are in [`listing-copy.json`](listing-copy.json). OpenAI's listing package uses the same English and localized copy. The Official MCP Registry manifest supports a single description field, so its public summary uses the concise English version.

This repository contains the public MCP Registry manifest and the protected Registry publisher workflow. The server implementation and customer data are maintained in the SuperCheap backend.

- Website: https://supercheap.market/
- MCP endpoint: https://supercheap.market/mcp
- Connection guide: https://supercheap.market/us-en/use-supercheap-with-ai/
- Support: https://supercheap.market/support/ · support@supercheap.market

## Connect an AI assistant

1. In an AI client that supports remote MCP servers, add a remote server or connector.
2. Select Streamable HTTP if the client asks for a transport, and enter `https://supercheap.market/mcp`.
3. Complete the SuperCheap OAuth sign-in in the browser and approve the customer access requested by the client. Use the SuperCheap customer account you want the assistant to access.
4. Ask the assistant to search for products in a supported market. It can inspect full product details before choosing variants and adding them to the cart.

No API key is needed. Customer OAuth protects account-specific features; catalog browsing is available without signing in. Client menus differ; use the connection guide for the current client-specific steps. Review the delivery method and total on SuperCheap before paying.

## Directory publication and testing snapshots

The directory and client checks below are dated evidence, not a claim that each third-party listing was rescanned today. **Official MCP Registry readback on 14 November 2026:** `io.github.hardtab/supercheap-shopping` version `0.1.1` is active and latest; version `0.1.0` remains active but is no longer latest. [Read version 0.1.1](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.hardtab%2Fsupercheap-shopping/versions/0.1.1). **OpenAI portal readback on 14 November 2026:** version `0.1.2` is Published / Listed publicly. The public ChatGPT listing page still shows the older `0.1.0` listing and short description `Find and compare products`; propagation of the new portal version and subtitle is not yet confirmed. **Claude:** the connector remains publicly listed; an updated English description has been submitted for review, and the old text remains live while that review is pending. **Glama:** the owner updated its description directly and chose to keep it independent of the Registry description. Keep the Registry's concise description and Glama's fuller card text separate.

### Historical client and directory verification — 16 October 2026

- **Official MCP Registry on 16 October:** the lookup returned `io.github.hardtab/supercheap-shopping`, version `0.1.0`, with `status=active` and `isLatest=true` at that time. The 14 November readback shows `0.1.1` as latest. Its declared Streamable HTTP endpoint is `https://supercheap.market/mcp`.
- **Customer tools:** Glama reports 35 tools, `Healthy`, `Works in Glama`, and a 16 October test timestamp. Smithery is publicly marked Published; its displayed deployment timestamp is 7 October, so its cached metadata is not a fresh scan of the latest backend. These are directory discovery and health signals, not proof that a buyer completed checkout through either directory.
- **Smithery customer checkout:** the existing authorized Smithery connection resolved a saved product variant, quoted and prepared only the selected cart line, and created a hosted Stripe checkout link. A read through the same connection confirmed `pending-payment`; both original cart lines remained in the cart. The Stripe-hosted page displayed SuperCheap and the quoted THB total. No payment was made. This verifies the selected-line checkout path through that connection, not a completed purchase or every client lifecycle scenario. Fresh supplier-preview hydration and Glama checkout remain unverified.
- **Other public directories:** [mcpservers.org](https://mcpservers.org/servers/hardtab/supercheap-mcp) has a public card. MCPI displays verified ownership and 35 tools, with a 15 October check; that snapshot is not buyer acceptance. MCP Market acknowledged a free-queue submission, but its public listing was not found in the 8 October search. PulseMCP still states on 16 October that submissions and listing changes are paused; its SuperCheap search returned no card. Arcade acknowledged its Early Access interest form, but beta acceptance and a public Arcade listing are unconfirmed.
- **Claude:** [SuperCheap is publicly listed in the Claude Directory](https://claude.ai/directory/supercheap), published by HARD TAB LLC as a Community connector. The live card was checked on 16 October. Actual Claude product widgets displayed query-matched black hoodie photos and localized product links; when variant data is absent, cards use the main photo without fetching supplier details solely for images. This is not an Anthropic-verified badge or evidence of a completed purchase.
- **OpenAI (historical only):** the portal showed In review / Not published on 16 October. This was superseded by the 14 November Published / Listed publicly readback above.

A Registry record or directory card only helps users find the server. It does not prove that a client authorizes OAuth, completes a shopping flow, or publishes SuperCheap in an AI marketplace.

## Registry publisher workflow

The publisher workflow is manually dispatched from `main`. `validate` is the default and runs without Registry publisher credentials. Publishing requires choosing `operation=publish`, setting `confirm_publish=true`, and passing the protected `mcp-registry-publish` environment review. Before a publish dispatch, verify that the environment still requires a human reviewer, permits only `main`, and has administrator bypass disabled. The reviewer should inspect the exact run, manifest, and workflow before approving it.

The workflow checks the live customer-only OAuth boundary, then uses the official Registry publisher with a short-lived GitHub OIDC identity. It verifies the exact namespace, version, endpoint, title, and website after publication. That check proves Registry publication only; OAuth, shopping, refresh, and revocation need separate verification in each client.

## Files

- `server.json`: public Official MCP Registry manifest.
- `.github/workflows/registry-operations.yml`: manual validation and reviewer-gated publication workflow.
