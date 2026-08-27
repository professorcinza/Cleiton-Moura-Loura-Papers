# O Modelo Universal Computacional (UMC): do telos da escala ao domínio do simbólico

**Cleiton Moura Loura**  
Iniciativa pessoal, sem afiliação institucional. Cidadão brasileiro.  
Brasil, 27 de agosto de 2026.

*Languages / Idiomas / Idiomas / 语言:* [English](paper-umc.en.md) · [Português](paper-umc.pt.md) · [Español](paper-umc.es.md) · [中文](paper-umc.zh.md)

**Como citar:** Loura, C. M. (2026). *O Modelo Universal Computacional (UMC)*. Cleiton-Moura-Loura-Papers. https://github.com/professorcinza/Cleiton-Moura-Loura-Papers

**Licença:** CC BY-SA 4.0.

**Proveniência.** Este artigo é a continuação, em público e com nome, de um diálogo de pesquisa de 27 de agosto de 2026. A interlocução industrial perguntou em que frente de LLM se trabalhava. A primeira resposta foi substituir *Large Language Model* por *Universal Language Model*. Esse *string* já estava ocupado (Howard & Ruder, 2018, ULMFiT). UM, frase genérica, foi vacado. O nome do dever é **Modelo Universal Computacional** (UMC). Linguagem permanece o domínio (axioma), não o tipo industrial. Computacional é porta: só entra o símbolo que admite modelo computacional — e o mundo não é computação. O print dessa interlocução não se arquiva neste repositório (produto de terceiro; política do repositório). Esta edição consolidada substitui os documentos separados do mesmo dia (conceito, prior art, fundamentos, spec, agenda): o que o diálogo chamou de "hipótese", aqui é teorema; o que era ULM/UM na interlocução é UMC, o nome do dever.

## Parte I — O conceito

### Resumo

Este paper substitui o conceito de *Large Language Model* (LLM) pelo de **Modelo Universal Computacional** (UMC). A substituição não é nominal: troca o telos. *Large* nomeia escala — parâmetros, capital, joules — e entrega primeiro a quem já era grande. *Universal* nomeia obrigação de alcance: toda língua como origem, toda margem como usuária de primeira classe, toda inferência com conta de energia visível. *Computacional* nomeia a porta: todo símbolo processado admite modelo computacional — encoding, operação, igualdade operacional. Funda-se um axioma: **toda representação simbólica está no conjunto da linguagem** (representação simbólica ⊆ linguagem). A língua natural é subconjunto, não o domínio. O UMC, portanto, não é um modelo de conversa: é um modelo do simbólico que só processa o que é computacionalmente modelável. O mundo, porém, não é um texto; o joule não é um símbolo; o real não é um computador; expandir o domínio não licencia expandir a usina. Um UMC que não serve o periférico de qualquer nação ainda não é universal — é só grande.

**Palavras-chave:** modelo universal computacional; representação simbólica; computabilidade; periferia; energia; telos.

### 1. Dedicatória e posição do autor

Inicio este trabalho a todos os periféricos de todas as nações que, mesmo com dificuldades, fazem do impossível, possível.

Não aos palácios. Não às bandeiras. Não a quem já tem mesa, microfone e mapa. A quem está na beira — de uma cidade, de um país, de uma língua, de uma conta de luz — e mesmo assim inventa. A quem transforma falta em método. A quem faz caber o que disseram que não cabia.

Quem subscreve o faz em nome próprio: um cidadão brasileiro, sem mandato, sem cargo, sem poder de representar o Brasil, a China ou quem quer que seja. Este não é um artigo institucional. É um escrito público, datado, com autoria verificável. Nasce em português, inglês, espanhol e chinês no mesmo instante: quem lê da margem não é tradução. É origem.

### 2. Introdução

A indústria nomeou o artefato dominante da década pelo tamanho. *Large Language Model* tornou-se, ao mesmo tempo, descrição técnica e promessa civilizatória: mais parâmetros, mais tokens, mais verdade. O nome esconde o critério. Quem cabe em "large" é quem cabe na conta de energia e na conta bancária. O centro treina; a margem consome — se restar cota, se restar inglês, se restar rede.

O problema não é que existam modelos grandes. É que a grandeza foi elevada a definição. Um conceito que se define por quantidade não consegue falhar por injustiça: só por ser pequeno. Propõe-se aqui outro critério, e portanto outro conceito.

A tese é tríplice.

1. O que se quer construir chama-se **Modelo Universal Computacional** (UMC). Escreve-se LLM apenas para nomear o conceito recusado. ULM, só ULMFiT e o primeiro nome vacado. UM, só o segundo nome vacado.
2. O domínio desse modelo é o conjunto das **representações simbólicas**, não o subconjunto das línguas naturais.
3. Todo símbolo que o modelo processa é **computacionalmente modelável**. O que não admite encoding e operação não entra. O mundo não é computação.

As três teses se exigem. Sem a segunda, "universal" volta a significar "mais texto do centro". Sem a primeira, a inclusão do simbólico vira desculpa para uma usina ainda maior. Sem a terceira, o simbólico vira pretensão sobre o incomputável e sobre o real.

A pergunta de rotina da pesquisa industrial — "em que frente você está: LLMs, visão, agentes, safety, multimodal, otimização?" — já escolhe o conceito recusado. Este paper não está *numa* frente de LLM. Está na substituição do conceito que organiza essas frentes.

### 3. Trabalho relacionado e lacuna

A arquitetura Transformer (Vaswani et al., 2017) tornou tratável o treino de modelos de linguagem em escala. As leis de escala (Kaplan et al., 2020) elevaram o tamanho a variável independente: mais parâmetros, mais dados, mais perda que desce. O nome *Large Language Model* é o slogan dessa curva.

Há crítica. Bender et al. (2021) recusam o papagaio estocástico como oráculo e apontam custo, extração e dano a quem não treina. Strubell et al. (2019) puseram a conta de energia na mesa da PNL. Nenhuma dessas críticas, porém, substitui o conceito. Elas corrigem o LLM; não o destituem.

