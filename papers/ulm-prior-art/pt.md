# ULM: mapa de prior art — o que já existe, a lacuna, a fraude de novidade

**Cleiton Moura Loura**  
Iniciativa pessoal, sem afiliação institucional. Cidadão brasileiro.  
Brasil, 27 de agosto de 2026.

*Idiomas:* [Português](pt.md) · [English](en.md) · [中文](zh.md)

**Como citar:** Loura, C. M. (2026). *ULM: mapa de prior art — o que já existe, a lacuna, a fraude de novidade*. Cleiton-Moura-Loura-Papers. https://github.com/professorcinza/Cleiton-Moura-Loura-Papers

**Licença:** CC BY-SA 4.0.

**Governa / é governado.** Engrossa o §3 do paper [O Modelo Universal de Linguagem](../modelo-universal-de-linguagem/pt.md). Não substitui a [spec ULM v1](../../spec/ulm/pt.md). Não sobe o status de ULM-001–010.

**Proveniência.** Continuação do mesmo dia: a pergunta era para que serve o pesquisador se o próximo passo não é literatura. A resposta é este mapa — crivo de novidade, não *leaderboard*, não treino.

---

## Resumo

Peça a peça, quase tudo o que a spec exige **já existe** nalguma literatura ou prática. O que não existe no vocabulário padrão é o **feixe**: alcance como telos, línguas como origem no mesmo commit, margem como teste sem cota do centro, joule visível por tarefa, domínio do simbólico *e* recusa de absorver o real, spec antes de pesos, local-first como obrigação, nome como recusa, autoria aberta como falha-do-nome. Este texto marca, contra cada ULM-00X, o que ocupa, o que sobra, e o que seria **fraude de novidade** se este repositório afirmasse “o primeiro X”.

A cadeia de caracteres *Universal Language Model* e a sigla ULM **já estavam ocupadas** (Howard & Ruder, 2018). Prioridade sobre o *string* seria fraude. O paper afirma prioridade sobre o *nome do dever*, não sobre o artefato e não sobre a etiqueta.

**Palavras-chave:** prior art; ULMFiT; novidade; ULM-001–010; telos.

---

## 1. O que este texto não é

Não é revisão sistemática com protocolo de busca. Ausência aqui não prova ausência no mundo. Por isso este mapa **proíbe** a frase “somos os primeiros a”.

Não é comparação de SOTA. Não há artefato. Não há *benchmark* a vencer.

Não é briefing de tendências. Hype do dia não entra como estado da arte.

Não verifica a spec. Status de ULM-001–010 permanece `rascunho`.

Aceita-se o que o paper já aceitou: a literatura que instalou *large* como eixo e a crítica que o corrigiu sem destituí-lo. Recusa-se fingir SOTA, treinar usina para “provar” universalidade, e tomar citação por prova de alcance.

---

## 2. O nome já estava sujo

Antes de ULM-001: o *string*.

| Etiqueta | O que é | O que não é |
|---|---|---|
| **ULMFiT** (Howard & Ruder, 2018) | *Universal Language Model Fine-tuning*: receita de *fine-tune* de um modelo de língua para classificação. Ocupa **ULM** e a expressão inglesa *Universal Language Model*. | Obrigação de alcance. Margem como teste. Joule como crivo. Spec antes de pesos. Recusa de *large*. |
| **Universal Sentence Encoder** (Cer et al., 2018) | Embeddings de sentença “universais” no sentido de transferência. | Universal como dever para a beira. |
| **USM** (Zhang et al., 2023) | *Universal Speech Model* (Google): fala em muitas línguas, eixo ainda de cobertura/escala. | Telos de alcance com conta de energia e origem trilíngue no commit. |
| **Foundation model** (Bommasani et al., 2021) | Outro rebatismo do artefato grande. Troca o adjetivo; não destitui a escala. | O nome do dever que este paper propõe. |

**Fraude de novidade:** afirmar que a sigla ULM, ou a expressão *Universal Language Model*, nasce neste repositório. Não nasce. O que se reivindica é o dever: universal = alcance, não volume — e o feixe ULM-001–010. O *string* é de outrem. Usa-se com a sujeira à vista.

---

## 3. Tabela-mestra

