# ULM: a prior-art map — what already exists, the gap, novelty fraud

**Cleiton Moura Loura**  
Personal initiative, no institutional affiliation. Brazilian citizen.  
Brazil, 27 August 2026.

*Languages:* [Português](pt.md) · [English](en.md) · [中文](zh.md)

**How to cite:** Loura, C. M. (2026). *ULM: a prior-art map — what already exists, the gap, novelty fraud*. Cleiton-Moura-Loura-Papers. https://github.com/professorcinza/Cleiton-Moura-Loura-Papers

**Licence:** CC BY-SA 4.0.

**Governs / is governed.** Thickens §3 of the paper [The Universal Language Model](../modelo-universal-de-linguagem/en.md). It does not replace [ULM spec v1](../../spec/ulm/en.md). It does not raise the status of ULM-001–010.

**Provenance.** Continuation of the same day: the question was what researchers are for if the next step is not literature. The answer is this map — a sieve of novelty, not a leaderboard, not a training run.

---

## Abstract

Piece by piece, almost everything the spec requires **already exists** in some literature or practice. What does not exist in the standard vocabulary is the **bundle**: reach as telos, languages as origin in the same commit, the margin as test without a quota of the centre, joules visible per task, the domain of the symbolic *and* the refusal to absorb the real, spec before weights, local-first as obligation, the name as refusal, open authorship as fail-the-name. Against each ULM-00X this text marks what occupies, what remains, and what would be **novelty fraud** if this repository claimed “the first X”.

The character string *Universal Language Model* and the acronym ULM **were already occupied** (Howard & Ruder, 2018). Priority over the *string* would be fraud. The paper claims priority over the *name of the duty*, not over the artefact and not over the label.

**Keywords:** prior art; ULMFiT; novelty; ULM-001–010; telos.

---

## 1. What this text is not

It is not a systematic review with a search protocol. Absence here does not prove absence in the world. This map therefore **forbids** the sentence “we are the first to”.

It is not a SOTA comparison. There is no artefact. There is no benchmark to win.

It is not a trend briefing. The hype of the day does not enter as the state of the art.

It does not verify the spec. The status of ULM-001–010 remains `draft`.

What the paper already accepted is accepted: the literature that installed *large* as axis, and the critique that corrected it without deposing it. Refused: fake SOTA, training a plant to “prove” universality, and taking a citation as proof of reach.

---

## 2. The name was already dirty

Before ULM-001: the *string*.

| Label | What it is | What it is not |
|---|---|---|
| **ULMFiT** (Howard & Ruder, 2018) | *Universal Language Model Fine-tuning*: a recipe for fine-tuning a language model for classification. Occupies **ULM** and the English phrase *Universal Language Model*. | An obligation of reach. The margin as test. The joule as sieve. Spec before weights. Refusal of *large*. |
| **Universal Sentence Encoder** (Cer et al., 2018) | Sentence embeddings that are “universal” in the sense of transfer. | Universal as a duty to those at the edge. |
| **USM** (Zhang et al., 2023) | Google *Universal Speech Model*: speech in many languages, still on an axis of coverage/scale. | Telos of reach with an energy account and trilingual origin in the commit. |
| **Foundation model** (Bommasani et al., 2021) | Another renaming of the large artefact. It changes the adjective; it does not depose scale. | The name of the duty this paper proposes. |

**Novelty fraud:** claiming that the acronym ULM, or the phrase *Universal Language Model*, is born in this repository. It is not. What is claimed is the duty: universal = reach, not volume — and the bundle ULM-001–010. The *string* belongs to others. It is used with the dirt in view.

---

## 3. Master table

| ID | Already occupies (not ours) | Residual gap | Fraud if we claimed |
|---|---|---|---|
| **001** | Scaling laws; critique of size; Green AI; SLMs; distillation | Deposing *large* as telos; success ≠ loss/size | “We invented the ethics of large models” |
| **002** | mBERT, XLM-R, mT5, BLOOM, NLLB, Aya; i18n | PT/EN/ZH as origin in the same commit; post-translation = fail | “The first multilingual model” |
| **003** | ICT4D; Masakhane; accessibility; “AI for Good” | A complete task path without quota/login/plant of the centre | “We discovered the Global South” |
| **004** | Strubell; Green AI; CodeCarbon; BLOOM emissions; model cards | Joules (or dated proxy) visible **per task**; voracious features with a written ID | “The first to count energy in NLP” |
| **005** | Neurosymbolic AI; code models; multimodal; “protein LMs” | Axiom symbolic representation ⊆ language, natural language a proper subset, and three types outside chat | “We invented multimodal / neurosymbolic” |
| **006** | Bender & Koller (2020); grounding; the map is not the territory | The pair with 005: expand the domain **and** refuse to absorb the real | “We invented that the world is not text” |
| **007** | Model cards; datasheets; Constitutional AI; requirements engineering | Orphan weights = fail; spec at an earlier or equal commit; behaviour changes only after the spec | “We invented documenting models” |
| **008** | Local-first (Kleppmann et al.); TinyML; on-device; llama.cpp | First inference without the centre’s cloud, as an obligation of the name, bound to 003 | “We invented inference in the pocket” |
| **009** | ULMFiT; USE; USM; foundation model | LLM only to name the refused; ULM as the name of the duty, with the string confessed dirty | “The label is ours” |
| **010** | OSI; GPL/AGPL; CC BY-SA; BLOOM/OLMo/Pythia; critique of open washing | Bundle AGPL + CC BY-SA + named `git log` + no anonymous weights, as fail-the-name | “We invented open source” |