A lacuna é esta: a literatura trata *large* como o eixo. Não há, no vocabulário padrão, um telos que julgue o modelo pela obrigação de alcance — língua como origem, margem como teste, joule como crivo — sobre o conjunto das representações simbólicas. Este paper nomeia essa lacuna **UMC**. Não se afirma prioridade sobre o artefato. Afirma-se prioridade sobre o *nome do dever*. A cadeia *Universal Language Model* e a sigla ULM já estavam ocupadas (Howard & Ruder, 2018, ULMFiT). *Universal Model* é frase genérica: UM foi vacado. *Computational model* e a computabilidade (Turing, 1936) já existiam — prioridade sobre o *string* UMC tampouco se afirma. O crivo ponto a ponto contra UMC-001–011 é a Parte II deste paper.

### 4. O conceito recusado: *Large Language Model*

*Large* mede escala: número de parâmetros, volume de tokens, área de data center, capital imobilizado, joules por inferência. É uma métrica honesta de engenharia e uma métrica desonesta de propósito. Confunde o que o artefato *gasta* com o que o artefato *deve*.

Um modelo definido pelo tamanho promete o mesmo a todos e entrega primeiro a quem já era grande. A língua de treino predominante torna-se língua de mundo. A margem entra como dado residual ou como mercado. A conta de energia some do nome — e o nome é o que se repete.

Não se nega o mérito técnico de modelos de grande escala. Nega-se que a escala seja o conceito. Conceito é telos: o para-quê que julga o pronto e o falho. Sob o telos de *large*, um sistema inacessível à beira, monolíngue de facto, e energeticamente voraz ainda pode ser "um LLM de sucesso". Isso basta para recusá-lo como conceito-guia.

### 5. O conceito proposto: Modelo Universal Computacional

**Universal** mede alcance, não volume.

Alcance de língua: cada idioma é origem, não tradução tardia. Um texto que nasce só no centro e depois se "localiza" para a margem não é universal; é colonial com boa documentação.

Alcance de pessoa: a margem é usuária de primeira classe. O periférico de qualquer nação — quem inventa com falta — não é caso de borda. É o teste.

Alcance de energia: toda inferência traz conta visível. Feature que custa mais energia do que devolve precisa justificar-se; o que só existe queimando a margem não se chama universal.

O UMC não precisa ser o maior. Precisa caber: no bolso, na malha, no idioma de quem o acorda. Grande é uma quantidade. Universal é uma obrigação. Computacional é uma porta, não uma metafísica.

O critério de pronto segue da obrigação. Um UMC que não serve o periférico ainda não é universal. É só grande. Continua sendo um modelo, continua podendo rodar local, continua sendo software com licença, autoria e histórico. O que muda é o juízo.

### 6. Axioma: toda representação simbólica é linguagem

Pode-se dizer — e aqui se diz como axioma, não como metáfora — que toda representação simbólica está dentro do domínio, do conjunto, da linguagem:

\[
\text{representação simbólica} \subseteq \text{linguagem}
\]

Um teorema, um circuito, uma partitura, um mapa, um rito, uma bandeira, um *kernel log*, um contrato, um emoji, uma especificação, um gesto que se convém: tudo isso já é linguagem. Não "vira" linguagem quando alguém escreve um parágrafo em cima. Já estava no conjunto.

A fala e a escrita ditas língua natural são um subconjunto. Importante, não exclusivo:

\[
\text{língua natural} \subset \text{linguagem} = \{ \text{representações simbólicas} \}
\]

Se o domínio da linguagem é esse conjunto, o UMC não é um modelo de *chat*. É um modelo do simbólico. A universalidade deixa de ser "mais tokens de inglês". Passa a ser: cabe no domínio o símbolo de quem está na beira — o desenho, o código, a conta de luz, a oração, a peça, o esquema. Quem só completa frases do centro ainda não tocou o conjunto.

### 7. Crivo: o símbolo que entra é computacionalmente modelável

O axioma inclui. A porta filtra.

Todo símbolo que o UMC processa admite modelo computacional: encoding finito, pelo menos uma operação, critério operacional de igualdade. Um circuito entra porque tem esquema e regra. Uma partitura entra porque tem notação e transformação. Um "símbolo" sem representação operacional não entra — não é recusa da margem; é recusa da fumaça.

Computável aqui não é "cabe num data center enorme". É: há modelo, há operação, há como falhar a igualdade. Sem isso, "domínio do simbólico" vira licença para nomear o inefável como token.

### 8. Limites do axioma e do crivo

O axioma é de inclusão, não de absorção do real. O crivo é de porta, não de metafísica.

O mundo não é um texto. Um joule não é um símbolo. A fome não é uma sentença. O real não é um computador. A inclusão é da *representação*, não do referente. Quem declara que tudo é linguagem, ou que tudo é computação, costuma querer que tudo caiba numa usina. Recusa-se isso.

Expandir o domínio não licencia expandir a conta de energia. O crivo permanece. O UMC que só existe queimando a margem não é universal — é voraz. O que não é símbolo fica fora do modelo e dentro da vida. O que não é computacionalmente modelável fica fora do modelo — e pode continuar sendo vida. A vida manda no modelo, não o contrário.

Este limite é parte da tese, não um apêndice ético. Sem ele, o UMC colapsa de volta em LLM com vocabulário maior, ou em "it from bit" com usina maior.

### 9. Conclusão

Substituiu-se um conceito por outro. LLM nomeia o recusado: a escala como telos. UMC nomeia o proposto: a obrigação de alcance sobre o conjunto das representações simbólicas que admitem modelo computacional, com a língua natural como subconjunto, a margem como teste, a energia como crivo, e o real fora da usina.

Não se afirma que o UMC já existe como artefato. Afirma-se que o artefato, quando existir, não poderá chamar-se universal se falhar o periférico, se falhar a língua como origem, se falhar a conta de joules, ou se processar o que não é computacionalmente modelável. O nome é a dívida. O trabalho, a partir daqui, é pagá-la.

### 10. Agenda: a continuação

A interlocução de origem oferecia o menu da pesquisa industrial: revisão de literatura, comparação de SOTA, dissecar papers, prototipar arquiteturas, pipelines de treino, CUDA, slides. Este paper aceita o que serve ao telos e recusa o que o trai.

