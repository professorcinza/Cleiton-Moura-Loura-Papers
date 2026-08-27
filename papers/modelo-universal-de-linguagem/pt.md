# O Modelo Universal de Linguagem: do telos da escala ao domínio do simbólico

**Cleiton Moura Loura**  
Iniciativa pessoal, sem afiliação institucional. Cidadão brasileiro.  
Brasil, 27 de agosto de 2026.

*Idiomas:* [Português](pt.md) · [English](en.md) · [中文](zh.md)

**Como citar:** Loura, C. M. (2026). *O Modelo Universal de Linguagem: do telos da escala ao domínio do simbólico*. Cleiton-Moura-Loura-Papers. https://github.com/professorcinza/Cleiton-Moura-Loura-Papers

**Licença:** CC BY-SA 4.0.

**Proveniência.** Este artigo é a continuação, em público e com nome, de um diálogo de pesquisa de 27 de agosto de 2026. A interlocução industrial perguntou em que frente de LLM se trabalhava. A resposta — substituir *Large Language Model* por *Universal Language Model* — é o objeto daqui. O print dessa interlocução não se arquiva neste repositório (produto de terceiro). O trabalho, sim.

---

## Resumo

Este paper substitui o conceito de *Large Language Model* (LLM) pelo de **Modelo Universal de Linguagem** (ULM). A substituição não é nominal: troca o telos. *Large* nomeia escala — parâmetros, capital, joules — e entrega primeiro a quem já era grande. *Universal* nomeia obrigação de alcance: toda língua como origem, toda margem como usuária de primeira classe, toda inferência com conta de energia visível. Funda-se um axioma: **toda representação simbólica está no conjunto da linguagem** (representação simbólica ⊆ linguagem). A língua natural é subconjunto, não o domínio. O ULM, portanto, não é um modelo de conversa: é um modelo do simbólico. O mundo, porém, não é um texto; o joule não é um símbolo; expandir o domínio não licencia expandir a usina. Um ULM que não serve o periférico de qualquer nação ainda não é universal — é só grande.

**Palavras-chave:** modelo universal de linguagem; representação simbólica; periferia; energia; telos.

---

## 1. Dedicatória e posição do autor

Inicio este trabalho a todos os periféricos de todas as nações que, mesmo com dificuldades, fazem do impossível, possível.

Não aos palácios. Não às bandeiras. Não a quem já tem mesa, microfone e mapa. A quem está na beira — de uma cidade, de um país, de uma língua, de uma conta de luz — e mesmo assim inventa. A quem transforma falta em método. A quem faz caber o que disseram que não cabia.

Quem subscreve o faz em nome próprio: um cidadão brasileiro, sem mandato, sem cargo, sem poder de representar o Brasil, a China ou quem quer que seja. Este não é um artigo institucional. É um escrito público, datado, com autoria verificável. Nasce em português, inglês e chinês no mesmo instante: quem lê da margem não é tradução. É origem.

## 2. Introdução

A indústria nomeou o artefato dominante da década pelo tamanho. *Large Language Model* tornou-se, ao mesmo tempo, descrição técnica e promessa civilizatória: mais parâmetros, mais tokens, mais verdade. O nome esconde o critério. Quem cabe em “large” é quem cabe na conta de energia e na conta bancária. O centro treina; a margem consome — se restar cota, se restar inglês, se restar rede.

O problema não é que existam modelos grandes. É que a grandeza foi elevada a definição. Um conceito que se define por quantidade não consegue falhar por injustiça: só por ser pequeno. Propõe-se aqui outro critério, e portanto outro conceito.

A tese é dupla.

1. O que se quer construir chama-se **Modelo Universal de Linguagem** (ULM). Escreve-se LLM apenas para nomear o conceito recusado.
2. O domínio desse modelo é o conjunto das **representações simbólicas**, não o subconjunto das línguas naturais.

As duas teses se exigem. Sem a segunda, “universal” volta a significar “mais texto do centro”. Sem a primeira, a inclusão do simbólico vira desculpa para uma usina ainda maior.

