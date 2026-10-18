# Agent instructions

## Shared CI agreements

The authoritative HARD TAB CI agreement is [agent-ops/docs/ci-agreements.md](https://github.com/hardtab/agent-ops/blob/main/docs/ci-agreements.md).
Before changing workflows, CI scripts/actions, runner routing, GitHub variables,
labels/groups, runner services, hooks, Docker settings, or quality gates, read
its current `main` version. With authenticated GitHub CLI:

```sh
gh api 'repos/hardtab/agent-ops/contents/docs/ci-agreements.md?ref=main' --jq .content | base64 --decode
```

Product work does not
implicitly authorize CI/infrastructure changes. Report infrastructure failures
with evidence; preserve the shared Linux/Mac pool, Docker eligibility and
production trust boundaries. Do not introduce GitHub-hosted runners or Actions
Cache/Artifact Storage. Do not bypass failing checks by lowering quality gates.
If the document cannot be read, keep existing CI settings and report that limit.
Explicit user instructions govern the authorized task; read the agreement for
its full scope, current exceptions, and change procedure.
