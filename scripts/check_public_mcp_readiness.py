"""Fail-closed production preflight for the public SuperCheap catalog MCP."""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.parse
import urllib.request


BASE = "https://supercheap.market"
ALLOWED_HOSTS = {"supercheap.market", "api.supercheap.market"}
EXPECTED_RESOURCE = "https://supercheap.market/api/v1/mcp"
EXPECTED_AUTHORIZATION_SERVER = "https://supercheap.market"
EXPECTED_CUSTOMER_SCOPES = [
    "catalog:read",
    "cart:read",
    "cart:write",
    "checkout:read",
    "checkout:write",
    "orders:read",
    "orders:write",
    "profile:read",
    "profile:write",
    "support:read",
    "support:write",
]
EXPECTED_STAFF_SCOPES = [
    "staff:support:read",
    "staff:support:write",
    "staff:bonus-program:read",
    "staff:bonus-program:write",
    "staff:orders:read",
    "staff:orders:write",
    "staff:customers:read",
    "staff:audit:read",
    "staff:catalog:write",
    "staff:configuration:read",
    "staff:configuration:write",
    "staff:taxonomy:read",
    "staff:taxonomy:write",
    "staff:influencers:read",
    "staff:influencers:write",
    "staff:influencers:orders:read",
    "staff:influencers:balance-gifts:write",
    "staff:influencers:discovery:read",
    "staff:influencers:discovery:write",
    "staff:influencers:review:read",
    "staff:influencers:review:write",
    "staff:influencers:finance:read",
    "staff:influencers:finance:write",
    "staff:influencers:finance:correct",
    "staff:influencers:outreach:read",
    "staff:influencers:outreach:write",
]

PUBLIC_CATALOG_TOOLS = {
    "market_list",
    "category_search",
    "category_get_tree",
    "catalog_search_products",
    "catalog_get_product",
    "catalog_get_similar_products",
    "catalog_report_product_impressions",
}
ANONYMOUS_CATALOG_TOOLS = PUBLIC_CATALOG_TOOLS - {"catalog_report_product_impressions"}
MCP_PROTOCOL_VERSION = "2025-11-25"
USER_AGENT = "SuperCheap-Registry-Preflight/1.0"


def request(url: str, expected_status: int, *, method: str = "GET", body: bytes | None = None,
            headers: dict[str, str] | None = None) -> tuple[bytes, object]:
    request_headers = {"Accept": "application/json", "User-Agent": USER_AGENT}
    if headers:
        request_headers.update(headers)
    http_request = urllib.request.Request(url, data=body, method=method, headers=request_headers)
    try:
        response = urllib.request.urlopen(http_request, timeout=20)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        if response.status != expected_status:
            raise RuntimeError(
                f"Unexpected HTTP {response.status} for {urllib.parse.urlsplit(url).path}; "
                f"expected {expected_status}"
            )
        final = urllib.parse.urlsplit(response.geturl())
        if final.scheme != "https" or final.hostname not in ALLOWED_HOSTS:
            raise RuntimeError("A public SuperCheap endpoint redirected outside the approved HTTPS hosts")
        return response.read(1_000_000), response.headers


def json_get(url: str) -> dict[str, object]:
    body, _ = request(url, 200)
    try:
        value = json.loads(body)
    except json.JSONDecodeError as error:
        raise RuntimeError("A public metadata endpoint did not return JSON") from error
    if not isinstance(value, dict):
        raise RuntimeError("A public metadata endpoint returned an unexpected JSON value")
    return value


def require_exact_scopes(metadata: dict[str, object], expected: list[str], description: str) -> None:
    scopes = metadata.get("scopes_supported")
    if not isinstance(scopes, list) or any(not isinstance(scope, str) for scope in scopes):
        raise RuntimeError(f"{description} did not provide a string scope list")
    if len(scopes) != len(set(scopes)) or sorted(scopes) != sorted(expected):
        raise RuntimeError(f"{description} did not advertise the expected scopes exactly once")