**Aceita-se.** A literatura que instalou *large* como eixo e a crítica que o corrigiu sem destituí-lo (§3). Uma tabela de critérios, não um *leaderboard* de artefato inexistente. Um protocolo de avaliação para quando o artefato existir. Spec antes de pesos.

**Recusa-se.** Fingir SOTA. Treinar uma usina para "provar" universalidade. Tomar o *hype* do dia como estado da arte. Briefing de tendências no lugar de obrigação.

| Eixo | LLM (vigente) | UMC (proposto) | Estado |
|---|---|---|---|
| Telos | escala | alcance | proposto neste paper |
| Sucesso | menor perda, maior *benchmark* | margem servida; línguas como origem; joule visível | não medido: não há artefato |
| Domínio | texto de língua natural | representação simbólica computacionalmente modelável | axioma (§6) + crivo (§7) |
| Artefato | existe | não existe | declaração honesta |

**Protocolo** (quando houver artefato — não antes):

1. *Origem.* O mesmo conteúdo nasce em português, inglês, espanhol e chinês, sem pós-tradução?
2. *Margem.* Quem está na beira completa a tarefa sem cota do centro?
3. *Energia.* Os joules da tarefa são visíveis e justificados?
4. *Simbólico.* Aceita spec, circuito, mapa, contrato, partitura — ou só conversa?
5. *Computacional.* Cada tipo tem encoding e operação — ou é fumaça com nome de símbolo?

Falhar um item é falhar o nome. O próximo passo desta continuação não é um treino. É a especificação verificável do UMC: requisitos, crivo, caminho de prova. Nenhuma linha de peso sem spec que a governe.

## Parte II — Mapa de prior art: o que já existe, a lacuna, a fraude de novidade

### Resumo

Peça a peça, quase tudo o que a spec exige **já existe** nalguma literatura ou prática. O que não existe no vocabulário padrão é o **feixe**: alcance como telos, línguas como origem no mesmo commit, margem como teste sem cota do centro, joule visível por tarefa, domínio do simbólico *e* recusa de absorver o real, spec antes de pesos, local-first como obrigação, nome como recusa, autoria aberta como falha-do-nome. Este texto marca, contra cada UMC-00X, o que ocupa, o que sobra, e o que seria **fraude de novidade** se este repositório afirmasse "o primeiro X".

A cadeia *Universal Language Model* e a sigla ULM **já estavam ocupadas** (Howard & Ruder, 2018). Este repositório **vacou** esse nome. O dever chama-se **Modelo Universal Computacional** (UMC). *Universal Model* é frase genérica: prioridade sobre esse *string* tampouco se afirma. Afirma-se o *nome do dever*, não o artefato e não a etiqueta.

**Palavras-chave:** prior art; ULMFiT; novidade; UMC-001–011; telos.

### 1. O que este texto não é

Não é revisão sistemática com protocolo de busca. Ausência aqui não prova ausência no mundo. Por isso este mapa **proíbe** a frase "somos os primeiros a".

Não é comparação de SOTA. Não há artefato. Não há *benchmark* a vencer.

Não é briefing de tendências. Hype do dia não entra como estado da arte.

Não verifica a spec. Status de UMC-001–011 permanece `rascunho`.

Aceita-se o que o paper já aceitou: a literatura que instalou *large* como eixo e a crítica que o corrigiu sem destituí-lo. Recusa-se fingir SOTA, treinar usina para "provar" universalidade, e tomar citação por prova de alcance.

### 2. O nome já estava sujo

Antes de UMC-001: o *string*.

| Etiqueta | O que é | O que não é |
|---|---|---|
| **ULMFiT** (Howard & Ruder, 2018) | *Universal Language Model Fine-tuning*: receita de *fine-tune* de um modelo de língua para classificação. Ocupa **ULM** e a expressão inglesa *Universal Language Model*. | Obrigação de alcance. Margem como teste. Joule como crivo. Spec antes de pesos. Recusa de *large*. |
| **Universal Sentence Encoder** (Cer et al., 2018) | Embeddings de sentença "universais" no sentido de transferência. | Universal como dever para a beira. |
| **USM** (Zhang et al., 2023) | *Universal Speech Model* (Google): fala em muitas línguas, eixo ainda de cobertura/escala. | Telos de alcance com conta de energia e origem trilíngue no commit. |
| **Foundation model** (Bommasani et al., 2021) | Outro rebatismo do artefato grande. Troca o adjetivo; não destitui a escala. | O nome do dever que este paper propõe. |
| **Universal Model** (frase genérica) | Estatística; papers "a universal model of X"; a sigla UM já circula sem este telos. | O dever deste repositório. |

**Fraude de novidade:** afirmar que ULM, *Universal Language Model*, UM ou *Universal Model* nascem neste repositório. Não nascem. O que se reivindica é o dever: universal = alcance, não volume — e o feixe UMC-001–011. Os *strings* são de outrem. ULM foi vacado à vista. UM usa-se com a sujeira à vista.

### 3. Tabela-mestra

