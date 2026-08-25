# xai-sdk-python — CutNBreak checkout of xAI's official Python SDK; coagent's first-party xAI transport

## METADATA

- FILE := `C:\INFRAGENS_v0.1.0\infragens\001_DIGITAL\000_nlcii\001_substrate_inference\001_core\xai-sdk-python\000_COAGENT.md` — estate overlay for this checkout.
- SCOPE := this repository only — official `xai-sdk` 1.19.0 source plus the INFRAGENS/coagent overlay (this file, estate env alias, git binding).
- ROLE := constitutive-provider SDK checkout. Coagent WIELDS this; this package is not an orchestrator, not a second coagent, and not console-custody authority.
- ASSOC := `..\000_COAGENT.md` (001_core tier — console custody + employed `grok-4.6`) · `..\xai\org_access\org_access_state.md` (live Management API catalog) · `001_DIGITAL\006_web_ops\xai\shared\client\management_client.py` (thin REST key client) · `C:\INFRAGENS_v0.1.0\HANDOVER_GROK-4.6_CUTOVER.md` · `003_PHYSICAL\001_user\001_coagent\coagent\` (wielding NLCII; `providers/xai`, settings `INTERFACE_*`).

## LINEAGE

- Parent chain upward to the fleet root (S.root), hop by hop:
  - `C:\INFRAGENS_v0.1.0\infragens\001_DIGITAL\000_nlcii\001_substrate_inference\001_core\000_COAGENT.md`
  - `C:\INFRAGENS_v0.1.0\infragens\001_DIGITAL\000_nlcii\001_substrate_inference\000_COAGENT.md`
  - `C:\INFRAGENS_v0.1.0\infragens\001_DIGITAL\000_nlcii\000_COAGENT.md`
  - `C:\INFRAGENS_v0.1.0\infragens\001_DIGITAL\000_COAGENT.md`
  - `C:\INFRAGENS_v0.1.0\infragens\000_COAGENT.md`
  - `C:\INFRAGENS_v0.1.0\000_COAGENT.md` — S.root.
- Nested children: none. Vendor `src/xai_sdk/` is the importable package, not an inform-surface tree.

## SUBSTANCE

### What this is

Official xAI Python SDK (`xai-sdk`, Apache-2.0, import `xai_sdk`) forked to `CutNBreak/xai-sdk-python` and seated under `001_core` because it is materiel of the constitutive provider. gRPC client: chat, image, video, files, collections, models, tokenize, batch, auth. Sync `Client` and async `AsyncClient`.

Import name, PyPI identity, and proto bindings stay `xai_sdk`. Do not rename the package to look more INFRAGENS — the name is the vendor interface contract.

### How it sits in INFRAGENS / coagent

- **Wield, do not become.** `s := materiel(coagent)`. Coagent talks to `grok-4.6` through several transports (HTTP Responses, Grok CLI, this gRPC SDK). This tree is the estate-owned first-party SDK so we can patch, pin, and read source without leaving the fleet.
- **Not console-custody authority.** Keys, billing, team ACLs, spend live in `001_core` + `.env` + the REST Management API (`https://management-api.x.ai`). Default reach for that REST surface is python/`httpx` and `management_client.py`. The SDK's `management_api_key` channel is **collections gRPC**, not the REST key/billing catalog.
- **Employment authority** stays `settings.INTERFACE_MODEL` / `INTERFACE_PROVIDER` / `SANDBOX_CONFIGS` and `HANDOVER_GROK-4.6_CUTOVER.md`. Do not flip `INTERFACE_*` from this tree.

### Auth split (hard)

| Name | Host | Role |
|---|---|---|
| `XAI_API_KEY` | `api.x.ai` | inference — required to construct a client |
| `XAI_MANAGEMENT_API_KEY` | `management-api.x.ai` | estate-canonical management token |
| `XAI_MANAGEMENT_KEY` | same | vendor env name; still accepted |
| `XAI_MANAGEMENT_API_BASE_URL` | REST only | used by `httpx` / `ManagementClient`, not this gRPC client |

Resolver in `src/xai_sdk/client.py::management_key_from_env`: estate name first, then vendor name. **Never** substitute `XAI_API_KEY`. A 401/403 on management is the wrong or missing management token.

Load keys from `C:\INFRAGENS_v0.1.0\.env`. Do not print secrets. Do not commit `.env`.

### Git binding (this is the coherence contract)

- **origin** := `https://github.com/CutNBreak/xai-sdk-python` — estate fork; this checkout's push target.
- **upstream** := `https://github.com/xai-org/xai-sdk-python.git` — vendor; fetch/rebase only. Do not push estate commits to xai-org.
- **superproject** := `C:\INFRAGENS_v0.1.0` (`CutNBreak/INFRAGENS_v0.1.0`) registers this path as a **submodule** (mode 160000). Do not copy SDK contents into the monorepo. Do not leave this as an unregistered nested `.git`.
- **order** := children ≺ᵗ superproject — commit here first, then advance the superproject gitlink in a separate commit that stages only the pointer + `.gitmodules` + inform cascade.
- **vendor merge** := `git fetch upstream && git merge upstream/main` (or rebase) on an estate branch when absorbing releases. Keep the overlay (`000_COAGENT.md`, `management_key_from_env`) across merges.

### Boundaries

- No keys, tokens, billing PII, or model weights in this tree.
- No `CLAUDE.md`. Directory orientation lives here.
- Do not rewrite `src/xai_sdk/proto/` by hand.
- Do not promote this checkout into an orchestrator, sandbox lane, or second Interface LLM.

## CHANGE LOG

- 2026-08-25 — Estate overlay installed: this charter, `management_key_from_env` (accepts `XAI_MANAGEMENT_API_KEY`), `upstream` remote, and submodule registration under INFRAGENS_v0.1.0, because a vendor checkout that is neither informed nor gitlinked is invisible to successors and incoherent with the superproject.