def parse_mcp_response(body: bytes, content_type: str) -> dict[str, object]:
    media_type = content_type.split(";", 1)[0].strip().lower()
    if media_type == "application/json":
        try:
            value = json.loads(body)
        except json.JSONDecodeError as error:
            raise RuntimeError("The MCP endpoint returned invalid JSON") from error
    elif media_type == "text/event-stream":
        events = []
        for line in body.decode("utf-8").splitlines():
            if line.startswith("data:"):
                try:
                    events.append(json.loads(line[5:].lstrip()))
                except json.JSONDecodeError as error:
                    raise RuntimeError("The MCP endpoint returned invalid JSON in an SSE event") from error
        if len(events) != 1:
            raise RuntimeError("The MCP endpoint did not return exactly one JSON-RPC response event")
        value = events[0]
    else:
        raise RuntimeError(f"The MCP endpoint returned unexpected content type {content_type!r}")
    if not isinstance(value, dict):
        raise RuntimeError("The MCP endpoint returned an unexpected JSON-RPC value")
    return value


def mcp_post(
    url: str,
    payload: dict[str, object],
    expected_status: int,
    *,
    allow_jsonrpc_error: bool = False,
) -> dict[str, object] | None:
    body, headers = request(
        url,
        expected_status,
        method="POST",
        body=json.dumps(payload, separators=(",", ":")).encode("utf-8"),
        headers={
            "Accept": "application/json, text/event-stream",
            "Content-Type": "application/json",
            "MCP-Protocol-Version": MCP_PROTOCOL_VERSION,
        },
    )
    if expected_status == 202:
        if body:
            raise RuntimeError("The MCP initialized notification unexpectedly returned a body")
        return None
    value = parse_mcp_response(body, headers.get("Content-Type", ""))
    if (
        value.get("jsonrpc") != "2.0"
        or value.get("id") != payload.get("id")
        or ("error" in value and not allow_jsonrpc_error)
    ):
        raise RuntimeError(f"The MCP endpoint returned an unexpected response for {payload.get('method')}")
    return value


def security_schemes(tool: dict[str, object]) -> list[tuple[str, tuple[str, ...]]]:
    metadata = tool.get("_meta")
    schemes = metadata.get("securitySchemes") if isinstance(metadata, dict) else None
    if not isinstance(schemes, list):
        raise RuntimeError(f"MCP tool {tool.get('name')!r} omitted security schemes")
    normalized = []
    for scheme in schemes:
        if not isinstance(scheme, dict):
            raise RuntimeError(f"MCP tool {tool.get('name')!r} has an invalid security scheme")
        if scheme == {"type": "noauth"}:
            normalized.append(("noauth", ()))
            continue
        scopes = scheme.get("scopes")
        if scheme.get("type") != "oauth2" or not isinstance(scopes, list) or any(
            not isinstance(scope, str) for scope in scopes
        ):
            raise RuntimeError(f"MCP tool {tool.get('name')!r} has an unexpected security scheme")
        normalized.append(("oauth2", tuple(sorted(scopes))))
    if len(normalized) != len(set(normalized)):
        raise RuntimeError(f"MCP tool {tool.get('name')!r} repeats a security scheme")
    return sorted(normalized)