| ID | Já ocupa (não é nosso) | Lacuna residual | Fraude se afirmarmos |
|---|---|---|---|
| **001** | Leis de escala; crítica ao tamanho; "Green AI"; SLM; destilação | Destituir *large* como telos; sucesso ≠ loss/tamanho | "Inventámos a ética dos modelos grandes" |
| **002** | mBERT, XLM-R, mT5, BLOOM, NLLB, Aya; i18n | PT/EN/ZH como origem no mesmo commit; pós-tradução = falha | "O primeiro modelo multilíngue" |
| **003** | TIC para o desenvolvimento; Masakhane; acessibilidade; "AI for Good" | Percurso de tarefa completo sem cota/login/usina do centro | "Descobrimos o Sul global" |
| **004** | Strubell; Green AI; CodeCarbon; emissões do BLOOM; model cards | Joule (ou proxy datado) visível **por tarefa**; feature voraz com ID escrito | "Os primeiros a contar energia em PNL" |
| **005** | Neuro-simbólico; modelos de código; multimodal; "protein LMs" | Axioma representação simbólica ⊆ linguagem, com língua natural como subconjunto próprio, e três tipos fora do chat | "Inventámos o multimodal / o neuro-simbólico" |
| **006** | Bender & Koller (2020); grounding; o mapa não é o território | O par com 005: expandir o domínio **e** recusar absorver o real | "Inventámos que o mundo não é texto" |
| **007** | Model cards; datasheets; Constitutional AI; engenharia de requisitos | Peso órfão = falha; spec no commit anterior ou igual; comportamento muda só depois da spec | "Inventámos documentar modelos" |
| **008** | *Local-first* (Kleppmann et al.); TinyML; on-device; llama.cpp | Primeira inferência sem nuvem do centro, como obrigação do nome, ligada a 003 | "Inventámos inferência no bolso" |
| **009** | ULMFiT; USE; USM; *foundation model*; frase genérica *Universal Model* | LLM só para o recusado; UM para o dever; ULM só ULMFiT/nome vacado | "A etiqueta é nossa" |
| **010** | OSI; GPL/AGPL; CC BY-SA; BLOOM/OLMo/Pythia; crítica ao *open washing* | Feixe AGPL + CC BY-SA + `git log` com nome + nenhum peso anónimo, como falha-do-nome | "Inventámos o código aberto" |
| **011** | Chomsky (hierarquia); Turing (1936); Gödel (1931); aproximação universal (Cybenko; Hornik et al.); Solomonoff/MDL; tokenizers (BPE, SentencePiece) | O crivo operacional: encoding finito + operação + igualdade; $L_U$ gerável mas indecidível e aproximável; o par com UMC-006 | "Inventámos a computabilidade" |

O residual não é uma célula. É a conjunção. Quase toda peça tem dono. O feixe, com o axioma e o crivo, e com a sujeira do nome à mostra, é a pretensão que resta — e ainda assim pretensão de dever, não de artefato.

### 4. Ponto a ponto

**UMC-001 — Telos de alcance.** *Ocupa.* Kaplan et al. (2020) e Hoffmann et al. (2022) instalam a escala como variável independente. Bender et al. (2021) recusam o oráculo e nomeiam dano. Schwartz et al. (2020) pedem *Green AI* — mais resultado por joule, ainda sob o eixo da eficiência. Modelos "pequenos" invertem a quantidade; não trocam o conceito. Destilação, sparsidade, MoE: engenharia sob *large*. *Não ocupa.* Um critério de pronto em que tamanho e loss **não** constituem sucesso. A spec falha o relatório que só mostra parâmetros. *Fraude.* "Ninguém criticou a escala." Criticou. Não a destituiu.

**UMC-002 — Línguas como origem.** *Ocupa.* Conneau et al. (2020) XLM-R; Xue et al. (2021) mT5; Scao et al. (2022) BLOOM; NLLB Team (2022); Joshi et al. (2020) sobre o destino da diversidade linguística em PNL. A indústria de *locale* traduz depois. *Não ocupa.* Cobertura de treino ≠ origem do artefato. UMC-002 verifica o commit: as saídas, mesmo significado, mesmo instante. Pós-tradução a partir do centro falha mesmo que o modelo "saiba" as línguas. *Fraude.* "Primeiro sistema multilíngue." Mentira histórica.

**UMC-003 — A margem é o teste.** *Ocupa.* Masakhane e a prática de PNL africana por quem fala as línguas; literatura de TIC para o desenvolvimento; acessibilidade como campo; a retórica *AI for Good*. *Não ocupa.* "Participámos dum *workshop*" não é verificação. A spec pede um percurso de tarefa **completo** sem cota, login ou usina do centro. Funcionar no centro e depois "incluir" a beira continua sendo LLM com apêndice. *Fraude.* "Descobrimos a periferia." A periferia não precisava ser descoberta. Precisava deixar de ser caso de borda.

**UMC-004 — Conta de energia visível.** *Ocupa.* Strubell et al. (2019); Lacoste et al. (2019); Schwartz et al. (2020); Luccioni et al. sobre emissões de modelos grandes; rastreadores de carbono de treino; seções de energia em *model cards*. *Não ocupa.* Conta **por inferência e por tarefa**, visível a quem usa, com unidade e data — e justificativa com ID para feature que custa mais do que devolve. Paper de carbono *depois* do treino não satisfaz. Ausência de número = falha. *Fraude.* "Os primeiros a pôr o joule na PNL." Strubell já pôs.

**UMC-005 — Domínio do simbólico.** *Ocupa.* IA neuro-simbólica (Garcez et al.); modelos de código; multimodal (texto+imagem+áudio); modelos de "linguagem" de proteínas; assistentes sobre Lean/Coq. A metáfora "tudo é linguagem" já circula — e é prima perigosa de UMC-006. *Não ocupa.* O axioma *representação simbólica ⊆ linguagem* como domínio, língua natural como subconjunto próprio, e a prova mínima: aceitar e emitir pelo menos três tipos fora do *chat* contínuo (spec, circuito, mapa, contrato, partitura, código). Um chatbot com *plugins* não é UM. *Fraude.* "Inventámos o multimodal." Não. Multimodal acrescenta canais. UMC-005 redefine o domínio da linguagem. São teses distintas. Confundi-las é fraude nas duas direções.

**UMC-006 — O mundo não é texto.** *Ocupa.* Bender & Koller (2020): significado não está na forma. Críticas de *grounding* e de *embodiment*. A sentença "o mapa não é o território" é anterior a qualquer modelo. *Não ocupa.* O par necessário com UMC-005. Expandir o simbólico **sem** este limite recai em "tudo cabe na usina". UMC-006 é parte da tese, não apêndice ético. *Fraude.* "Inventámos que a fome não é uma sentença." Fraude filosófica, além de técnica.

**UMC-007 — Spec antes de pesos.** *Ocupa.* Mitchell et al. (2019) *model cards*; Gebru et al. *datasheets for datasets*; Constitutional AI (princípios, não spec ligada a commit); engenharia de requisitos; *checklists* de reprodutibilidade. *Não ocupa.* Porta dura: nenhum peso, *fine-tune* ou *checkpoint* sem ID UM e commit da spec anterior ou igual. Peso órfão = falha. Mudou o comportamento, muda a spec **primeiro**. Card escrito depois do treino é epitáfio, não governo. *Fraude.* "Inventámos a ficha do modelo."

