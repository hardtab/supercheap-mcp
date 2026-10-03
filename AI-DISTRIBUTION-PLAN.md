# AI Distribution Plan: SuperCheap MCP

Date: 2026-10-03

Goal: Make SuperCheap discoverable in AI assistants (ChatGPT, Claude, Copilot, Codex, etc.) through MCP directories, plugin ecosystems, and AI discovery platforms.

---

## 1. Current status (3 October 2026)

| Channel | Status | Details |
|---|---|---|
| **Official MCP Registry** | ✅ Published | `io.github.hardtab/supercheap-shopping`, v0.1.0, Streamable HTTP |
| **Smithery** | ✅ Listed | hardtab/supercheap-shopping, 33 tools |
| **Glama** | ✅ Listed | io.github.hardtab/supercheap-shopping (OAuth fixed) |
| **mcpi.app** | ✅ Listed | supercheap listing active |
| **Arcade.dev** | 🔲 Pending | Register and add server |
| **OpenAI ChatGPT Plugin Directory** | 🔲 Pending | Prepare manifest, submit for review |
| **Claude / Anthropic MCP Directory** | 🔲 Waiting | No public directory yet |
| **Agentic Commerce Feeds** | 🔲 Research | Google Merchant Center, etc. |

---

## 2. Distribution channels — detailed

### 2.1 Official MCP Registry

**Status:** ✅ Published

**URL:** https://registry.modelcontextprotocol.io/v0.1/servers/io.github.hardtab%2Fsupercheap-shopping/versions/0.1.0

**Repository:** hardtab/supercheap-mcp

**Publishing a new version:**
1. Update `server.json` (version, description if needed)
2. Push to `main`
3. GitHub Actions → `Publish SuperCheap to Official MCP Registry` → Run workflow
4. Go to Review deployments → Approve and deploy
5. Wait for confirmed published status

**Protected environment:** `mcp-registry-publish` — human review required.

