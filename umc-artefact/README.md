# UMC — Artefato mínimo / Minimal artefact / Artefacto mínimo / 最小制品

**Data / Date:** 27/08/2026 · **Status:** rascunho / draft · **Licença / Licence / Licencia / 许可:** AGPL-3.0-or-later (código), CC BY-SA 4.0 (conteúdo)

Primeiro artefato mínimo verificável do paper UMC (Fase 3 da agenda). Sem pesos, sem rede, stdlib apenas. Governado pela spec UMC-001–011 (paper-umc). First minimal verifiable artefact of the UMC paper (Phase 3 of the agenda). No weights, no network, stdlib only. Governed by spec UMC-001–011 (paper-umc). Primer artefacto mínimo verificable del paper UMC (Fase 3 de la agenda). Sin pesos, sin red, solo stdlib. Gobernado por la spec UMC-001–011 (paper-umc). UMC 论文的第一个最小可核验制品（议程阶段 3）。无权重、无网络、仅标准库。受 spec UMC-001–011（paper-umc）管辖。

## English

Three symbolic types beyond chat (UMC-005), each with finite encoding, at least one operation and an operational equality criterion (UMC-011):

| Type | Encoding | Operations | Equality |
|---|---|---|---|
| `spec` | canonical JSON (`nome`, `versao`, `interface`, `precondicao`) | `validar()` | canonical form |
| `mapa` | canonical JSON (`pontos`, `vias`) | `rota()`, `distancia()` | canonical form |
| `partitura` | canonical JSON (`compasso`, `notas`) | `transpor()`, `duracao_total()` | canonical form |

Verifiable transformations (none requires trained weights, UMC-007):

- `spec → código`: generates a Python function skeleton from the spec.
- `mapa → contrato`: generates a route agreement (PT/EN/ES/ZH) with the calculated distance.
- `partitura → esquema`: generates a timing diagram with start/end times per pulse.

**Run (local-first, UMC-008 — no network):**

```bash
cd umc-artefact
python3 -m unittest discover -s umc/testes -v          # tests
python3 -m umc tipos                                     # list the three types
python3 -m umc spec-para-codigo exemplos/spec-somar.json
python3 -m umc mapa-para-contrato exemplos/mapa-vila.json --origem A --destino C --idioma pt
python3 -m umc partitura-para-esquema exemplos/partitura-simples.json
python3 -m umc energia                                    # energy log (UMC-004)
```

Every task writes an energy entry to `logs/energia.jsonl` with unit (`J`) and date (ISO 8601). The value is an explicit proxy (wall time × 15 W nominal), never a physical measurement — see `umc/energia.py`.

## Português

Três tipos simbólicos fora do chat (UMC-005), cada um com encoding finito, pelo menos uma operação e critério operacional de igualdade (UMC-011):

| Tipo | Encoding | Operações | Igualdade |
|---|---|---|---|
| `spec` | JSON canônico (`nome`, `versao`, `interface`, `precondicao`) | `validar()` | forma canônica |
| `mapa` | JSON canônico (`pontos`, `vias`) | `rota()`, `distancia()` | forma canônica |
| `partitura` | JSON canônico (`compasso`, `notas`) | `transpor()`, `duracao_total()` | forma canônica |

Transformações verificáveis (nenhuma exige pesos treinados, UMC-007):

- `spec → código`: gera um esqueleto de função Python a partir da spec.
- `mapa → contrato`: gera um contrato de percurso (PT/EN/ES/ZH) com a distância calculada.
- `partitura → esquema`: gera um diagrama de temporização com início/fim por pulso.

**Executar (local-first, UMC-008 — sem rede):**

```bash
cd umc-artefact
python3 -m unittest discover -s umc/testes -v          # testes
python3 -m umc tipos                                     # lista os três tipos
python3 -m umc spec-para-codigo exemplos/spec-somar.json
python3 -m umc mapa-para-contrato exemplos/mapa-vila.json --origem A --destino C --idioma pt
python3 -m umc partitura-para-esquema exemplos/partitura-simples.json
python3 -m umc energia                                    # log de energia (UMC-004)
```

