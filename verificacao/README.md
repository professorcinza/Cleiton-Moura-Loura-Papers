# Verificação — instrumentos da Fase 2 / Verification — Phase 2 instruments

**Data / Date:** 27/08/2026 · **Licença / Licence:** CC BY-SA 4.0 (conteúdo)

Instrumentos de verificação por item da spec UMC-001–011 (Fase 2 da agenda, Parte V do paper). Cada instrumento produz evidência datada em JSON; o runner consolidado grava `evidencia-<data>.json`.

Phase 2 verification instruments per item of spec UMC-001–011 (Phase 2 of the agenda, Part V of the paper). Each instrument produces dated evidence in JSON; the consolidated runner writes `evidencia-<date>.json`.

**Executar / Run:**

```bash
python3 verificacao/roda_verificacao.py
```

| Item | Instrumento / Instrument | Critério / Criterion |
|---|---|---|
| UMC-002 | `umc002_origem.py` | todo commit que toca conteúdo toca as quatro línguas / every content commit touches all four languages |
| UMC-003 | `umc003_margem.py` | percurso da margem completo, 0 chamadas ao centro / margin task path complete, 0 calls to the centre |
| UMC-006 | `umc006_mundo.py` | zero afirmações de que o não-simbólico é token (recusas classificadas) / zero claims that the non-symbolic is a token (refusals classified) |
| UMC-008 | `umc008_airgap.py` | percursos completam com sockets bloqueados; nenhum import de rede / paths complete with sockets blocked; no network imports |
| UMC-010 | `umc010_autoria.py` | LICENSE presente; git log com nome; nenhum binário rastreado / LICENSE present; named git log; no tracked binaries |

Status registrado: 5/5 PASSA (27/08/2026) — evidência em `evidencia-2026-08-27.json`.

Recorded status: 5/5 PASS (27/08/2026) — evidence in `evidencia-2026-08-27.json`.