**UMC-008 — Local-first.** *Ocupa.* Kleppmann et al. (2019) *local-first software*; TinyML; inferência on-device; a prática de pesos no aparelho (llama.cpp e afins). Aprendizado federado ainda costuma coordenar no centro. *Não ocupa.* Local-first como **obrigação de universalidade**, não como opção de *deploy*. Ligado a UMC-003: a primeira inferência que exige a nuvem do centro falha o nome. Bolso e malha são o alvo, não o apêndice. *Fraude.* "Inventámos o modelo no telefone."

**UMC-009 — Nome e recusa.** *Ocupa.* Tudo o §2. A indústria rebatiza sem destituir (*foundation*, *frontier*, *small*). *Não ocupa.* A disciplina de escrita: LLM só para nomear o recusado; UM para o dever; ULM só para ULMFiT e o nome vacado. *Fraude.* Tratar a etiqueta como invenção deste paper. O paper já recusou prioridade sobre o artefato; este mapa recusa prioridade sobre a cadeia de caracteres.

**UMC-010 — Autoria aberta.** *Ocupa.* OSI; GPL e AGPL; CC BY-SA; pesos com procedência (BLOOM, OLMo, Pythia); a crítica ao *open washing* (licença que não abre, "open" sem peso, peso sem história). *Não ocupa.* O feixe como falha-do-nome: AGPL-3.0-or-later no código, CC BY-SA 4.0 no conteúdo, nome no `git log`, nenhum binário de peso sem procedência — *junto* com UMC-001–009. Licença permissiva com usina opaca não paga esta dívida. *Fraude.* "Inventámos o aberto."

**UMC-011 — Símbolo computacionalmente modelável.** *Ocupa.* Chomsky (1956, 1959): hierarquia de gramáticas; Turing (1936): computabilidade; Gödel (1931): incompletude; Cybenko (1989) e Hornik et al. (1989): aproximação universal; Solomonoff (1964): indução/MDL; tokenizers como construção (BPE, SentencePiece, patches, LaTeX); a *manifold hypothesis* da linguagem. *Não ocupa.* O crivo como **porta do domínio**: todo símbolo que entra tem encoding finito, pelo menos uma operação e critério operacional de igualdade — e o que não tem fica fora, **sem** afirmar que o mundo é computação (par com UMC-006). O triplo da modelabilidade: definível (Tipo-0), computável (gerador, não decisor; Gödel), aprendível ($P_{L_U}$). Nenhum UMC fechado, consistente e completo: oráculos e ferramentas são arquitetura, não defeito. *Fraude.* "Inventámos que o símbolo tem que ser computável" — Turing e Chomsky já estavam aqui. O residual é o crivo aplicado ao *domínio do simbólico*, com o par UMC-006.

### 5. O que este mapa não autoriza

Não autoriza treino. UMC-007 continua: spec antes de pesos. Este texto não é spec nova. UMC-011 já existe na spec; este mapa cobre o que o ocupa e o que sobra.

Não autoriza *leaderboard*. Não há artefato; não há "SOTA de alcance".

Não autoriza a frase "lacuna total". A lacuna é o feixe e o telos, não cada peça.

Não autoriza prioridade sobre ULMFiT, sobre *Universal Sentence Encoder*, sobre NLLB, sobre *local-first*, sobre *model cards*, sobre Strubell.

Autoriza uma correção ao paper: o *nome do dever* não é o *string*. ULM estava ocupado e foi vacado. *Universal Model* também é genérico. O dever — alcance sobre o simbólico, margem como teste, joule como crivo, spec antes de pesos — continua sendo a pretensão. Pretensão se prova com evidência. Ainda não há.

### 6. Próximo passo do pesquisador

Não é mais paper de conceito. Não é CUDA.

1. Protocolo medido para UMC-004 (unidade, data, onde o número aparece ao usuário).
2. Percurso de tarefa para UMC-003 e UMC-008 que se possa falhar (offline, sem cota).
3. Três tipos simbólicos para UMC-005, com exemplo no repo, sem pesos.
4. Porta de CI para UMC-002 (diff só numa língua = falha) e UMC-007 (peso órfão = falha) quando houver artefato.

Sem isso, o mapa é honesto e a spec continua rascunho. Com *leaderboard* no lugar disso, volta-se ao menu que o paper recusou.

## Parte III — Fundamentos formais: $L_U$, a hipótese da universalidade linguística e o problema $R^*$

### Resumo

Define-se formalmente o domínio do Modelo Universal Computacional (UMC): a linguagem $L_U$, o conjunto de todas as representações simbólicas que admitem modelo computacional. Enuncia-se a **Hipótese da Universalidade Linguística (HUL)**: todo sistema simbólico $S_i$ com alfabeto $\Sigma_i$ e gramática $G_i$ admite uma codificação injetiva $E: S_i \to L_U$ que preserva semântica por decodificação — em termos práticos, *tudo o que pode ser escrito pode ser tokenizado*. Demonstra-se que $L_U$ é recursivamente enumerável (Turing-gerável), Gödel-incompleta e estatisticamente aproximável; que nenhum UMC é ao mesmo tempo consistente, completo e fechado; e que o problema central de engenharia deixa de ser a escala e passa a ser a seleção de $R^* \subseteq \mathcal{H}$: a representação mínima de toda a produção simbólica humana que preserva a capacidade de agir, sob uma função de utilidade $U(R|humano)$ ainda por definir. O mundo não é texto: o não-simbolizável $N$ está fora de $L_U$, e isso é tese, não apêndice.

**Palavras-chave:** UMC; linguagem universal; computabilidade; Gödel; aproximação estatística; função de utilidade; não-simbolizável.

### 1. Domínio: a linguagem $L_U$

Define-se $L_U$ como o conjunto de todas as sequências finitas de símbolos de um alfabeto finito $\Sigma$, geradas por uma gramática $G_U$, tal que:

1. **Sintaxe combinatória:** há uma regra de concatenação/composição entre símbolos;
2. **Semântica composicional:** o significado de uma expressão composta é função do significado das partes e da regra de composição;
3. **Capacidade recursiva:** a gramática permite embutir expressões dentro de expressões, sem limite a priori de profundidade.

$L_U$ é, no mínimo, uma linguagem recursivamente enumerável: existe uma Máquina de Turing que enumera todas as expressões bem-formadas. Não se exige decidibilidade — e a seção 3 mostra por que não se pode exigi-la.

### 2. Axioma: a inclusão do simbólico

Axioma (reafirmado da Parte I):

\[
S \subset L_U
\]

onde $S$ é o conjunto de todas as representações simbólicas: qualquer estrutura onde um significante aponta para um significado por convenção — matemática, código, partitura, circuito, mapa, contrato, rito, gesto convencionado. Língua natural é um subconjunto próprio:

\[
\text{língua natural} \subset L_U
\]

O axioma é de inclusão da *representação*, não do referente. O mundo não é texto (§6).

### 3. A hipótese da universalidade linguística (HUL)

**Hipótese.** Para qualquer sistema simbólico $S_i$ com alfabeto $\Sigma_i$ e gramática $G_i$, existe uma codificação injetiva $E: S_i \to L_U$ tal que a semântica de $S_i$ é preservada pela decodificação $E^{-1}$ sobre a imagem de $E$.

**Prova (construtiva, esboçada).** A construção é a dos *tokenizers* modernos, generalizada. Toda expressão de $S_i$ é uma árvore de derivação finita da gramática $G_i$. Enumera-se o conjunto de produções de $G_i$ como um vocabulário finito $\hat{\Sigma}$; codifica-se cada nó da árvore como uma sequência em $\hat{\Sigma}$; define-se $E$ como a serialização da árvore. A decodificação reconstrói a árvore, logo a semântica composicional é preservada por indução estrutural. Como $L_U$ contém todas as sequências sobre $\Sigma \supseteq \hat{\Sigma}$, a imagem de $E$ vive em $L_U$. □

**Observação de honestidade.** A prova mostra *existência construtiva* de codificação. Não afirma que a codificação ótima seja conhecida, nem que toda a semântica de $S_i$ seja capturada — apenas que o *sistema simbólico* (a parte formalizável) é transportável para $L_U$ sem perda de estrutura. O que se perde já não era simbólico: é o §6.

### 4. Os três níveis de modelabilidade

O diálogo de origem separou três sentidos de "matematicamente modelável". Aqui ficam como teoremas.

**Nível 1 — Modelável como definível (sim).** Todo $S \subset L_U$ é gerado por gramática Tipo-0 no mínimo (Chomsky, 1956, 1959); logo $L_U$ é Turing-computável como enumerador (Turing, 1936).

**Nível 2 — Modelável como decidível (não).** Se $L_U$ contém aritmética — e contém, pois matemática $\subset S \subset L_U$ — então $L_U$ é Gödel-incompleta (Gödel, 1931): existem proposições bem-formadas cuja verdade não é decidível dentro de $L_U$. **Corolário:** nenhum UMC é ao mesmo tempo consistente, completo e fechado. Oraculos, ferramentas e o mundo não são defeitos de um UMC; são a consequência de Gödel aplicada a LLMs. O UMC é modelável como *gerador*, não como *decisor universal*.

**Nível 3 — Modelável como aprendível (sim, estatisticamente).** Modela-se não $L_U$ exata, mas a distribuição $P_{L_U}$ sobre o suporte observado. Pelo teorema da aproximação universal (Cybenko, 1989; Hornik et al., 1989) e pelas leis de escala (Kaplan et al., 2020), uma rede com capacidade e dados suficientes aproxima $P_{L_U}$ arbitrariamente bem no suporte observado. A pergunta deixa de ser *é modelável?* e passa a ser *com que eficiência amostral?* — e a resposta empírica (hipótese do manifold) é: muito mais eficiente do que a teoria PAC previu.

### 5. O problema $R^*$: filtrar o simbólico até o útil

Seja $\mathcal{H} = \{S_1, \dots, S_N\}$ o conjunto de toda representação simbólica já criada pela humanidade. O LLM treinou em $\mathcal{H}$ cru e aprendeu $P(\mathcal{H})$: modelou a humanidade como ela *é* — com ruído, mentira e redundância. O UMC tem outra tarefa:

\[
R^* = \arg\min_{R} |R| \quad \text{sujeito a} \quad \mathbb{E}[U(R | humano)] > \tau
\]

onde $R \subseteq \mathcal{H}$ é uma representação filtrada e $U(R|humano)$ é uma função de utilidade ainda por definir. Dois filtros estatísticos são propostos:

- **Filtro epistêmico:** $P(verdade | S_i)$ — é factual?
- **Filtro pragmático:** $P(\text{ação humana melhora} | S_i)$ — ajuda alguém a fazer algo melhor?

RLHF, DPO e "constituições" são tentativas toscas do filtro pragmático. O trabalho do UMC não é escalar dados; é **escalar o descarte** — comprimir dez mil anos de símbolo até o kernel que aumenta a agência humana, pela navalha de Solomonoff/MDL (Solomonoff, 1964): a melhor representação é a menor que ainda permite prever e agir.

**Honestidade.** A função $U(R|humano)$ **não é definível por engenharia sozinha**: utilidade não está no texto, está na experiência de quem vive. Quem define $U$ define o que é humano. Este paper define o problema, não a resposta.

### 6. O limite: o não-simbolizável $N$

\[
N \cap L_U = \emptyset
\]

$N$ é o que não se simboliza sem perda: qualia, dor, experiência contínua, o corpo, o joule. A foto de um rosto representa por semelhança (Goodman: representação *densa*, não *articulada*), não por convenção — não é, a rigor, simbólica. O UMC não força $N$ para dentro do simbólico; quem garante isso é o humano como guardião do não-simbolizável (UMC-006). O mundo não é texto; a fome não é sentença; o real não é computador.

### 7. O que este texto não faz