| ID | Já ocupa (não é nosso) | Lacuna residual | Fraude se afirmarmos |
|---|---|---|---|
| **001** | Leis de escala; crítica ao tamanho; “Green AI”; SLM; destilação | Destituir *large* como telos; sucesso ≠ loss/tamanho | “Inventámos a ética dos modelos grandes” |
| **002** | mBERT, XLM-R, mT5, BLOOM, NLLB, Aya; i18n | PT/EN/ZH como origem no mesmo commit; pós-tradução = falha | “O primeiro modelo multilíngue” |
| **003** | TIC para o desenvolvimento; Masakhane; acessibilidade; “AI for Good” | Percurso de tarefa completo sem cota/login/usina do centro | “Descobrimos o Sul global” |
| **004** | Strubell; Green AI; CodeCarbon; emissões do BLOOM; model cards | Joule (ou proxy datado) visível **por tarefa**; feature voraz com ID escrito | “Os primeiros a contar energia em PNL” |
| **005** | Neuro-simbólico; modelos de código; multimodal; “protein LMs” | Axioma representação simbólica ⊆ linguagem, com língua natural como subconjunto próprio, e três tipos fora do chat | “Inventámos o multimodal / o neuro-simbólico” |
| **006** | Bender & Koller (2020); grounding; o mapa não é o território | O par com 005: expandir o domínio **e** recusar absorver o real | “Inventámos que o mundo não é texto” |
| **007** | Model cards; datasheets; Constitutional AI; engenharia de requisitos | Peso órfão = falha; spec no commit anterior ou igual; comportamento muda só depois da spec | “Inventámos documentar modelos” |
| **008** | *Local-first* (Kleppmann et al.); TinyML; on-device; llama.cpp | Primeira inferência sem nuvem do centro, como obrigação do nome, ligada a 003 | “Inventámos inferência no bolso” |
| **009** | ULMFiT; USE; USM; *foundation model* | LLM só para nomear o recusado; ULM como nome do dever, com o *string* confessado sujo | “A etiqueta é nossa” |
| **010** | OSI; GPL/AGPL; CC BY-SA; BLOOM/OLMo/Pythia; crítica ao *open washing* | Feixe AGPL + CC BY-SA + `git log` com nome + nenhum peso anónimo, como falha-do-nome | “Inventámos o código aberto” |

O residual não é uma célula. É a conjunção. Quase toda peça tem dono. O feixe, com o axioma e o crivo, e com a sujeira do nome à mostra, é a pretensão que resta — e ainda assim pretensão de dever, não de artefato.

---

## 4. Ponto a ponto

### ULM-001 — Telos de alcance

**Ocupa.** Kaplan et al. (2020) e Hoffmann et al. (2022) instalam a escala como variável independente. Bender et al. (2021) recusam o oráculo e nomeiam dano. Schwartz et al. (2020) pedem *Green AI* — mais resultado por joule, ainda sob o eixo da eficiência. Modelos “pequenos” invertem a quantidade; não trocam o conceito. Destilação, sparsidade, MoE: engenharia sob *large*.

**Não ocupa.** Um critério de pronto em que tamanho e loss **não** constituem sucesso. A spec falha o relatório que só mostra parâmetros.

**Fraude.** “Ninguém criticou a escala.” Criticou. Não a destituiu.

### ULM-002 — Línguas como origem

**Ocupa.** Conneau et al. (2020) XLM-R; Xue et al. (2021) mT5; Scao et al. (2022) BLOOM; NLLB Team (2022); Joshi et al. (2020) sobre o destino da diversidade linguística em PNL. A indústria de *locale* traduz depois.

**Não ocupa.** Cobertura de treino ≠ origem do artefato. ULM-002 verifica o commit: três saídas, mesmo significado, mesmo instante. Pós-tradução a partir do centro falha mesmo que o modelo “saiba” as três línguas.

**Fraude.** “Primeiro sistema multilíngue.” Mentira histórica.

### ULM-003 — A margem é o teste

**Ocupa.** Masakhane e a prática de PNL africana por quem fala as línguas; literatura de TIC para o desenvolvimento; acessibilidade como campo; a retórica *AI for Good*.

**Não ocupa.** “Participámos dum *workshop*” não é verificação. A spec pede um percurso de tarefa **completo** sem cota, login ou usina do centro. Funcionar no centro e depois “incluir” a beira continua sendo LLM com apêndice.

**Fraude.** “Descobrimos a periferia.” A periferia não precisava ser descoberta. Precisava deixar de ser caso de borda.

### ULM-004 — Conta de energia visível

**Ocupa.** Strubell et al. (2019); Lacoste et al. (2019); Schwartz et al. (2020); Luccioni et al. sobre emissões de modelos grandes; rastreadores de carbono de treino; seções de energia em *model cards*.

**Não ocupa.** Conta **por inferência e por tarefa**, visível a quem usa, com unidade e data — e justificativa com ID para feature que custa mais do que devolve. Paper de carbono *depois* do treino não satisfaz. Ausência de número = falha.

**Fraude.** “Os primeiros a pôr o joule na PNL.” Strubell já pôs.

### ULM-005 — Domínio do simbólico

**Ocupa.** IA neuro-simbólica (Garcez et al.); modelos de código; multimodal (texto+imagem+áudio); modelos de “linguagem” de proteínas; assistentes sobre Lean/Coq. A metáfora “tudo é linguagem” já circula — e é prima perigosa de ULM-006.