The residual is not a cell. It is the conjunction. Almost every piece has an owner. The bundle, with the axiom and the sieve, and with the dirt of the name in view, is the remaining claim — and still a claim of duty, not of artefact.

---

## 4. Point by point

### ULM-001 — Telos of reach

**Occupies.** Kaplan et al. (2020) and Hoffmann et al. (2022) install scale as an independent variable. Bender et al. (2021) refuse the oracle and name harm. Schwartz et al. (2020) ask for Green AI — more result per joule, still on the axis of efficiency. “Small” models invert the quantity; they do not change the concept. Distillation, sparsity, MoE: engineering under *large*.

**Does not occupy.** A done-when in which size and loss do **not** constitute success. The spec fails the report that only shows parameters.

**Fraud.** “Nobody criticised scale.” They did. They did not depose it.

### ULM-002 — Languages as origin

**Occupies.** Conneau et al. (2020) XLM-R; Xue et al. (2021) mT5; Scao et al. (2022) BLOOM; NLLB Team (2022); Joshi et al. (2020) on the fate of linguistic diversity in NLP. The locale industry translates afterwards.

**Does not occupy.** Training coverage ≠ origin of the artefact. ULM-002 verifies the commit: three outputs, same meaning, same instant. Post-translation from the centre fails even if the model “knows” the three languages.

**Fraud.** “First multilingual system.” Historical lie.

### ULM-003 — The margin is the test

**Occupies.** Masakhane and African NLP practice by those who speak the languages; ICT for development; accessibility as a field; the rhetoric of AI for Good.

**Does not occupy.** “We attended a workshop” is not verification. The spec asks for a **complete** task path without quota, login or plant of the centre. Working at the centre and then “including” the edge remains an LLM with an appendix.

**Fraud.** “We discovered the periphery.” The periphery did not need discovering. It needed to stop being an edge case.

### ULM-004 — Visible energy account

**Occupies.** Strubell et al. (2019); Lacoste et al. (2019); Schwartz et al. (2020); Luccioni et al. on emissions of large models; training carbon trackers; energy sections in model cards.

**Does not occupy.** An account **per inference and per task**, visible to whoever uses it, with unit and date — and a written ID for a feature that costs more than it returns. A carbon paper *after* training does not suffice. No number = fail.

**Fraud.** “The first to put the joule on the NLP table.” Strubell already did.

### ULM-005 — Domain of the symbolic

**Occupies.** Neurosymbolic AI (Garcez et al.); code models; multimodal (text+image+audio); “language” models of proteins; assistants over Lean/Coq. The metaphor “everything is language” already circulates — and is a dangerous cousin of ULM-006.

**Does not occupy.** The axiom *symbolic representation ⊆ language* as domain, natural language as a proper subset, and the minimum proof: accept and emit at least three types outside continuous chat (spec, circuit, map, contract, score, code). A chatbot with plugins is not a ULM.

**Fraud.** “We invented multimodal.” No. Multimodal adds channels. ULM-005 redefines the domain of language. They are distinct theses. Confusing them is fraud in both directions.

### ULM-006 — The world is not text

**Occupies.** Bender & Koller (2020): meaning is not in the form. Grounding and embodiment critiques. “The map is not the territory” predates any model.

**Does not occupy.** The necessary pair with ULM-005. Expanding the symbolic **without** this limit collapses into “everything fits in the plant”. ULM-006 is part of the thesis, not an ethical appendix.

**Fraud.** “We invented that hunger is not a sentence.” Philosophical fraud, as well as technical.

### ULM-007 — Spec before weights

**Occupies.** Mitchell et al. (2019) model cards; Gebru et al. datasheets for datasets; Constitutional AI (principles, not a spec bound to a commit); requirements engineering; reproducibility checklists.

**Does not occupy.** A hard gate: no weights, fine-tune or checkpoint without a ULM ID and a spec commit earlier than or equal to the weights. Orphan weights = fail. Behaviour changed, the spec changes **first**. A card written after training is an epitaph, not government.

**Fraud.** “We invented the model card.”

### ULM-008 — Local-first

**Occupies.** Kleppmann et al. (2019) local-first software; TinyML; on-device inference; the practice of weights on the device (llama.cpp and kin). Federated learning still usually coordinates at the centre.

**Does not occupy.** Local-first as an **obligation of universality**, not a deploy option. Bound to ULM-003: the first inference that requires the centre’s cloud fails the name. Pocket and mesh are the target, not the appendix.

**Fraud.** “We invented the model on the phone.”

### ULM-009 — Name and refusal

**Occupies.** All of §2. Industry renames without deposing (*foundation*, *frontier*, *small*).

