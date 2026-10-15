# SuperCheap MCP

SuperCheap lets an AI assistant search products for a supported market, review product details and variants, manage a customer cart, quote selected cart lines, and prepare a hosted checkout.

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

No API key is needed. The endpoint uses customer OAuth. Client menus differ; use the connection guide for the current client-specific steps. Review the delivery method and total on SuperCheap before paying.

## Current verification — 15 October 2026

- **Official MCP Registry:** a fresh lookup returned `io.github.hardtab/supercheap-shopping`, version `0.1.0`, with `status=active` and `isLatest=true`. Its declared Streamable HTTP endpoint is `https://supercheap.market/mcp`.
- **Customer tools:** the live Smithery and Glama cards each report 35 tools. Glama currently labels the connector `Healthy` and `Works in Glama`. These are directory discovery and health signals, not proof that a buyer completed checkout through either directory.
- **Smithery customer checkout:** the existing authorized Smithery connection resolved a saved product variant, quoted and prepared only the selected cart line, and created a hosted Stripe checkout link. A read through the same connection confirmed `pending-payment`; both original cart lines remained in the cart. The Stripe-hosted page displayed SuperCheap and the quoted THB total. No payment was made. This verifies the selected-line checkout path through that connection, not a completed purchase or every client lifecycle scenario. Fresh supplier-preview hydration and Glama checkout remain unverified.
- **Other public directories:** [mcpservers.org](https://mcpservers.org/servers/hardtab/supercheap-mcp) has a public card. MCPI has an owner-published 35-tool metadata snapshot dated 8 October; that snapshot is not buyer acceptance. MCP Market acknowledged a free-queue submission, but its public listing was not found in the 8 October search. PulseMCP said on 14 October that submissions and listing changes are paused; no SuperCheap card was found. Arcade acknowledged its Early Access interest form, but beta acceptance and a public Arcade listing are unconfirmed.
- **AI marketplaces:** this repository does not establish OpenAI or Claude publication. No public OpenAI or Claude listing is claimed here.

A Registry record or directory card only helps users find the server. It does not prove that a client authorizes OAuth, completes a shopping flow, or publishes SuperCheap in an AI marketplace.

## Registry publisher workflow

The publisher workflow is manually dispatched from `main`. `validate` is the default and runs without Registry publisher credentials. Publishing requires choosing `operation=publish`, setting `confirm_publish=true`, and passing the protected `mcp-registry-publish` environment review. Before a publish dispatch, verify that the environment still requires a human reviewer, permits only `main`, and has administrator bypass disabled. The reviewer should inspect the exact run, manifest, and workflow before approving it.

The workflow checks the live customer-only OAuth boundary, then uses the official Registry publisher with a short-lived GitHub OIDC identity. It verifies the exact namespace, version, endpoint, title, and website after publication. That check proves Registry publication only; OAuth, shopping, refresh, and revocation need separate verification in each client.

## Files

- `server.json`: public Official MCP Registry manifest.
- `.github/workflows/registry-operations.yml`: manual validation and reviewer-gated publication workflow.