**Não ocupa.** O axioma *representação simbólica ⊆ linguagem* como domínio, língua natural como subconjunto próprio, e a prova mínima: aceitar e emitir pelo menos três tipos fora do *chat* contínuo (spec, circuito, mapa, contrato, partitura, código). Um chatbot com *plugins* não é ULM.

**Fraude.** “Inventámos o multimodal.” Não. Multimodal acrescenta canais. ULM-005 redefine o domínio da linguagem. São teses distintas. Confundi-las é fraude nas duas direções.

### ULM-006 — O mundo não é texto

**Ocupa.** Bender & Koller (2020): significado não está na forma. Críticas de *grounding* e de *embodiment*. A sentença “o mapa não é o território” é anterior a qualquer modelo.

**Não ocupa.** O par necessário com ULM-005. Expandir o simbólico **sem** este limite recai em “tudo cabe na usina”. ULM-006 é parte da tese, não apêndice ético.

**Fraude.** “Inventámos que a fome não é uma sentença.” Fraude filosófica, além de técnica.

### ULM-007 — Spec antes de pesos

**Ocupa.** Mitchell et al. (2019) *model cards*; Gebru et al. *datasheets for datasets*; Constitutional AI (princípios, não spec ligada a commit); engenharia de requisitos; *checklists* de reprodutibilidade.

**Não ocupa.** Porta dura: nenhum peso, *fine-tune* ou *checkpoint* sem ID ULM e commit da spec anterior ou igual. Peso órfão = falha. Mudou o comportamento, muda a spec **primeiro**. Card escrito depois do treino é epitáfio, não governo.

**Fraude.** “Inventámos a ficha do modelo.”

### ULM-008 — Local-first

**Ocupa.** Kleppmann et al. (2019) *local-first software*; TinyML; inferência on-device; a prática de pesos no aparelho (llama.cpp e afins). Aprendizado federado ainda costuma coordenar no centro.

**Não ocupa.** Local-first como **obrigação de universalidade**, não como opção de *deploy*. Ligado a ULM-003: a primeira inferência que exige a nuvem do centro falha o nome. Bolso e malha são o alvo, não o apêndice.

**Fraude.** “Inventámos o modelo no telefone.”

### ULM-009 — Nome e recusa

**Ocupa.** Tudo o §2. A indústria rebatiza sem destituir (*foundation*, *frontier*, *small*).

**Não ocupa.** A disciplina de escrita: LLM só para nomear o recusado; ULM para o dever; e a confissão pública de que o *string* já tinha dono.

**Fraude.** Tratar a etiqueta como invenção deste paper. O paper já recusou prioridade sobre o artefato; este mapa recusa prioridade sobre a cadeia de caracteres.

### ULM-010 — Autoria aberta

**Ocupa.** OSI; GPL e AGPL; CC BY-SA; pesos com procedência (BLOOM, OLMo, Pythia); a crítica ao *open washing* (licença que não abre, “open” sem peso, peso sem história).

**Não ocupa.** O feixe como falha-do-nome: AGPL-3.0-or-later no código, CC BY-SA 4.0 no conteúdo, nome no `git log`, nenhum binário de peso sem procedência — *junto* com ULM-001–009. Licença permissiva com usina opaca não paga esta dívida.

**Fraude.** “Inventámos o aberto.”

---

## 5. O que este mapa não autoriza

Não autoriza treino. ULM-007 continua: spec antes de pesos. Este texto não é spec nova; não cria ID ULM-011.

Não autoriza *leaderboard*. Não há artefato; não há “SOTA de alcance”.

Não autoriza a frase “lacuna total”. A lacuna é o feixe e o telos, não cada peça.

Não autoriza prioridade sobre ULMFiT, sobre *Universal Sentence Encoder*, sobre NLLB, sobre *local-first*, sobre *model cards*, sobre Strubell.

Autoriza uma correção ao paper: o *nome do dever* não é o *string*. O *string* estava ocupado. O dever — alcance sobre o simbólico, margem como teste, joule como crivo, spec antes de pesos — continua sendo a pretensão. Pretensão se prova com evidência. Ainda não há.

---

## 6. Próximo passo do pesquisador

Não é mais paper de conceito. Não é CUDA.

1. Protocolo medido para ULM-004 (unidade, data, onde o número aparece ao usuário).
2. Percurso de tarefa para ULM-003 e ULM-008 que se possa falhar (offline, sem cota).
3. Três tipos simbólicos para ULM-005, com exemplo no repo, sem pesos.
4. Porta de CI para ULM-002 (diff só numa língua = falha) e ULM-007 (peso órfão = falha) quando houver artefato.

Sem isso, o mapa é honesto e a spec continua rascunho. Com *leaderboard* no lugar disso, volta-se ao menu que o paper recusou.

---

## Referências

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
*Brasil, 27 de agosto de 2026*