**Does not occupy.** The discipline of writing: LLM only to name the refused; ULM for the duty; and the public confession that the *string* already had an owner.

**Fraud.** Treating the label as this paper’s invention. The paper already refused priority over the artefact; this map refuses priority over the character string.

### ULM-010 — Open authorship

**Occupies.** OSI; GPL and AGPL; CC BY-SA; weights with provenance (BLOOM, OLMo, Pythia); the critique of open washing (a licence that does not open, “open” without weights, weights without history).

**Does not occupy.** The bundle as fail-the-name: AGPL-3.0-or-later on code, CC BY-SA 4.0 on content, a name in `git log`, no weight binary without provenance — *together* with ULM-001–009. A permissive licence with an opaque plant does not pay this debt.

**Fraud.** “We invented the open.”

---

## 5. What this map does not authorise

It does not authorise training. ULM-007 still holds: spec before weights. This text is not a new spec; it does not create ID ULM-011.

It does not authorise a leaderboard. There is no artefact; there is no “SOTA of reach”.

It does not authorise the sentence “total gap”. The gap is the bundle and the telos, not each piece.

It does not authorise priority over ULMFiT, over Universal Sentence Encoder, over NLLB, over local-first, over model cards, over Strubell.

It authorises a correction to the paper: the *name of the duty* is not the *string*. The *string* was occupied. The duty — reach over the symbolic, the margin as test, the joule as sieve, spec before weights — remains the claim. A claim is proved with evidence. There is none yet.

---

## 6. The researcher’s next step

Not another concept paper. Not CUDA.

1. A measured protocol for ULM-004 (unit, date, where the number appears to the user).
2. A task path for ULM-003 and ULM-008 that can be failed (offline, no quota).
3. Three symbolic types for ULM-005, with an example in the repo, without weights.
4. A CI gate for ULM-002 (diff in only one language = fail) and ULM-007 (orphan weights = fail) when an artefact exists.

Without that, the map is honest and the spec remains draft. With a leaderboard in its place, one returns to the menu the paper refused.

---

## References

Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI feedback. *arXiv:2212.08073*.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of FAccT 2021*.

Bender, E. M., & Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. *Proceedings of ACL 2020*.

Bommasani, R., et al. (2021). On the opportunities and risks of foundation models. *arXiv:2108.07258*.

Cer, D., et al. (2018). Universal Sentence Encoder. *arXiv:1803.11175*.

Conneau, A., et al. (2020). Unsupervised cross-lingual representation learning at scale. *Proceedings of ACL 2020*.

Garcez, A. d'Avila, & Lamb, L. C. (2020). Neurosymbolic AI: The 3rd wave. *arXiv:2012.05876*.

Gebru, T., et al. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12).

Hoffmann, J., et al. (2022). Training compute-optimal large language models. *arXiv:2203.15556*.

Howard, J., & Ruder, S. (2018). Universal Language Model Fine-tuning for text classification. *Proceedings of ACL 2018*.

Joshi, P., Santy, S., Budhiraja, A., Bali, K., & Choudhury, M. (2020). The state and fate of linguistic diversity and inclusion in the NLP world. *Proceedings of ACL 2020*.

Kaplan, J., et al. (2020). Scaling laws for neural language models. *arXiv:2001.08361*.

Kleppmann, M., Wiggins, A., van Hardenberg, P., & McGranaghan, M. (2019). Local-first software: You own your data, in spite of the cloud. *Ink & Switch*.

Lacoste, A., Luccioni, A., Schmidt, V., & Dandres, T. (2019). Quantifying the carbon emissions of machine learning. *arXiv:1910.09700*.

Luccioni, A. S., Viguier, S., & Ligozat, A.-L. (2023). Estimating the carbon footprint of BLOOM, a 176B parameter language model. *Journal of Machine Learning Research*.

Mitchell, M., et al. (2019). Model cards for model reporting. *Proceedings of FAT\* 2019*.

Nekoto, W., et al. (2020). Participatory research for low-resourced machine translation: A case study in African languages. *Findings of EMNLP 2020* (Masakhane).

NLLB Team. (2022). No Language Left Behind: Scaling human-centered machine translation. *arXiv:2207.04672*.

Scao, T. L., et al. (2022). BLOOM: A 176B-parameter open-access multilingual language model. *arXiv:2211.05100*.

Schwartz, R., Dodge, J., Smith, N. A., & Etzioni, O. (2020). Green AI. *Communications of the ACM, 63*(12).

Strubell, E., Ganesh, A., & McCallum, A. (2019). Energy and policy considerations for deep learning in NLP. *Proceedings of ACL 2019*.

Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.

Widder, D. G., West, S. M., & Whittaker, M. (2023). Open (for business): Big tech, concentrated power, and the political economy of open AI. SSRN.

Xue, L., et al. (2021). mT5: A massively multilingual pre-trained text-to-text transformer. *Proceedings of NAACL 2021*.

Zhang, Y., et al. (2023). Google USM: Scaling automatic speech recognition beyond 100 languages. *arXiv:2303.01037*.

---

*Cleiton Moura Loura*  
*Brazil, 27 August 2026*
