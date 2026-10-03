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
| **MCPI** | ✅ Imported | [mcpi.app/servers/supercheap](https://mcpi.app/servers/supercheap). Claim owner pending email verification; карточка не подтверждает ownership. |
| **Arcade.dev** | 🔲 Research | Исследуется возможность партнёрского онбординга. |
| **OpenAI ChatGPT Plugin Directory** | 🔲 Подача готовится | 8 кейсов, видео, ZIP-пакет — публикация через platform.openai.com. |
| **Claude / Anthropic MCP Directory** | 🔲 Pending | Канал существует. Платные планы Claude поддерживают Remote MCP. |
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
2. ~~`invalid_scope` при OAuth-авторизации — **FIXED**~~ (`offline_access` добавлен в allowlist scopes, PR #26 merged & deployed)
3. **OAuth flow — проверена частично:** Authenticated initialize, tools, catalog — ✅ здоров. Cart, checkout, refresh, revoke — ⏳ ещё не проверены.
4. **Dedicated reviewer / client cases** — ⏳ Нужен отдельный тестовый аккаунт с демонстрационными данными; восемь сценариев определены, но их фактическое выполнение ещё не подтверждено.

**Процесс регистрации:**
1. Зайти на glama.ai через GitHub (аккаунт bleshik)
2. Добавить новый MCP-коннектор
3. Указать Remote MCP URL — `https://supercheap.market/mcp`
4. Привязать GitHub-репозиторий `hardtab/supercheap-mcp` для ownership

---

### 2.4 MCPI

**Статус:** ✅ Imported

**URL:** https://mcpi.app/servers/supercheap

**Примечание:** Карточка сервера импортирована. Claim owner — ожидает верификацию email. Наличие карточки само по себе не подтверждает ownership.

**Ссылки:**
- [Карточка на MCPI](https://mcpi.app/servers/supercheap)

---

### 2.5 Arcade.dev

**Статус:** 🔲 Research

**URL:** https://arcade.dev

**Ссылки:**
- [Главная](https://arcade.dev)

**Заметка:** Способ включения SuperCheap в Arcade ещё не подтверждён. Подготовлено направление партнёрского обращения; регистрацию и наличие универсального Add MCP server нельзя считать проверенными.

---

### 2.6 OpenAI ChatGPT Plugin Directory

**Статус:** 🔲 Подача готовится

**URL:** https://developers.openai.com/plugins/deploy/submission
**Submission:** https://platform.openai.com/plugins

**Ссылки:**
- [Официальная документация по публикации](https://developers.openai.com/plugins/deploy/submission) (сверено 3 октября 2026)
- [Submission portal](https://platform.openai.com/plugins)

**Требования OpenAI для публикации:**
1. **Пакет:** ZIP-архив, содержащий `plugin.json` + `mcp.json` + иконку. Подготовлен в backend integrations.
2. **Publisher identity:** Подтверждённая личность разработчика и отдельный аккаунт для dedicated reviewer.
3. **Кейсы для ревью:** 8 реальных пользовательских случаев (5 положительных, 3 отрицательных) + видео, демонстрирующее работу.
4. **Загрузка:** Через портал `https://platform.openai.com/plugins`.
5. **Процесс:** Сначала автоматическое сканирование (проверка пакета), затем ручное ревью, затем отдельная публикация.

**Примечания:**
- Открытый endpoint `openai-plugin.json` не требуется.
- Структура пакета валидирована.

**Статус подачи:** Кейсы (8 шт.) готовятся к загрузке, публикация не произведена. Ожидается завершение подготовки кейсов и видео перед отправкой на ревью.

---

### 2.7 Claude / Anthropic MCP Directory

**Статус:** 🔲 Ожидание выбора аккаунта

**URL:** https://claude.ai/directory/manage/new

**Источник:** https://claude.com/blog/build-plugins-for-claude

Claude Directory существует; портал подачи доступен разработчикам на платных планах Claude. Согласно [официальному объявлению](https://claude.com/blog/build-plugins-for-claude), доступны два пути:
- **Remote MCP Connector** — публичный Streamable HTTP сервер (подходит наш `https://supercheap.market/mcp`)
- **Plugin Bundle** — пакет MCP и skills, размещённый на GitHub; в портал подаётся репозиторий

**Статус подачи:** Не начато. Платный аккаунт для подачи ещё должен выбрать владелец; покупка тарифа не выполнялась. Нужно:
1. Войти на claude.ai/directory/manage/new под аккаунтом с платным планом Claude
2. Подать Remote MCP Connector
3. Дождаться модерации

---

### 2.8 Agentic Commerce Feeds

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
| **MCPI** | — | Email | Карточка импортирована. Owner claim pending email verification. |
| **Arcade.dev** | — | — | Исследуется возможность партнёрского онбординга. |
| **OpenAI Platform** | Издатель HARD TAB LLC — требует проверки | Способ входа выбирает владелец | Подтвердить организацию, verified developer identity и рабочий email перед подачей |
| **GitHub** | bleshik / организация hardtab | Существующий вход в браузере или gh CLI | Не помещать токены в план; Registry использует отдельный Actions OIDC |
| **MCP Registry CLI** | Registry OIDC | OIDC через GitHub Actions | Используется в publish workflow. Не требует ручного токена |

**Где хранятся credentials:**
- GitHub Secrets: `Settings → Secrets and variables → Actions` в каждом репозитории
- MCP Registry environment: `Settings → Environments → mcp-registry-publish`
- Для OpenAI подтвердить нужную организацию и verified developer identity; секреты и reviewer credentials хранить вне публичного пакета

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
- [x] Добавить `offline_access` в allowlist scopes (supercheap-backend: `mcp-access-token.ts`)
- [x] PR #26 merged & deployed — invalid_scope / offline_access fix
- [ ] Получить dedicated reviewer / подготовить клиентские кейсы (8 шт.) для публикации

### P1 — Расширить присутствие в директориях
- [ ] **Arcade.dev** — исследовать возможность партнёрского онбординга
- [ ] **OpenAI ChatGPT Plugin Directory** — завершить кейсы (8 шт.) и подать на ревью

### P2 — Улучшить обнаруживаемость
- [ ] **modelcontextprotocol/servers** — PR со списком сторонних серверов
- [ ] **SuperCheap MCP Version 0.2.0** — добавить больше инструментов, если нужно

---

## 6. Метрики и мониторинг

Что проверять регулярно:
1. **Service readiness:** `curl -s https://supercheap.market/api/v1/health/ready` — должен быть 200 для health check. `curl -i https://supercheap.market/mcp` без Authorization — проверен GET 401 (OAuth challenge).
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
