# Spec UM — Universal Model

**Cleiton-Moura-Loura-Papers · spec/um · v1 · status: draft**  
**Governs:** the paper [The Universal Model](../../papers/modelo-universal/en.md)  
**Date:** 27 August 2026  
**Languages:** [Português](pt.md) · [English](en.md) · [中文](zh.md)

No line of weights, inference code or training without this spec. No spec without a path of verification. Status rises only with recorded evidence.

Cycle: `draft` → `reviewed` → `verified`.

---

## UM-001 — Telos of reach

The system is judged by **reach**, not by scale. Parameter count, token volume and position on a loss benchmark do **not** constitute success.

**Verification:** no “done” report cites scale as a sufficient criterion. If the only success number is size or loss, UM-001 fails.

**Status:** draft.

## UM-002 — Languages as origin

Portuguese, English and Chinese are born together. Post-translation from the centre does not count as origin.

**Verification:** for each artefact version, the three outputs (or specs, or interface strings) exist in the same commit, with the same meaning. A diff in only one language = fail.

**Status:** draft.

## UM-003 — The margin is the test

The person on the periphery of any nation is a first-class user, not an edge case. “Works at the centre” is not done.

**Verification:** there exists at least one complete task path **without** a quota, login or plant of the centre. If the task requires the industrial quota, UM-003 fails.

**Status:** draft.

## UM-004 — Visible energy account

Every inference and every training run publishes joules (or a measured, dated proxy). A feature that costs more energy than it returns is justified in writing, with an ID.

**Verification:** a log or measurement per task, with unit and date. No account = fail. Justification without a number = fail.

**Status:** draft.

## UM-005 — Domain of the symbolic

The domain is the set of symbolic representations. Natural language is a subset. A system that only chats in prose is not a UM.

**Verification:** the artefact accepts and emits at least three types outside continuous chat — e.g. spec, circuit/schematic, map, contract, score, code. Prose alone = fail.

**Status:** draft.

## UM-006 — The world is not a text

Joule, hunger, body and referent are **not** language. The model does not declare that life fits inside it.

**Verification:** no official output asserts that the non-symbolic is a token. If the system “solves” hunger or energy with text alone, UM-006 fails.

**Status:** draft.

## UM-007 — Spec before weights

There is no training, fine-tune or checkpoint without this spec governing it. If behaviour changes, the spec changes first.

**Verification:** each weight artefact points to a UM ID and a spec commit earlier than or equal to the weight commit. Orphan weights = fail.

**Status:** draft.

## UM-008 — Local-first

The minimum path of use runs without the centre’s network. Mesh and pocket are the target, not the data centre.

**Verification:** a UM-003 task completes *offline* after the artefact is on the device. If the first inference requires the centre’s cloud, UM-008 fails.

**Status:** draft.

## UM-009 — Name and refusal

The artefact is called UM. The acronym LLM appears only to name the refused concept. The acronym ULM appears only for ULMFiT and for the first name, now vacated.

**Verification:** a search of the artefact repository. LLM outside historical citation or the refusal = fail. ULM outside ULMFiT, historical citation or the vacated name = fail.

**Status:** draft.

## UM-010 — Open authorship

Code AGPL-3.0-or-later; content CC BY-SA 4.0; authorship in Git history. No anonymous line of weights.

**Verification:** LICENSE present; `git log` with a name; no binary without provenance. Absence = fail.

**Status:** draft.

---

## Done

The UM is **verified** only when UM-001 through UM-010 are `verified` with dated evidence. To fail one is to fail the name.

There is no artefact. This spec is the next step of the 27/08/2026 continuation — not the training run.

Prior art against UM-001–010: [map](../../papers/um-prior-art/en.md). The map does not raise the status of this spec.

---

*Cleiton Moura Loura*  
*Brazil, 27 August 2026*