**Links:**
- [Repository](https://github.com/hardtab/supercheap-mcp)
- [Publish workflow](https://github.com/hardtab/supercheap-mcp/actions/workflows/publish.yml)
- [Environment secrets](https://github.com/hardtab/supercheap-mcp/settings/environments/mcp-registry-publish)

---

### 2.2 Smithery

**Status:** ✅ Registered

**URL:** https://smithery.ai/servers/hardtab/supercheap-shopping

**Login:** https://smithery.ai → Sign in with GitHub (bleshik)

**Dashboard:** https://smithery.ai/dashboard

**Setup:** Add MCP server → URL `https://supercheap.market/mcp` → auto-scanned.

**Updates:** Automatic re-scanning by Smithery.

**Links:**
- [Server card](https://smithery.ai/servers/hardtab/supercheap-shopping)
- [Admin dashboard](https://smithery.ai/dashboard)

---

### 2.3 Glama

**Status:** ✅ Registered, OAuth scope issue fixed

**URL:** https://glama.ai/mcp/connectors/io.github.hardtab/supercheap-shopping

**Login:** https://glama.ai → Sign in with GitHub (bleshik)

**Dashboard:** https://glama.ai/dashboard

**Known issue (resolved):** Glama requests `offline_access` scope during OAuth. The backend now includes `offline_access` in allowed scopes. If you still see `invalid_scope`, the backend deployment may be pending.

**Links:**
- [Connector card](https://glama.ai/mcp/connectors/io.github.hardtab/supercheap-shopping)

---

### 2.4 mcpi.app

**Status:** ✅ Registered

**URL:** https://mcpi.app/servers/supercheap

**Notes:** Public MCP aggregator, no account required.

---

### 2.5 Arcade.dev

**Status:** 🔲 Need to register

**URL:** https://arcade.dev

**To do:**
1. Go to https://arcade.dev → register via GitHub (bleshik)
2. Add MCP server: URL `https://supercheap.market/mcp`
3. Name: `SuperCheap Shopping`
4. Verify tool scanning works

---

### 2.6 OpenAI ChatGPT Plugin Directory

**Status:** 🔲 Planned

According to Tibo (@thsottiaux): "Plugin discovery on ChatGPT leads to massive adoption opportunity. Open ecosystems will win."  
[Source](https://x.com/thsottiaux/status/2105039482013757749)

**Links:**
- [Submit plugins — OpenAI Developers](https://platform.openai.com/plugins)
- [Plugin review guidelines](https://developers.openai.com/docs/plugins/review)

**To do:**
1. Prepare OpenAI plugin manifest → host at `https://supercheap.market/openai-plugin.json`
2. Register at https://platform.openai.com
3. Pass OpenAI moderation/review
4. Plugin becomes available in GPT Store / Plugin Discovery

**Important:** This is a separate format from MCP (OpenAI Plugins API, not MCP).

---

### 2.7 Claude / Anthropic & other AI directories

**Status:** 🔲 Waiting

Anthropic does not have a public MCP server directory yet. Options:
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — submit a PR adding SuperCheap to the community list
- When Anthropic launches an official catalog — submit

Other platforms to monitor:
- **OpenTools** (https://opentools.ai) — AI plugin directory
- **Composio** (https://composio.dev) — integration platform with MCP
- **n8n** (https://n8n.io) — workflow automation with MCP nodes
- **Zapier AI Actions** — AI discovery via Zapier
- **Pipedream** (https://pipedream.com) — MCP integrations
- **Toolbase** (https://toolbase.io) — MCP catalog
- **MCP.so** (https://mcp.so) — MCP aggregator

---

### 2.8 Agentic Commerce Feeds

**Status:** 🔲 Research

Future expansion: Google Merchant Center, Amazon PAAPI, PriceGrabber, etc.

---

## 3. Accounts and access

| Platform | Account | Login method | Notes |
|---|---|---|---|
| **Official MCP Registry** | GitHub hardtab | GitHub Actions OIDC | Published. Protected env `mcp-registry-publish` |
| **Smithery** | bleshik | GitHub OAuth | https://smithery.ai/dashboard |
| **Glama** | bleshik | GitHub OAuth | https://glama.ai/dashboard |
| **mcpi.app** | — | Public | No account needed |
| **Arcade.dev** | bleshik | GitHub OAuth (likely) | Not registered yet |
| **OpenAI Platform** | hardtab LLC | Email + password | Not created yet for plugins |
| **GitHub hardtab org** | bleshik | GitHub OAuth + PAT | Owner of all SuperCheap repos |
| **Cloudflare** | hardtab LLC | Email + 2FA | https://dash.cloudflare.com |

**Where credentials are stored:**
- GitHub Secrets: `Settings → Secrets and variables → Actions` in each repo
- MCP Registry environment: `Settings → Environments → mcp-registry-publish`
- Cloudflare API Token: GitHub Actions secrets (separate for web/workers)
- OpenAI: will need separate developer account + API key

---

## 4. Technical details

**MCP Endpoint:** https://supercheap.market/mcp  
**Protocol:** Streamable HTTP  
**Tools:** 33 (as of 3 Oct 2026)  
**Auth:** OAuth 2.0 (Authorization Code + PKCE)  
**Default scope:** `catalog:read`

**OAuth endpoints:**
- Authorize: `https://supercheap.market/mcp/oauth/authorize`
- Token: `https://supercheap.market/mcp/oauth/token`
- Protected resource metadata: `https://supercheap.market/.well-known/oauth-protected-resource`
- Authorization server metadata: `https://supercheap.market/.well-known/oauth-authorization-server`

**Scopes:** `catalog:read cart:read cart:write checkout:read checkout:write profile:read profile:write offline_access`

**Public resources:**
- Site: https://supercheap.market/
- AI guide: https://supercheap.market/us-en/use-supercheap-with-ai/
- LLMs.txt: https://supercheap.market/llms.txt
- LLMs-full: https://supercheap.market/llms-full.txt
- MCP metadata repo: https://github.com/hardtab/supercheap-mcp
- Web frontend: https://github.com/hardtab/supercheap-web
- Backend AI: https://github.com/hardtab/supercheap-backend-ai-integration

**Linked directories on the AI page:**
The page at https://supercheap.market/us-en/use-supercheap-with-ai/ links to:
- [MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.hardtab%2Fsupercheap-shopping/versions/0.1.0)
- [Smithery](https://smithery.ai/servers/hardtab/supercheap-shopping)
- [Glama](https://glama.ai/mcp/connectors/io.github.hardtab/supercheap-shopping)
- [mcpi](https://mcpi.app/servers/supercheap)

---

## 5. Known issues

| Problem | Status | Fix |
|---|---|---|
| Glama OAuth `invalid_scope` | ✅ Fixed | Added `offline_access` to allowlist scopes |
| Smithery card in wrong namespace | ✅ Fixed | Moved to hardtab/supercheap-shopping |
| MCP Registry deploy needs human review | 🔲 Process | Must approve in Review deployments after each publish |

---

## 6. Task queue (priority)

### P0 — Done
- [x] `offline_access` added to MCP scope allowlist
- [x] Glama connector registered and accessible
- [x] Smithery card moved to hardtab/supercheap-shopping
- [x] Public AI page updated with directory links
- [x] MCP Registry published (v0.1.0)

### P1 — Do next
- [ ] **Arcade.dev** — register (https://arcade.dev) and add SuperCheap
- [ ] **OpenAI Plugin Directory** — prepare manifest, submit for moderation

### P2 — Queue
- [ ] **modelcontextprotocol/servers** — PR adding SuperCheap to community list
- [ ] **OpenTools** — check MCP support
- [ ] **Composio** — add integration
- [ ] **n8n** — community node for SuperCheap

### Long-term
- [ ] Google Merchant Center / Shopping feeds for AI shopping
- [ ] Anthropic MCP directory (when available)
- [ ] SuperCheap MCP v0.2.0 — new tools

---

## 7. Architecture notes

- SuperCheap uses **Streamable HTTP** transport, not STDIO. MCP clients must support remote servers.
- OAuth is shared between web and MCP. Same authorization server.
- `offline_access` is a no-op scope (grants no access), but required by Glama and other inspectors.

---

*Document created 3 October 2026.*  
*Last updated: 3 October 2026 — restructured, added issue tracker, architecture notes, updated statuses.*
