# Spec UM — Modelo Universal

**Cleiton-Moura-Loura-Papers · spec/um · v1 · status: rascunho**  
**Governa:** o paper [O Modelo Universal](../../papers/modelo-universal/pt.md)  
**Data:** 27 de agosto de 2026  
**Idiomas:** [Português](pt.md) · [English](en.md) · [中文](zh.md)

Nenhuma linha de peso, código de inferência ou treino sem esta spec. Nenhuma spec sem caminho de verificação. Status só sobe com evidência registrada.

Ciclo: `rascunho` → `revisado` → `verificado`.

---

## UM-001 — Telos de alcance

O sistema é julgado por **alcance**, não por escala. Número de parâmetros, volume de tokens e posição em *benchmark* de perda **não** constituem sucesso.

**Verificação:** nenhum relatório de “pronto” cita escala como critério suficiente. Se o único número de sucesso for tamanho ou loss, UM-001 falha.

**Status:** rascunho.

## UM-002 — Línguas como origem

Português, inglês e chinês nascem juntos. Pós-tradução a partir do centro não conta como origem.

**Verificação:** para cada versão do artefato, as três saídas (ou specs, ou *strings* de interface) existem no mesmo commit, com o mesmo significado. Diff só numa língua = falha.

**Status:** rascunho.

## UM-003 — A margem é o teste

O periférico de qualquer nação é usuário de primeira classe, não caso de borda. “Funciona no centro” não é pronto.

**Verificação:** existe pelo menos um percurso de tarefa completo **sem** cota, login ou usina do centro. Se a tarefa exige a quota industrial, UM-003 falha.

**Status:** rascunho.

## UM-004 — Conta de energia visível

Toda inferência e todo treino publicam joules (ou proxy medido e datado). Feature que custa mais energia do que devolve justifica-se por escrito, com ID.

**Verificação:** log ou medição por tarefa, com unidade e data. Ausência de conta = falha. Justificativa sem número = falha.

**Status:** rascunho.

## UM-005 — Domínio do simbólico

O domínio é o conjunto das representações simbólicas. Língua natural é subconjunto. Um sistema que só conversa em prosa não é UM.

**Verificação:** o artefato aceita e emite pelo menos três tipos fora do *chat* contínuo — p.ex. spec, circuito/esquema, mapa, contrato, partitura, código. Um só tipo prosa = falha.

**Status:** rascunho.

## UM-006 — O mundo não é texto

Joule, fome, corpo e referente **não** são linguagem. O modelo não declara que a vida cabe nele.

**Verificação:** nenhuma saída oficial afirma que o não-simbólico é token. Se o sistema “resolve” fome ou energia só com texto, UM-006 falha.

**Status:** rascunho.

## UM-007 — Spec antes de pesos

Não há treino, *fine-tune* nem *checkpoint* sem esta spec a governá-lo. Mudou o comportamento, muda a spec primeiro.

**Verificação:** cada artefato de peso aponta para um ID UM e um commit da spec anterior ou igual ao commit do peso. Peso órfão = falha.

**Status:** rascunho.

## UM-008 — Local-first

O percurso mínimo de uso roda sem rede do centro. A malha e o bolso são o alvo, não o data center.

**Verificação:** uma tarefa de UM-003 completa *offline* após o artefato estar no dispositivo. Se a primeira inferência exige a nuvem do centro, UM-008 falha.

**Status:** rascunho.

## UM-009 — Nome e recusa

O artefato chama-se UM. A sigla LLM aparece só para nomear o conceito recusado. A sigla ULM aparece só para ULMFiT e para o primeiro nome, vacado.

**Verificação:** busca no repositório do artefato. LLM fora de citação histórica ou da recusa = falha. ULM fora de ULMFiT, citação histórica ou nome vacado = falha.

**Status:** rascunho.

## UM-010 — Autoria aberta

Código AGPL-3.0-or-later; conteúdo CC BY-SA 4.0; autoria no histórico de Git. Nenhuma linha anônima de peso.

**Verificação:** LICENSE presente; `git log` com nome; nenhum binário sem procedência. Ausência = falha.

**Status:** rascunho.

---

## Pronto

O UM está **verificado** somente quando UM-001 a UM-010 estão `verificado` com evidência datada. Falhar um é falhar o nome.

Não há artefato. Esta spec é o próximo passo da continuação de 27/08/2026 — não o treino.

Prior art contra UM-001–010: [mapa](../../papers/um-prior-art/pt.md). O mapa não sobe o status desta spec.

---

*Cleiton Moura Loura*  
*Brasil, 27 de agosto de 2026*