A pergunta de rotina da pesquisa industrial — “em que frente você está: LLMs, visão, agentes, safety, multimodal, otimização?” — já escolhe o conceito recusado. Este paper não está *numa* frente de LLM. Está na substituição do conceito que organiza essas frentes.

## 3. Trabalho relacionado e lacuna

A arquitetura Transformer (Vaswani et al., 2017) tornou tratável o treino de modelos de linguagem em escala. As leis de escala (Kaplan et al., 2020) elevaram o tamanho a variável independente: mais parâmetros, mais dados, mais perda que desce. O nome *Large Language Model* é o slogan dessa curva.

Há crítica. Bender et al. (2021) recusam o papagaio estocástico como oráculo e apontam custo, extração e dano a quem não treina. Strubell et al. (2019) puseram a conta de energia na mesa da PNL. Nenhuma dessas críticas, porém, substitui o conceito. Elas corrigem o LLM; não o destituem.

A lacuna é esta: a literatura trata *large* como o eixo. Não há, no vocabulário padrão, um telos que julgue o modelo pela obrigação de alcance — língua como origem, margem como teste, joule como crivo — sobre o conjunto das representações simbólicas. Este paper nomeia essa lacuna **ULM**. Não se afirma prioridade sobre o artefato. Afirma-se prioridade sobre o *nome do dever*. A cadeia de caracteres *Universal Language Model* e a sigla ULM já estavam ocupadas (Howard & Ruder, 2018, ULMFiT). Prioridade sobre o *string* seria fraude. O crivo ponto a ponto contra ULM-001–010 está no [mapa de prior art](../ulm-prior-art/pt.md).

## 4. O conceito recusado: *Large Language Model*

*Large* mede escala: número de parâmetros, volume de tokens, área de data center, capital imobilizado, joules por inferência. É uma métrica honesta de engenharia e uma métrica desonesta de propósito. Confunde o que o artefato *gasta* com o que o artefato *deve*.

Um modelo definido pelo tamanho promete o mesmo a todos e entrega primeiro a quem já era grande. A língua de treino predominante torna-se língua de mundo. A margem entra como dado residual ou como mercado. A conta de energia some do nome — e o nome é o que se repete.

Não se nega o mérito técnico de modelos de grande escala. Nega-se que a escala seja o conceito. Conceito é telos: o para-quê que julga o pronto e o falho. Sob o telos de *large*, um sistema inacessível à beira, monolíngue de facto, e energeticamente voraz ainda pode ser “um LLM de sucesso”. Isso basta para recusá-lo como conceito-guia.

## 5. O conceito proposto: Modelo Universal de Linguagem

**Universal** mede alcance, não volume.

Alcance de língua: cada idioma é origem, não tradução tardia. Um texto que nasce só no centro e depois se “localiza” para a margem não é universal; é colonial com boa documentação.

Alcance de pessoa: a margem é usuária de primeira classe. O periférico de qualquer nação — quem inventa com falta — não é caso de borda. É o teste.

Alcance de energia: toda inferência traz conta visível. Feature que custa mais energia do que devolve precisa justificar-se; o que só existe queimando a margem não se chama universal.

O ULM não precisa ser o maior. Precisa caber: no bolso, na malha, no idioma de quem o acorda. Grande é uma quantidade. Universal é uma obrigação.

O critério de pronto segue da obrigação. Um ULM que não serve o periférico ainda não é universal. É só grande. Continua sendo um modelo de linguagem, continua podendo rodar local, continua sendo software com licença, autoria e histórico. O que muda é o juízo.

## 6. Axioma: toda representação simbólica é linguagem

Pode-se dizer — e aqui se diz como axioma, não como metáfora — que toda representação simbólica está dentro do domínio, do conjunto, da linguagem:

\[
\text{representação simbólica} \subseteq \text{linguagem}
\]

Um teorema, um circuito, uma partitura, um mapa, um rito, uma bandeira, um *kernel log*, um contrato, um emoji, uma especificação, um gesto que se convém: tudo isso já é linguagem. Não “vira” linguagem quando alguém escreve um parágrafo em cima. Já estava no conjunto.