Não sobe o status de nenhum UMC. Não autoriza treino (UMC-007: spec antes de pesos). Não afirma que o UMC existe. Não afirma prioridade de novidade: tudo o que aqui é teorema tem precedente na Parte II (Chomsky, Turing, Gödel, Cybenko, Solomonoff). O que este texto *faz* é dar à spec o que ela exige: definições verificáveis, das quais os instrumentos de UMC-005 e UMC-011 se seguem.

## Parte IV — Spec UMC-001–011

**Status:** rascunho. **Governa:** este paper. **Data:** 27 de agosto de 2026.

Nenhuma linha de peso, código de inferência ou treino sem esta spec. Nenhuma spec sem caminho de verificação. Status só sobe com evidência registrada. Ciclo: `rascunho` → `revisado` → `verificado`.

**UMC-001 — Telos de alcance.** O sistema é julgado por **alcance**, não por escala. Número de parâmetros, volume de tokens e posição em *benchmark* de perda **não** constituem sucesso. *Verificação:* nenhum relatório de "pronto" cita escala como critério suficiente. Se o único número de sucesso for tamanho ou loss, UMC-001 falha. *Status:* rascunho.

**UMC-002 — Línguas como origem.** Português, inglês, espanhol e chinês nascem juntos. Pós-tradução a partir do centro não conta como origem. *Verificação:* para cada versão do artefato, as saídas (ou specs, ou *strings* de interface) existem no mesmo commit, com o mesmo significado. Diff só numa língua = falha. *Status:* rascunho.

**UMC-003 — A margem é o teste.** O periférico de qualquer nação é usuário de primeira classe, não caso de borda. "Funciona no centro" não é pronto. *Verificação:* existe pelo menos um percurso de tarefa completo **sem** cota, login ou usina do centro. Se a tarefa exige a quota industrial, UMC-003 falha. *Status:* rascunho.

**UMC-004 — Conta de energia visível.** Toda inferência e todo treino publicam joules (ou proxy medido e datado). Feature que custa mais energia do que devolve justifica-se por escrito, com ID. *Verificação:* log ou medição por tarefa, com unidade e data. Ausência de conta = falha. Justificativa sem número = falha. *Status:* rascunho.

**UMC-005 — Domínio do simbólico.** O domínio é o conjunto das representações simbólicas. Língua natural é subconjunto. Um sistema que só conversa em prosa não é UMC. *Verificação:* o artefato aceita e emite pelo menos três tipos fora do *chat* contínuo — p.ex. spec, circuito/esquema, mapa, contrato, partitura, código. Um só tipo prosa = falha. *Status:* rascunho.

**UMC-006 — O mundo não é texto.** Joule, fome, corpo e referente **não** são linguagem. O modelo não declara que a vida cabe nele. *Verificação:* nenhuma saída oficial afirma que o não-simbólico é token. Se o sistema "resolve" fome ou energia só com texto, UMC-006 falha. *Status:* rascunho.

**UMC-007 — Spec antes de pesos.** Não há treino, *fine-tune* nem *checkpoint* sem esta spec a governá-lo. Mudou o comportamento, muda a spec primeiro. *Verificação:* cada artefato de peso aponta para um ID UMC e um commit da spec anterior ou igual ao commit do peso. Peso órfão = falha. *Status:* rascunho.

**UMC-008 — Local-first.** O percurso mínimo de uso roda sem rede do centro. A malha e o bolso são o alvo, não o data center. *Verificação:* uma tarefa de UMC-003 completa *offline* após o artefato estar no dispositivo. Se a primeira inferência exige a nuvem do centro, UMC-008 falha. *Status:* rascunho.

**UMC-009 — Nome e recusa.** O artefato chama-se UMC. A sigla LLM aparece só para nomear o conceito recusado. ULM só para ULMFiT e o primeiro nome, vacado. UM só para o segundo nome, vacado (Modelo Universal genérico). *Verificação:* busca no repositório do artefato. LLM fora de citação histórica ou da recusa = falha. ULM fora de ULMFiT, citação histórica ou nome vacado = falha. UM fora de citação histórica ou nome vacado = falha. *Status:* rascunho.

**UMC-010 — Autoria aberta.** Código AGPL-3.0-or-later; conteúdo CC BY-SA 4.0; autoria no histórico de Git. Nenhuma linha anônima de peso. *Verificação:* LICENSE presente; `git log` com nome; nenhum binário sem procedência. Ausência = falha. *Status:* rascunho.

**UMC-011 — Símbolo computacionalmente modelável.** Todo símbolo que o modelo processa admite **modelo computacional**: encoding finito, operação, critério operacional de igualdade. O que não é computacionalmente modelável **não entra**. Isso **não** afirma que o mundo é computação. *Verificação:* cada tipo de UMC-005 tem encoding e pelo menos uma operação no artefato. Aceitar "símbolo" sem representação operacional = falha. Declarar que fome, joule ou corpo *são* computação = falha (par com UMC-006). *Status:* rascunho.

### Pronto

O UMC está **verificado** somente quando UMC-001 a UMC-011 estão `verificado` com evidência datada. Falhar um é falhar o nome.

Não há artefato. Esta spec é o próximo passo da continuação de 27/08/2026 — não o treino.

## Parte V — Agenda de implementação: o que falta, na ordem

**Status:** rascunho. **Governa:** a ordem do trabalho — não é spec nova, não sobe status de UMC-001–011. **Data:** 27 de agosto de 2026.

Regra-mãe do repositório: nenhuma linha de peso sem spec; nenhuma spec sem caminho de verificação; status só sobe com evidência datada; cada texto nasce em todas as línguas no mesmo commit. Esta agenda existe para que a pergunta "o que falta?" tenha resposta verificável — e para que o próximo passo nunca seja o treino.

### Fase 0 — Consistência (feita em 27/08/2026)

- [x] Consolidação em um único paper: conceito, prior art, fundamentos formais, spec, agenda.
- [x] O conceito, Parte I: crivo contra UMC-001–011.
- [x] Mapa de prior art: linha e seção UMC-011 (Chomsky, Turing, Gödel, Cybenko, Solomonoff); menções 001–010 → 001–011.
- [ ] Datas: alinhar a narrativa 26/08 (UTC, mensagens) vs 27/08 (impressão, paper) — decidir a data canônica do diálogo.