Cada tarefa grava uma entrada de energia em `logs/energia.jsonl` com unidade (`J`) e data (ISO 8601). O valor é proxy explícito (tempo de parede × 15 W nominal), nunca medição física — ver `umc/energia.py`.

## Español

Tres tipos simbólicos fuera del chat (UMC-005), cada uno con encoding finito, al menos una operación y criterio operacional de igualdad (UMC-011):

| Tipo | Encoding | Operaciones | Igualdad |
|---|---|---|---|
| `spec` | JSON canónico (`nome`, `versao`, `interface`, `precondicao`) | `validar()` | forma canónica |
| `mapa` | JSON canónico (`pontos`, `vias`) | `rota()`, `distancia()` | forma canónica |
| `partitura` | JSON canónico (`compasso`, `notas`) | `transpor()`, `duracao_total()` | forma canónica |

Transformaciones verificables (ninguna exige pesos entrenados, UMC-007):

- `spec → código`: genera un esqueleto de función Python a partir de la spec.
- `mapa → contrato`: genera un contrato de recorrido (PT/EN/ES/ZH) con la distancia calculada.
- `partitura → esquema`: genera un diagrama de temporización con inicio/fin por pulso.

**Ejecutar (local-first, UMC-008 — sin red):**

```bash
cd umc-artefact
python3 -m unittest discover -s umc/testes -v          # pruebas
python3 -m umc tipos                                     # lista los tres tipos
python3 -m umc spec-para-codigo exemplos/spec-somar.json
python3 -m umc mapa-para-contrato exemplos/mapa-vila.json --origem A --destino C --idioma pt
python3 -m umc partitura-para-esquema exemplos/partitura-simples.json
python3 -m umc energia                                    # log de energía (UMC-004)
```

Cada tarea graba una entrada de energía en `logs/energia.jsonl` con unidad (`J`) y fecha (ISO 8601). El valor es proxy explícito (tiempo de pared × 15 W nominal), nunca medición física — ver `umc/energia.py`.

## 中文

三个聊天之外的符号类型（UMC-005），每个都有有限编码、至少一种运算与操作性相等判据（UMC-011）：

| 类型 | 编码 | 运算 | 相等 |
|---|---|---|---|
| `spec` | 规范 JSON（`nome`、`versao`、`interface`、`precondicao`） | `validar()` | 规范形式 |
| `mapa` | 规范 JSON（`pontos`、`vias`） | `rota()`、`distancia()` | 规范形式 |
| `partitura` | 规范 JSON（`compasso`、`notas`） | `transpor()`、`duracao_total()` | 规范形式 |

可核验变换（无一需要训练权重，UMC-007）：

- `spec → 代码`：由 spec 生成 Python 函数骨架。
- `mapa → 合同`：生成路线协议（PT/EN/ES/ZH），含计算距离。
- `partitura → 示意图`：生成定时图，每脉冲含起止时刻。

**运行（local-first，UMC-008——无网络）：**

```bash
cd umc-artefact
python3 -m unittest discover -s umc/testes -v          # 测试
python3 -m umc tipos                                     # 列出三个类型
python3 -m umc spec-para-codigo exemplos/spec-somar.json
python3 -m umc mapa-para-contrato exemplos/mapa-vila.json --origem A --destino C --idioma pt
python3 -m umc partitura-para-esquema exemplos/partitura-simples.json
python3 -m umc energia                                    # 能耗日志（UMC-004）
```

每项任务向 `logs/energia.jsonl` 写入一条能耗记录，含单位（`J`）与日期（ISO 8601）。数值为显式代理（墙钟时间 × 15 W 标称），绝非物理测量——见 `umc/energia.py`。