def check_public_mcp_alias(path: str) -> None:
    endpoint = f"{BASE}{path}"
    initialize = mcp_post(
        endpoint,
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": MCP_PROTOCOL_VERSION,
                "capabilities": {},
                "clientInfo": {"name": "Registry-preflight", "version": "1"},
            },
        },
        200,
    )
    result = initialize.get("result") if initialize else None
    if not isinstance(result, dict) or result.get("protocolVersion") != MCP_PROTOCOL_VERSION:
        raise RuntimeError(f"Unauthenticated initialize at {path} did not negotiate the expected MCP version")

    mcp_post(endpoint, {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}, 202)
    listed = mcp_post(
        endpoint,
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
        200,
    )
    tools_result = listed.get("result") if listed else None
    tools = tools_result.get("tools") if isinstance(tools_result, dict) else None
    if not isinstance(tools, list) or any(not isinstance(tool, dict) for tool in tools):
        raise RuntimeError(f"Unauthenticated tools/list at {path} returned an invalid tool list")
    names = [tool.get("name") for tool in tools]
    if any(not isinstance(name, str) for name in names) or len(names) != len(set(names)):
        raise RuntimeError(f"Unauthenticated tools/list at {path} returned missing or duplicate tool names")
    if set(names) != PUBLIC_CATALOG_TOOLS:
        raise RuntimeError(
            f"Unauthenticated MCP tools at {path} differed from the public catalog allowlist: "
            f"{sorted(names)!r}"
        )

    for tool in tools:
        name = tool["name"]
        expected = [("oauth2", ("catalog:read",))]
        if name in ANONYMOUS_CATALOG_TOOLS:
            expected = sorted([("noauth", ()), *expected])
        if security_schemes(tool) != expected:
            raise RuntimeError(f"MCP tool {name!r} at {path} advertised an unexpected security boundary")

    # The current payment-link schema requires confirmationId, confirmed=true, and
    # idempotencyKey. Empty arguments cannot create a checkout, even if the tool is
    # accidentally registered but omitted from tools/list; the exact allowlist above
    # also fails before this probe if the writer is advertised.
    write_probe = mcp_post(
        endpoint,
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {"name": "checkout_create_payment_link", "arguments": {}},
        },
        200,
        allow_jsonrpc_error=True,
    )
    error = write_probe.get("error") if write_probe else None
    if not isinstance(error, dict) or error.get("code") != -32602 or error.get("message") != (
        "Tool checkout_create_payment_link not found"
    ):
        raise RuntimeError(f"Unauthenticated payment-link write probe at {path} was not rejected as unavailable")


def check_live_readiness() -> None:
    ready = json_get(f"{BASE}/api/v1/health/ready")
    if ready.get("status") != "ok":
        raise RuntimeError("SuperCheap production readiness is not ok")

    protected = json_get(f"{BASE}/.well-known/oauth-protected-resource/api/v1/mcp")
    require_exact_scopes(protected, EXPECTED_CUSTOMER_SCOPES, "Customer protected-resource metadata")
    if protected.get("resource") != EXPECTED_RESOURCE:
        raise RuntimeError("Customer protected-resource metadata described an unexpected MCP resource")
    if protected.get("authorization_servers") != [EXPECTED_AUTHORIZATION_SERVER]:
        raise RuntimeError("Customer protected-resource metadata advertised an unexpected authorization server")

    staff_protected = json_get(
        f"{EXPECTED_AUTHORIZATION_SERVER}/.well-known/oauth-protected-resource/api/v1/mcp/staff"
    )
    require_exact_scopes(staff_protected, EXPECTED_STAFF_SCOPES, "Staff protected-resource metadata")
    if staff_protected.get("authorization_servers") != [EXPECTED_AUTHORIZATION_SERVER]:
        raise RuntimeError("Staff protected-resource metadata did not use the shared authorization server")
    if staff_protected.get("resource") != f"{EXPECTED_AUTHORIZATION_SERVER}/api/v1/mcp/staff":
        raise RuntimeError("Staff protected-resource metadata described an unexpected resource")

    authorization = json_get(f"{EXPECTED_AUTHORIZATION_SERVER}/.well-known/oauth-authorization-server")
    require_exact_scopes(
        authorization,
        EXPECTED_CUSTOMER_SCOPES + EXPECTED_STAFF_SCOPES,
        "Shared authorization-server metadata",
    )
    if not {"authorization_code", "refresh_token"}.issubset(
        set(authorization.get("grant_types_supported", []))
    ):
        raise RuntimeError("Authorization-server metadata omitted a supported customer OAuth grant")
    if "S256" not in authorization.get("code_challenge_methods_supported", []):
        raise RuntimeError("Authorization-server metadata omitted PKCE S256")

    check_public_mcp_alias("/mcp")
    check_public_mcp_alias("/api/v1/mcp")
    print(
        "Live readiness and OAuth metadata passed. Both MCP aliases expose only the "
        "six approved anonymous catalog readers plus OAuth-gated product impressions; "
        "no cart, checkout, or order writer is exposed anonymously."
    )


if __name__ == "__main__":
    try:
        check_live_readiness()
    except Exception as error:  # noqa: BLE001 - print a concise, fail-closed workflow error
        print(f"::error::{error}", file=sys.stderr)
        raise SystemExit(1) from error