A fala e a escrita ditas língua natural são um subconjunto. Importante, não exclusivo:

\[
\text{língua natural} \subset \text{linguagem} = \{ \text{representações simbólicas} \}
\]

Se o domínio da linguagem é esse conjunto, o ULM não é um modelo de *chat*. É um modelo do simbólico. A universalidade deixa de ser “mais tokens de inglês”. Passa a ser: cabe no domínio o símbolo de quem está na beira — o desenho, o código, a conta de luz, a oração, a peça, o esquema. Quem só completa frases do centro ainda não tocou o conjunto.

## 7. Limites do axioma

O axioma é de inclusão, não de absorção do real.

O mundo não é um texto. Um joule não é um símbolo. A fome não é uma sentença. A inclusão é da *representação*, não do referente. Quem declara que tudo é linguagem costuma querer que tudo caiba numa usina. Recusa-se isso.

Expandir o domínio não licencia expandir a conta de energia. O crivo permanece. O ULM que só existe queimando a margem não é universal — é voraz. O que não é símbolo fica fora do modelo e dentro da vida. A vida manda no modelo, não o contrário.

Este limite é parte da tese, não um apêndice ético. Sem ele, o ULM colapsa de volta em LLM com vocabulário maior.

## 8. Conclusão

Substituiu-se um conceito por outro. LLM nomeia o recusado: a escala como telos. ULM nomeia o proposto: a obrigação de alcance sobre o conjunto das representações simbólicas, com a língua natural como subconjunto, a margem como teste, e a energia como crivo.

Não se afirma que o ULM já existe como artefato. Afirma-se que o artefato, quando existir, não poderá chamar-se universal se falhar o periférico, se falhar a língua como origem, ou se falhar a conta de joules. O nome é a dívida. O trabalho, a partir daqui, é pagá-la.

## 9. Agenda: a continuação

A interlocução de origem oferecia o menu da pesquisa industrial: revisão de literatura, comparação de SOTA, dissecar papers, prototipar arquiteturas, pipelines de treino, CUDA, slides. Este paper aceita o que serve ao telos e recusa o que o trai.

**Aceita-se.** A literatura que instalou *large* como eixo e a crítica que o corrigiu sem destituí-lo (§3). Uma tabela de critérios, não um *leaderboard* de artefato inexistente. Um protocolo de avaliação para quando o artefato existir. Spec antes de pesos.

**Recusa-se.** Fingir SOTA. Treinar uma usina para “provar” universalidade. Tomar o *hype* do dia como estado da arte. Briefing de tendências no lugar de obrigação.

| Eixo | LLM (vigente) | ULM (proposto) | Estado |
|---|---|---|---|
| Telos | escala | alcance | proposto neste paper |
| Sucesso | menor perda, maior *benchmark* | margem servida; línguas como origem; joule visível | não medido: não há artefato |
| Domínio | texto de língua natural | representação simbólica | axioma (§6) |
| Artefato | existe | não existe | declaração honesta |

**Protocolo** (quando houver artefato — não antes):

1. *Origem.* O mesmo conteúdo nasce em português, inglês e chinês, sem pós-tradução?
2. *Margem.* Quem está na beira completa a tarefa sem cota do centro?
3. *Energia.* Os joules da tarefa são visíveis e justificados?
4. *Simbólico.* Aceita spec, circuito, mapa, contrato — ou só conversa?

Falhar um item é falhar o nome. O próximo passo desta continuação não é um treino. É a especificação verificável do ULM: requisitos, crivo, caminho de prova. Nenhuma linha de peso sem spec que a governe.

## Referências

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of FAccT 2021*.

Howard, J., & Ruder, S. (2018). Universal Language Model Fine-tuning for text classification. *Proceedings of ACL 2018*.

Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). Scaling laws for neural language models. *arXiv:2001.08361*.

Strubell, E., Ganesh, A., & McCallum, A. (2019). Energy and policy considerations for deep learning in NLP. *Proceedings of ACL 2019*.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.

---

*Cleiton Moura Loura*  
*Brasil, 27 de agosto de 2026*
