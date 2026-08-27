# -*- coding: utf-8 -*-
"""UMC — Modelo Universal Computacional / Universal Computational Model /
Modelo Universal Computacional / 通用计算模型.

Artefato mínimo verificável (Fase 3 da agenda, 27/08/2026).
Minimal verifiable artefact (Phase 3 of the agenda, 27 Aug 2026).
Artefacto mínimo verificable (Fase 3 de la agenda, 27/08/2026).
最小可核验制品（议程阶段 3，2026 年 8 月 27 日）。

Sem pesos. Sem rede. Sem centro. Stdlib apenas.
No weights. No network. No centre. Stdlib only.
Sin pesos. Sin red. Sin centro. Solo stdlib.
无权重。无网络。无中心。仅标准库。

Governa: spec UMC-001-011 do paper-umc. Nenhuma linha de peso sem spec.
Governed by: spec UMC-001-011 of paper-umc. No line of weights without a spec.
Gobernado por: spec UMC-001-011 de paper-umc. Ninguna línea de pesos sin spec.
受 spec UMC-001-011（paper-umc）管辖：无 spec 则无一行权重。

SPDX-License-Identifier: AGPL-3.0-or-later
Copyright (c) 2026 Cleiton Moura Loura
"""

__name_do_dever__ = "UMC"
__versao__ = "0.1.0"
__data__ = "2026-08-27"
__licenca__ = "AGPL-3.0-or-later"

from .tipos import Spec, Mapa, Partitura, canonico  # noqa: F401

__all__ = ["Spec", "Mapa", "Partitura", "canonico"]
