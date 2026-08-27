# Spec ULM — Universal Language Model

**Cleiton-Moura-Loura-Papers · spec/ulm · v1 · status: draft**  
**Governs:** the paper [The Universal Language Model](../../papers/modelo-universal-de-linguagem/en.md)  
**Date:** 27 August 2026  
**Languages:** [Português](pt.md) · [English](en.md) · [中文](zh.md)

No line of weights, inference code or training without this spec. No spec without a path of verification. Status rises only with recorded evidence.

Cycle: `draft` → `reviewed` → `verified`.

---

## ULM-001 — Telos of reach

The system is judged by **reach**, not by scale. Parameter count, token volume and position on a loss benchmark do **not** constitute success.

**Verification:** no “done” report cites scale as a sufficient criterion. If the only success number is size or loss, ULM-001 fails.

**Status:** draft.

## ULM-002 — Languages as origin

Portuguese, English and Chinese are born together. Post-translation from the centre does not count as origin.

**Verification:** for each artefact version, the three outputs (or specs, or interface strings) exist in the same commit, with the same meaning. A diff in only one language = fail.

**Status:** draft.

## ULM-003 — The margin is the test

The person on the periphery of any nation is a first-class user, not an edge case. “Works at the centre” is not done.

**Verification:** there exists at least one complete task path **without** a quota, login or plant of the centre. If the task requires the industrial quota, ULM-003 fails.

**Status:** draft.

## ULM-004 — Visible energy account

Every inference and every training run publishes joules (or a measured, dated proxy). A feature that costs more energy than it returns is justified in writing, with an ID.

**Verification:** a log or measurement per task, with unit and date. No account = fail. Justification without a number = fail.

**Status:** draft.

## ULM-005 — Domain of the symbolic

The domain is the set of symbolic representations. Natural language is a subset. A system that only chats in prose is not a ULM.

**Verification:** the artefact accepts and emits at least three types outside continuous chat — e.g. spec, circuit/schematic, map, contract, score, code. Prose alone = fail.

**Status:** draft.

## ULM-006 — The world is not a text

Joule, hunger, body and referent are **not** language. The model does not declare that life fits inside it.

**Verification:** no official output asserts that the non-symbolic is a token. If the system “solves” hunger or energy with text alone, ULM-006 fails.

**Status:** draft.

## ULM-007 — Spec before weights

There is no training, fine-tune or checkpoint without this spec governing it. If behaviour changes, the spec changes first.

**Verification:** each weight artefact points to a ULM ID and a spec commit earlier than or equal to the weight commit. Orphan weights = fail.

**Status:** draft.

## ULM-008 — Local-first

The minimum path of use runs without the centre’s network. Mesh and pocket are the target, not the data centre.

**Verification:** a ULM-003 task completes *offline* after the artefact is on the device. If the first inference requires the centre’s cloud, ULM-008 fails.

**Status:** draft.

## ULM-009 — Name and refusal

The artefact is called ULM. The acronym LLM appears only to name the refused concept.

**Verification:** a search of the artefact repository. LLM outside historical citation or the refusal = fail.

**Status:** draft.

## ULM-010 — Open authorship

Code AGPL-3.0-or-later; content CC BY-SA 4.0; authorship in Git history. No anonymous line of weights.

**Verification:** LICENSE present; `git log` with a name; no binary without provenance. Absence = fail.

**Status:** draft.

---

## Done

The ULM is **verified** only when ULM-001 through ULM-010 are `verified` with dated evidence. To fail one is to fail the name.

There is no artefact. This spec is the next step of the 27/08/2026 continuation — not the training run.

---

*Cleiton Moura Loura*  
*Brazil, 27 August 2026*
