# AI Distribution Plan: SuperCheap MCP

Цель: сделать SuperCheap доступным для AI-ассистентов (ChatGPT, Claude, Copilot,
Codex и др.) через все основные MCP-директории и каналы обнаружения, чтобы
пользователям было проще найти SuperCheap и начать с ним работать.

---

## 1. Состояние на 3 октября 2026

| Канал | Статус | Детали |
|---|---|---|
| **Official MCP Registry** | ✅ Published | `io.github.hardtab/supercheap-shopping`, версия 0.1.0, Streamable HTTP. [Ссылка](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.hardtab%2Fsupercheap-shopping/versions/0.1.0) |
| **Smithery** | ✅ Listed | [hardtab/supercheap-shopping](https://smithery.ai/servers/hardtab/supercheap-shopping). 33 tools, authenticated scan OK. |
| **Glama** | ✅ Listed | [io.github.hardtab/supercheap-shopping](https://glama.ai/mcp/connectors/io.github.hardtab/supercheap-shopping). Healthy, 33 tools. |
| **Arcade.dev** | 🔲 Pending | Директория Arcade.dev — целевой канал для добавления. |
| **OpenAI ChatGPT Plugin Directory** | 🔲 Pending | Нужна публикация через OpenAI Developer Platform. |
| **Claude / Anthropic MCP Directory** | 🔲 Pending | Ожидается появление публичного каталога MCP-серверов. |
| **Agentic Commerce Feeds** | 🔲 Pending | Amazon, Google Shopping, другие AI-шопинг-фиды. |

---

## 2. Каналы дистрибуции — детально

### 2.1 Official MCP Registry

**Статус:** ✅ Опубликовано

**URL:** https://registry.modelcontextprotocol.io/v0.1/servers/io.github.hardtab%2Fsupercheap-shopping/versions/0.1.0

**Репозиторий:** hardtab/supercheap-mcp

**Как публиковать:** Только через manual dispatch в GitHub Actions из ветки `main`
репозитория `hardtab/supercheap-mcp`. Требуется human reviewer (protected
environment `mcp-registry-publish`).

**Ссылки:**
- [Репозиторий](https://github.com/hardtab/supercheap-mcp)
- [Workflow публикации](https://github.com/hardtab/supercheap-mcp/actions/workflows/publish.yml)
- [Environment secrets](https://github.com/hardtab/supercheap-mcp/settings/environments/mcp-registry-publish)

**Что надо для публикации новой версии:**
1. Обновить `server.json` (version, description при необходимости)
2. Переключиться на `main`, запушить
3. Перейти в Actions → `Publish SuperCheap to Official MCP Registry` → Run workflow
4. Дождаться human approval в Review deployments

---

### 2.2 Smithery

**Статус:** ✅ Зарегистрировано

**URL:** https://smithery.ai/servers/hardtab/supercheap-shopping

**Аккаунт:** GitHub bleshik. Smithery использует GitHub OAuth для входа.

**Ссылки:**
- [Карточка сервера](https://smithery.ai/servers/hardtab/supercheap-shopping)
- [Dashboard админа](https://smithery.ai/dashboard) (нужен вход)

**Процесс регистрации:**
1. Зайти на smithery.ai через GitHub (аккаунт bleshik)
2. Добавить новый MCP-сервер: URL `https://supercheap.market/mcp`
3. Указать namespace (используется `hardtab/supercheap-shopping`)
4. Smithery сам сканирует сервер и обнаруживает инструменты

**Обновление:** Автоматическое — Smithery периодически пересканирует сервер.
Если инструменты меняются, обновление происходит само.

---

### 2.3 Glama

**Статус:** ✅ Зарегистрировано, есть известная проблема

**URL:** https://glama.ai/mcp/connectors/io.github.hardtab/supercheap-shopping

**Аккаунт:** GitHub bleshik. Glama использует GitHub OAuth.

**Ссылки:**
- [Карточка коннектора](https://glama.ai/mcp/connectors/io.github.hardtab/supercheap-shopping)
- [Dashboard админа](https://glama.ai/dashboard) (нужен вход)

**Известные проблемы:**
1. ~~Glama не может найти OAuth metadata endpoint — **FIXED**~~ (добавлены alias-пути)
2. `invalid_scope` при OAuth-авторизации — **не исправлено.** Glama (и другие MCP-инспекторы) запрашивает `offline_access` при получении токена. Сервер не включает `offline_access` в разрешённые scope. Нужно либо:
   - Добавить `offline_access` в `CUSTOMER_MCP_SCOPES` и `STAFF_MCP_SCOPES` (безопасно — это no-op scope)
   - Либо настроить игнорирование неизвестных scope

**Процесс регистрации:**
1. Зайти на glama.ai через GitHub (аккаунт bleshik)
2. Добавить новый MCP-коннектор
3. Указать Remote MCP URL — `https://supercheap.market/mcp`
4. Привязать GitHub-репозиторий `hardtab/supercheap-mcp` для ownership

---

### 2.4 Arcade.dev

**Статус:** 🔲 Запланировано

**URL:** https://arcade.dev

**Аккаунт:** Пока не создан. GitHub OAuth или email.

**Ссылки:**
- [Главная](https://arcade.dev)
- [Документация по добавлению](https://arcade.dev/docs) (проверить раздел MCP)

**Действия:**
1. Создать аккаунт на arcade.dev (рекомендуется через GitHub bleshik)
2. Найти раздел добавления MCP-сервера
3. Добавить SuperCheap MCP:
   - Name: `io.github.hardtab/supercheap-shopping`
   - URL: `https://supercheap.market/mcp`
   - Description: копия из `server.json`
4. Проверить, что Arcade сканирует сервер и видит все 33 инструмента

---

### 2.5 OpenAI ChatGPT Plugin Directory

**Статус:** 🔲 Запланировано

**URL:** https://developers.openai.com/docs/plugins

**Ссылки:**
- [Документация по плагинам](https://developers.openai.com/docs/plugins)
- [Submit plugins — OpenAI Developers](https://platform.openai.com/plugins)
- [Plugin review guidelines](https://platform.openai.com/docs/plugins/review)

**Что нужно сделать:**
1. Подготовить ChatGPT plugin manifest:
   - Публичный endpoint: `https://supercheap.market/openai-plugin.json`
   - Manifest с description для AI, supported tools, auth type (OAuth)
2. Зарегистрироваться на platform.openai.com
3. Пройти review process (ручное модерация OpenAI)
4. После одобрения плагин становится доступен в ChatGPT через Plugin Discovery

**Важно:** ChatGPT plugin discovery — один из самых мощных каналов (судя по
данным Tibo, обнаруживаемость плагинов ведёт к массовому adoption).

**Статус подачи:** Не начато. Нужен первичный манифест.

---

### 2.6 Claude / Anthropic MCP Directory

**Статус:** 🔲 Ожидание

На данный момент у Anthropic нет публичного каталога MCP-серверов, аналогичного
MCP Registry или Smithery. Есть:
- Примеры в [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) репозитории — можно предложить PR
- Рекомендации в документации Claude

Возможные действия:
1. Следить за [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — можно добавить SuperCheap в список сторонних серверов
2. Когда Anthropic запустит официальный каталог — подать заявку

---

### 2.7 Agentic Commerce Feeds

**Статус:** 🔲 Запланировано к исследованию

Помимо MCP-директорий, AI-ассистенты могут находить товары через:
- **Google Shopping / Merchant Center** — AI-модели Google (Gemini, Search Generative Experience) используют фид товаров для ответов
- **Amazon Product Advertising API** — для Alexa и других AI
- **PriceGrabber / Shopping.com API** — некоторые AI умеют ходить в сравнение цен

Для SuperCheap это не основной канал (мы сами — площадка), но стоит иметь
в виду для расширения.

---

## 3. Аккаунты и доступы

| Площадка | Аккаунт | Способ входа | Примечание |
|---|---|---|---|
| **Official MCP Registry** | GitHub hardtab | GitHub Actions OIDC (ID token) | Опубликовано. Environment `mcp-registry-publish` в hardtab/supercheap-mcp |
| **Smithery** | GitHub bleshik | GitHub OAuth | Зарегистрировано. Вход через smithery.ai |
| **Glama** | GitHub bleshik | GitHub OAuth | Зарегистрировано. Вход через glama.ai |
| **Arcade.dev** | GitHub bleshik | GitHub OAuth (предположительно) | Не создан. Нужно зарегистрироваться |
| **OpenAI Platform** | hardtab LLC account | Email + пароль | Не создан для плагинов. Использовать корпоративный email |
| **GitHub (все площадки)** | bleshik | Personal access token | PAT с нужными scope лежит в secrets GitHub |
| **MCP Registry CLI** | Registry OIDC | OIDC через GitHub Actions | Используется в publish workflow. Не требует ручного токена |

**Где хранятся credentials:**
- GitHub Secrets: `Settings → Secrets and variables → Actions` в каждом репозитории
- MCP Registry environment: `Settings → Environments → mcp-registry-publish`
- Для OpenAI потребуется отдельный аккаунт разработчика и API key

---

## 4. Технические детали

### MCP Endpoint
- **URL:** `https://supercheap.market/mcp`
- **Протокол:** Streamable HTTP
- **Аутентификация:** OAuth 2.0 (Authorization Code + PKCE)
- **Требуемый scope по умолчанию:** `catalog:read`
- **Количество инструментов:** 33 (на 3 октября 2026)

### OAuth
- **Authorization endpoint:** `https://supercheap.market/mcp/oauth/authorize`
- **Token endpoint:** `https://supercheap.market/mcp/oauth/token`
- **Metadata:** `https://supercheap.market/.well-known/oauth-protected-resource`
- **Grant types:** `authorization_code`, `refresh_token`
- **Стандартно запрашиваемые scopes:** `catalog:read cart:read cart:write checkout:read checkout:write profile:read profile:write`

### Публичный статус
- **Сайт:** https://supercheap.market/
- **AI guide:** https://supercheap.market/us-en/use-supercheap-with-ai/
- **Репозиторий MCP metadata:** https://github.com/hardtab/supercheap-mcp
- **Backend repo:** https://github.com/hardtab/supercheap-backend

---

## 5. Очередь работ (priority)

### P0 — Исправить проблемы, блокирующие работу
- [ ] Добавить `offline_access` в allowlist scopes (supercheap-backend: `mcp-access-token.ts`)
- [ ] Дождаться CI по PR #26 (glama discovery fix), вмержить и задеплоить
- [ ] Проверить, что Glama OAuth работает после обоих фиксов

### P1 — Расширить присутствие в директориях
- [ ] **Arcade.dev** — зарегистрироваться и добавить карточку
- [ ] **OpenAI ChatGPT Plugin Directory** — подготовить манифест и подать

### P2 — Улучшить обнаруживаемость
- [ ] **modelcontextprotocol/servers** — PR со списком сторонних серверов
- [ ] **SuperCheap MCP Version 0.2.0** — добавить больше инструментов, если нужно

---

## 6. Метрики и мониторинг

Что проверять регулярно:
1. **Health endpoint:** `curl -sI https://supercheap.market/mcp` — должен быть 200
2. **Инструменты доступны:** Smithery/Glama показывают 33+ tools
3. **OAuth flow:** Полный цикл авторизации в любом MCP-клиенте
4. **Registry listing:** Статус `active` и `isLatest=true`

---

## 7. Nord Stream / Дополнительные каналы

Потенциальные площадки для будущего расширения:
- [**Toolbase**](https://toolbase.io) — каталог MCP
- [**MCP.so**](https://mcp.so) — ещё один агрегатор MCP-серверов
- [**OpenTools**](https://opentools.ai) — AI plugin directory
- [**Composio**](https://composio.dev) — интеграционная платформа с поддержкой MCP
- [**n8n**](https://n8n.io) — workflow automation, поддерживает MCP-ноды
- **Zapier AI Actions** — другое направление discovery для AI

---

*Документ создан 3 октября 2026. Регулярно обновляйте статусы и ссылки.*