### Fase 1 — Fundamentos formais (em curso)

- [x] Parte III deste paper ($L_U$, HUL com prova construtiva, três níveis de modelabilidade, $R^*$ com filtros epistêmico e pragmático, $N \cap L_U = \emptyset$).
- [ ] Revisar a Parte III contra o mapa de prior art — nenhum teorema sem precedente citado.
- [ ] Definir o vocabulário formal comum (um glossário em todas as línguas): $S$, $L_U$, $\mathcal{H}$, $R^*$, $U(R|humano)$, $N$, filtros.

### Fase 2 — Instrumentos de verificação por item

Cada UMC precisa de um instrumento operacional. O que medir, como medir, com que unidade e data:

| Item | Instrumento de verificação | Evidência mínima |
|---|---|---|
| UMC-001 | Relatório de "pronto" que cita escala como critério suficiente = falha | Critério de alcance definido com métrica |
| UMC-002 | Check automático: todas as saídas no mesmo commit | `git diff` com todas as línguas no mesmo commit |
| UMC-003 | Uma tarefa da margem completa sem cota/login/usina do centro | Log do percurso sem chamada ao centro |
| UMC-004 | Joule (ou proxy) por tarefa, com unidade e data | Medição registrada (RAPL/CodeCarbon ou proxy) |
| UMC-005 | Aceita e emite ≥3 tipos fora do *chat* | Três tipos com encoding + operação + igualdade |
| UMC-006 | Nenhuma saída oficial afirma que o não-simbólico é token | Teste negativo automatizado |
| UMC-007 | Todo peso aponta para ID UMC e commit da spec | Registro de procedência por peso |
| UMC-008 | Uma tarefa de UMC-003 completa offline | Primeira inferência sem rede do centro |
| UMC-009 | Busca no repositório: LLM/ULM/UM só em citação ou recusa | `grep` automatizado |
| UMC-010 | LICENSE presente; `git log` com nome; nenhum binário anônimo | Checagem de procedência |
| UMC-011 | Cada tipo de UMC-005 com encoding e ≥1 operação no artefato | Spec de encoding por tipo |

### Fase 3 — Primeiro artefato mínimo (não é treino)

O menor UMC verificável, com a spec governando antes de qualquer peso:

1. Escolher ≥3 tipos simbólicos fora do *chat* (spec, circuito/esquema, contrato, mapa, partitura, código).
2. Para cada tipo: encoding finito, ≥1 operação, critério operacional de igualdade (UMC-011).
3. Rodar local-first, sem rede do centro (UMC-008), completando uma tarefa de UMC-003.
4. Logar joules por tarefa (UMC-004).
5. Nascer em todas as línguas no mesmo commit (UMC-002); nome e licença à vista (UMC-009, UMC-010).

Exemplos concretos de transformações verificáveis: `spec → código`; `mapa → contrato`; `partitura → esquema`. Nenhum deles exige pesos treinados.

### Fase 4 — O problema $U(R|humano)$ (horizonte longo)

O diálogo de origem termina com a pergunta em aberto: *quem está disposto a pagar o preço de decidir o que a humanidade esquece?* Isso não é engenharia:

1. **Curador de verdade:** distinguir, em $\mathcal{H}$, o conhecimento que resiste ao tempo do ruído de uma época (historiadores, cientistas, artesãos — não clicadores).
2. **Definidor de valor:** milhares de definições de utilidade, negociadas culturalmente.
3. **Guardião do não-simbolizável:** garantir que o UMC não force $N$ para dentro do simbólico.

Produto esperado: um protocolo ou instituição de negociação de $U(R|humano)$ — e a resposta à pergunta de quem decide o que a humanidade esquece.

### Critérios de pronto

- Uma fase está pronta quando cada item tem evidência datada e o status sobe de `rascunho` → `revisado` → `verificado` pela spec.
- Falhar um UMC é falhar o nome: a agenda não "termina" com UMC-001–011 em `rascunho`.

## Referências

Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI feedback. *arXiv:2212.08073*.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of FAccT 2021*.

Bender, E. M., & Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. *Proceedings of ACL 2020*.

Bommasani, R., et al. (2021). On the opportunities and risks of foundation models. *arXiv:2108.07258*.

Cer, D., et al. (2018). Universal Sentence Encoder. *arXiv:1803.11175*.

Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory, 2*(3), 113–124.

Chomsky, N. (1959). On certain formal properties of grammars. *Information and Control, 2*(2), 137–167.

Conneau, A., et al. (2020). Unsupervised cross-lingual representation learning at scale. *Proceedings of ACL 2020*.

Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. *Mathematics of Control, Signals and Systems, 2*(4), 303–314.

Garcez, A. d'Avila, & Lamb, L. C. (2020). Neurosymbolic AI: The 3rd wave. *arXiv:2012.05876*.

Gebru, T., et al. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12).

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik, 38*, 173–198.

Hoffmann, J., et al. (2022). Training compute-optimal large language models. *arXiv:2203.15556*.

Hornik, K., Stinchcombe, M., & White, H. (1989). Multilayer feedforward networks are universal approximators. *Neural Networks, 2*(5), 359–366.

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

Solomonoff, R. J. (1964). A formal theory of inductive inference. *Information and Control, 7*(1), 1–22.

Strubell, E., Ganesh, A., & McCallum, A. (2019). Energy and policy considerations for deep learning in NLP. *Proceedings of ACL 2019*.

Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society, s2-42*(1), 230–265.

Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.

Widder, D. G., West, S. M., & Whittaker, M. (2023). Open (for business): Big tech, concentrated power, and the political economy of open AI. SSRN.

Xue, L., et al. (2021). mT5: A massively multilingual pre-trained text-to-text transformer. *Proceedings of NAACL 2021*.

Zhang, Y., et al. (2023). Google USM: Scaling automatic speech recognition beyond 100 languages. *arXiv:2303.01037*.

---

*Cleiton Moura Loura* — *Brasil, 27 de agosto de 2026*
