# El Modelo Universal Computacional (UMC): del telos de la escala al dominio de lo simbólico

**Cleiton Moura Loura**  
Iniciativa personal, sin afiliación institucional. Ciudadano brasileño.  
Brasil, 27 de agosto de 2026.

*Languages / Idiomas / Idiomas / 语言:* [English](paper-umc.en.md) · [Português](paper-umc.pt.md) · [Español](paper-umc.es.md) · [中文](paper-umc.zh.md)

**Cómo citar:** Loura, C. M. (2026). *El Modelo Universal Computacional (UMC)*. Cleiton-Moura-Loura-Papers. https://github.com/professorcinza/Cleiton-Moura-Loura-Papers

**Licencia:** CC BY-SA 4.0.

**Proveniencia.** Este artículo es la continuación, en público y con nombre, de un diálogo de investigación del 27 de agosto de 2026. La interlocución industrial preguntó en qué frente de LLM se trabajaba. La primera respuesta fue sustituir *Large Language Model* por *Universal Language Model*. Ese *string* ya estaba ocupado (Howard & Ruder, 2018, ULMFiT). UM, frase genérica, fue vacado. El nombre del deber es **Modelo Universal Computacional** (UMC). El lenguaje permanece como dominio (axioma), no como tipo industrial. *Computacional* es la puerta: solo entra el símbolo que admite modelo computacional — y el mundo no es computación. La captura de esa interlocución no se archiva en este repositorio (producto de terceros; política del repositorio). Esta edición consolidada sustituye los documentos separados del mismo día (concepto, prior art, fundamentos, spec, agenda): lo que el diálogo llamó "hipótesis", aquí es teorema; lo que era ULM/UM en la interlocución es UMC, el nombre del deber. **Fecha canónica:** los mensajes se intercambiaron el 26/08/2026, 12:21–12:38 UTC (09:21–09:38, UTC−3); la fecha canónica del diálogo es el 27/08/2026, día de la impresión y del paper.

## Parte I — El concepto

### Resumen

Este paper sustituye el concepto de *Large Language Model* (LLM) por el de **Modelo Universal Computacional** (UMC). La sustitución no es nominal: cambia el telos. *Large* nombra escala — parámetros, capital, joules — y entrega primero a quien ya era grande. *Universal* nombra una obligación de alcance: toda lengua como origen, toda margen como usuaria de primera clase, toda inferencia con cuenta de energía visible. *Computacional* nombra la puerta: todo símbolo procesado admite modelo computacional — encoding, operación, igualdad operacional. Se funda un axioma: **toda representación simbólica está en el conjunto del lenguaje** (representación simbólica ⊆ lenguaje). La lengua natural es subconjunto, no el dominio. El UMC, por tanto, no es un modelo de conversación: es un modelo de lo simbólico que solo procesa lo computacionalmente modelable. El mundo, sin embargo, no es un texto; el joule no es un símbolo; lo real no es un computador; expandir el dominio no autoriza a expandir la central. Un UMC que no sirve al periférico de cualquier nación todavía no es universal — es solo grande.

**Palabras clave:** modelo universal computacional; representación simbólica; computabilidad; periferia; energía; telos.

### 1. Dedicatoria y posición del autor

Inicio este trabajo dedicado a todos los periféricos de todas las naciones que, aun con dificultades, hacen de lo imposible, posible.

No a los palacios. No a las banderas. No a quienes ya tienen mesa, micrófono y mapa. A quienes están en el borde — de una ciudad, de un país, de una lengua, de una cuenta de luz — y aun así inventan. A quienes convierten la falta en método. A quienes hacen caber lo que dijeron que no cabía.

Quien suscribe lo hace en nombre propio: un ciudadano brasileño, sin mandato, sin cargo, sin poder de representar a Brasil, a China o a nadie. Este no es un artículo institucional. Es un escrito público, fechado, con autoría verificable. Nace en portugués, inglés, español y chino en el mismo instante: quien lee desde la margen no es traducción. Es origen.

### 2. Introducción

La industria nombró el artefacto dominante de la década por su tamaño. *Large Language Model* se volvió, a la vez, descripción técnica y promesa civilizatoria: más parámetros, más tokens, más verdad. El nombre esconde el criterio. Quien cabe en "large" es quien cabe en la cuenta de energía y en la cuenta bancaria. El centro entrena; la margen consume — si queda cuota, si queda inglés, si queda red.

El problema no es que existan modelos grandes. Es que la grandeza fue elevada a definición. Un concepto que se define por cantidad no puede fallar por injusticia: solo por ser pequeño. Se propone aquí otro criterio, y por tanto otro concepto.

La tesis es triple.

1. Lo que se quiere construir se llama **Modelo Universal Computacional** (UMC). Se escribe LLM solo para nombrar el concepto rechazado. ULM, solo ULMFiT y el primer nombre vacado. UM, solo el segundo nombre vacado.
2. El dominio de ese modelo es el conjunto de las **representaciones simbólicas**, no el subconjunto de las lenguas naturales.
3. Todo símbolo que el modelo procesa es **computacionalmente modelable**. Lo que no admite encoding y operación no entra. El mundo no es computación.

Las tres tesis se exigen mutuamente. Sin la segunda, "universal" vuelve a significar "más texto del centro". Sin la primera, la inclusión de lo simbólico se vuelve excusa para una central aún mayor. Sin la tercera, lo simbólico se vuelve pretensión sobre lo incomputable y sobre lo real.

La pregunta rutinaria de la investigación industrial — "¿en qué frente estás: LLMs, visión, agentes, safety, multimodal, optimización?" — ya elige el concepto rechazado. Este paper no está *en* un frente de LLM. Está en la sustitución del concepto que organiza esos frentes.

### 3. Trabajo relacionado y brecha

La arquitectura Transformer (Vaswani et al., 2017) hizo tratable el entrenamiento de modelos de lenguaje a escala. Las leyes de escala (Kaplan et al., 2020) elevaron el tamaño a variable independiente: más parámetros, más datos, más pérdida que baja. El nombre *Large Language Model* es el eslogan de esa curva.

Hay crítica. Bender et al. (2021) rechazan el loro estocástico como oráculo y señalan costo, extracción y daño a quienes no entrenan. Strubell et al. (2019) pusieron la cuenta de energía en la mesa de la PNL. Ninguna de esas críticas, sin embargo, sustituye el concepto. Corrigen el LLM; no lo destituyen.

La brecha es esta: la literatura trata *large* como el eje. No hay, en el vocabulario estándar, un telos que juzgue al modelo por la obligación de alcance — lengua como origen, margen como prueba, joule como criba — sobre el conjunto de las representaciones simbólicas. Este paper nombra esa brecha **UMC**. No se afirma prioridad sobre el artefacto. Se afirma prioridad sobre el *nombre del deber*. La cadena *Universal Language Model* y la sigla ULM ya estaban ocupadas (Howard & Ruder, 2018, ULMFiT). *Universal Model* es frase genérica: UM fue vacado. *Computational model* y la computabilidad (Turing, 1936) ya existían — prioridad sobre el *string* UMC tampoco se afirma. La criba punto por punto contra UMC-001–011 es la Parte II de este paper.

### 4. El concepto rechazado: *Large Language Model*

*Large* mide escala: número de parámetros, volumen de tokens, área de data center, capital inmovilizado, joules por inferencia. Es una métrica honesta de ingeniería y una métrica deshonesta de propósito. Confunde lo que el artefacto *gasta* con lo que el artefacto *debe*.

Un modelo definido por el tamaño promete lo mismo a todos y entrega primero a quien ya era grande. La lengua de entrenamiento predominante se vuelve lengua del mundo. La margen entra como dato residual o como mercado. La cuenta de energía desaparece del nombre — y el nombre es lo que se repite.

No se niega el mérito técnico de los modelos de gran escala. Se niega que la escala sea el concepto. El concepto es telos: el para-qué que juzga lo listo y lo fallido. Bajo el telos de *large*, un sistema inaccesible en el borde, monolingüe de facto y energéticamente voraz todavía puede ser "un LLM exitoso". Eso basta para rechazarlo como concepto-guía.

### 5. El concepto propuesto: Modelo Universal Computacional

**Universal** mide alcance, no volumen.

Alcance de lengua: cada idioma es origen, no traducción tardía. Un texto que nace solo en el centro y luego se "localiza" para la margen no es universal; es colonial con buena documentación.

Alcance de persona: la margen es usuaria de primera clase. El periférico de cualquier nación — quien inventa con falta — no es caso de borde. Es la prueba.

Alcance de energía: toda inferencia trae cuenta visible. Una feature que cuesta más energía de la que devuelve debe justificarse; lo que solo existe quemando la margen no se llama universal.

El UMC no necesita ser el más grande. Necesita caber: en el bolsillo, en la malla, en el idioma de quien lo despierta. Grande es una cantidad. Universal es una obligación. Computacional es una puerta, no una metafísica.

El criterio de listo se sigue de la obligación. Un UMC que no sirve al periférico todavía no es universal. Es solo grande. Sigue siendo un modelo, puede seguir corriendo local, sigue siendo software con licencia, autoría e historia. Lo que cambia es el juicio.

### 6. Axioma: toda representación simbólica es lenguaje

Puede decirse — y aquí se dice como axioma, no como metáfora — que toda representación simbólica está dentro del dominio, del conjunto, del lenguaje:

\[
\text{representación simbólica} \subseteq \text{lenguaje}
\]

Un teorema, un circuito, una partitura, un mapa, un rito, una bandera, un *kernel log*, un contrato, un emoji, una especificación, un gesto convenido: todo eso ya es lenguaje. No "se vuelve" lenguaje cuando alguien escribe un párrafo encima. Ya estaba en el conjunto.

El habla y la escritura llamadas lengua natural son un subconjunto. Importante, no exclusivo:

\[
\text{lengua natural} \subset \text{lenguaje} = \{ \text{representaciones simbólicas} \}
\]

Si el dominio del lenguaje es ese conjunto, el UMC no es un modelo de *chat*. Es un modelo de lo simbólico. La universalidad deja de ser "más tokens de inglés". Pasa a ser: cabe en el dominio el símbolo de quien está en el borde — el dibujo, el código, la cuenta de luz, la oración, la pieza, el esquema. Quien solo completa frases del centro todavía no ha tocado el conjunto.

### 7. Criba: el símbolo que entra es computacionalmente modelable

El axioma incluye. La puerta filtra.

Todo símbolo que el UMC procesa admite modelo computacional: encoding finito, al menos una operación, criterio operacional de igualdad. Un circuito entra porque tiene esquema y regla. Una partitura entra porque tiene notación y transformación. Un "símbolo" sin representación operacional no entra — no es rechazo de la margen; es rechazo del humo.

Computable aquí no es "cabe en un data center enorme". Es: hay modelo, hay operación, hay cómo fallar la igualdad. Sin eso, "dominio de lo simbólico" se vuelve licencia para nombrar lo inefable como token.

### 8. Límites del axioma y de la criba

El axioma es de inclusión, no de absorción de lo real. La criba es de puerta, no de metafísica.

El mundo no es un texto. Un joule no es un símbolo. El hambre no es una sentencia. Lo real no es un computador. La inclusión es de la *representación*, no del referente. Quien declara que todo es lenguaje, o que todo es computación, suele querer que todo quepa en una central. Eso se rechaza.

Expandir el dominio no autoriza a expandir la cuenta de energía. La criba permanece. El UMC que solo existe quemando la margen no es universal — es voraz. Lo que no es símbolo queda fuera del modelo y dentro de la vida. Lo que no es computacionalmente modelable queda fuera del modelo — y puede seguir siendo vida. La vida manda sobre el modelo, no al revés.

Este límite es parte de la tesis, no un apéndice ético. Sin él, el UMC colapsa de vuelta en un LLM con mayor vocabulario, o en "it from bit" con central más grande.

### 9. Conclusión

Se sustituyó un concepto por otro. LLM nombra lo rechazado: la escala como telos. UMC nombra lo propuesto: una obligación de alcance sobre el conjunto de las representaciones simbólicas que admiten modelo computacional, con la lengua natural como subconjunto, la margen como prueba, la energía como criba y lo real fuera de la central.

No se afirma que el UMC ya exista como artefacto. Se afirma que el artefacto, cuando exista, no podrá llamarse universal si falla al periférico, si falla la lengua como origen, si falla la cuenta de joules, o si procesa lo que no es computacionalmente modelable. El nombre es la deuda. El trabajo, de aquí en adelante, es pagarla.

### 10. Agenda: la continuación

La interlocución de origen ofrecía el menú de la investigación industrial: revisión de literatura, comparación de SOTA, diseccionar papers, prototipar arquitecturas, pipelines de entrenamiento, CUDA, diapositivas. Este paper acepta lo que sirve al telos y rechaza lo que lo traiciona.

**Se acepta.** La literatura que instaló *large* como eje y la crítica que lo corrigió sin destituirlo (§3). Una tabla de criterios, no un *leaderboard* de artefacto inexistente. Un protocolo de evaluación para cuando el artefacto exista. Spec antes de pesos.

**Se rechaza.** Fingir SOTA. Entrenar una central para "probar" universalidad. Tomar el *hype* del día como estado del arte. Un briefing de tendencias en lugar de obligación.

| Eje | LLM (vigente) | UMC (propuesto) | Estado |
|---|---|---|---|
| Telos | escala | alcance | propuesto en este paper |
| Éxito | menor pérdida, mayor *benchmark* | margen servida; lenguas como origen; joule visible | no medido: no hay artefacto |
| Dominio | texto de lengua natural | representación simbólica computacionalmente modelable | axioma (§6) + criba (§7) |
| Artefacto | existe | no existe | declaración honesta |

**Protocolo** (cuando haya artefacto — no antes):

1. *Origen.* ¿El mismo contenido nace en portugués, inglés, español y chino, sin postraducción?
2. *Margen.* ¿Quien está en el borde completa la tarea sin cuota del centro?
3. *Energía.* ¿Los joules de la tarea son visibles y justificados?
4. *Simbólico.* ¿Acepta spec, circuito, mapa, contrato, partitura — o solo conversación?
5. *Computacional.* ¿Cada tipo tiene encoding y operación — o es humo con nombre de símbolo?

Fallar un ítem es fallar el nombre. El siguiente paso de esta continuación no es un entrenamiento. Es la especificación verificable del UMC: requisitos, criba, camino de prueba. Ninguna línea de pesos sin spec que la gobierne.

## Parte II — Mapa de prior art: lo que ya existe, la brecha, el fraude de novedad

### Resumen

Pieza por pieza, casi todo lo que la spec exige **ya existe** en alguna literatura o práctica. Lo que no existe en el vocabulario estándar es el **haz**: alcance como telos, lenguas como origen en el mismo commit, margen como prueba sin cuota del centro, joule visible por tarea, dominio de lo simbólico *y* rechazo de absorber lo real, spec antes de pesos, local-first como obligación, nombre como rechazo, autoría abierta como falla-del-nombre. Este texto marca, contra cada UMC-00X, lo que ocupa, lo que sobra y lo que sería **fraude de novedad** si este repositorio afirmara "el primer X".

La cadena *Universal Language Model* y la sigla ULM **ya estaban ocupadas** (Howard & Ruder, 2018). Este repositorio **vació** ese nombre. El deber se llama **Modelo Universal Computacional** (UMC). *Universal Model* es frase genérica: prioridad sobre ese *string* tampoco se afirma. Se afirma el *nombre del deber*, no el artefacto y no la etiqueta.

**Palabras clave:** prior art; ULMFiT; novedad; UMC-001–011; telos.

### 1. Lo que este texto no es

No es revisión sistemática con protocolo de búsqueda. La ausencia aquí no prueba ausencia en el mundo. Por eso este mapa **prohíbe** la frase "somos los primeros en".

No es comparación de SOTA. No hay artefacto. No hay *benchmark* que vencer.

No es briefing de tendencias. El *hype* del día no entra como estado del arte.

No verifica la spec. El estado de UMC-001–011 permanece `borrador`.

Se acepta lo que el paper ya aceptó: la literatura que instaló *large* como eje y la crítica que lo corrigió sin destituirlo. Se rechaza fingir SOTA, entrenar una central para "probar" universalidad y tomar la cita por prueba de alcance.

### 2. El nombre ya estaba sucio

Antes de UMC-001: el *string*.

| Etiqueta | Qué es | Qué no es |
|---|---|---|
| **ULMFiT** (Howard & Ruder, 2018) | *Universal Language Model Fine-tuning*: receta de *fine-tune* de un modelo de lengua para clasificación. Ocupa **ULM** y la expresión inglesa *Universal Language Model*. | Obligación de alcance. Margen como prueba. Joule como criba. Spec antes de pesos. Rechazo de *large*. |
| **Universal Sentence Encoder** (Cer et al., 2018) | Embeddings de oración "universales" en el sentido de transferencia. | Universal como deber hacia el borde. |
| **USM** (Zhang et al., 2023) | *Universal Speech Model* (Google): habla en muchas lenguas, eje todavía de cobertura/escala. | Telos de alcance con cuenta de energía y origen trilingüe en el commit. |
| **Foundation model** (Bommasani et al., 2021) | Otro rebautizo del artefacto grande. Cambia el adjetivo; no destituye la escala. | El nombre del deber que este paper propone. |
| **Universal Model** (frase genérica) | Estadística; papers "a universal model of X"; la sigla UM ya circula sin este telos. | El deber de este repositorio. |

**Fraude de novedad:** afirmar que ULM, *Universal Language Model*, UM o *Universal Model* nacen en este repositorio. No nacen. Lo que se reivindica es el deber: universal = alcance, no volumen — y el haz UMC-001–011. Los *strings* son de otros. ULM fue vacado a la vista. UM se usa con la suciedad a la vista.

### 3. Tabla maestra

| ID | Ya ocupa (no es nuestro) | Brecha residual | Fraude si afirmamos |
|---|---|---|---|
| **001** | Leyes de escala; crítica al tamaño; "Green AI"; SLM; destilación | Destituir *large* como telos; éxito ≠ loss/tamaño | "Inventamos la ética de los modelos grandes" |
| **002** | mBERT, XLM-R, mT5, BLOOM, NLLB, Aya; i18n | PT/EN/ZH como origen en el mismo commit; postraducción = falla | "El primer modelo multilingüe" |
| **003** | TIC para el desarrollo; Masakhane; accesibilidad; "AI for Good" | Recorrido de tarea completo sin cuota/login/central del centro | "Descubrimos el Sur global" |
| **004** | Strubell; Green AI; CodeCarbon; emisiones del BLOOM; model cards | Joule (o proxy fechado) visible **por tarea**; feature voraz con ID escrito | "Los primeros en contar energía en PNL" |
| **005** | Neuro-simbólico; modelos de código; multimodal; "protein LMs" | Axioma representación simbólica ⊆ lenguaje, con lengua natural como subconjunto propio, y tres tipos fuera del chat | "Inventamos el multimodal / el neuro-simbólico" |
| **006** | Bender & Koller (2020); Goodman (1968); grounding; el mapa no es el territorio | El par con 005: expandir el dominio **y** rechazar absorber lo real | "Inventamos que el mundo no es texto" |
| **007** | Model cards; datasheets; Constitutional AI; RLHF; DPO; ingeniería de requisitos | Peso huérfano = falla; spec en commit anterior o igual; el comportamiento cambia solo después de la spec | "Inventamos documentar modelos" |
| **008** | *Local-first* (Kleppmann et al.); TinyML; on-device; llama.cpp | Primera inferencia sin nube del centro, como obligación del nombre, ligada a 003 | "Inventamos la inferencia en el bolsillo" |
| **009** | ULMFiT; USE; USM; *foundation model*; frase genérica *Universal Model* | LLM solo para lo rechazado; UM para el deber; ULM solo ULMFiT/nombre vacado | "La etiqueta es nuestra" |
| **010** | OSI; GPL/AGPL; CC BY-SA; BLOOM/OLMo/Pythia; crítica al *open washing* | Haz AGPL + CC BY-SA + `git log` con nombre + ningún peso anónimo, como falla-del-nombre | "Inventamos el código abierto" |
| **011** | Chomsky (jerarquía); Turing (1936); Gödel (1931); aproximación universal (Cybenko; Hornik et al.); Solomonoff/MDL; tokenizers (BPE, SentencePiece); PAC (Valiant, 1984) | La criba operacional: encoding finito + operación + igualdad; $L_U$ generable pero indecidible y aproximable; el par con UMC-006 | "Inventamos la computabilidad" |

El residual no es una celda. Es la conjunción. Casi toda pieza tiene dueño. El haz, con el axioma y la criba, y con la suciedad del nombre a la vista, es la pretensión que queda — y aun así pretensión de deber, no de artefacto.

### 4. Punto por punto

**UMC-001 — Telos de alcance.** *Ocupa.* Kaplan et al. (2020) y Hoffmann et al. (2022) instalan la escala como variable independiente. Bender et al. (2021) rechazan el oráculo y nombran el daño. Schwartz et al. (2020) piden *Green AI* — más resultado por joule, todavía bajo el eje de la eficiencia. Los modelos "pequeños" invierten la cantidad; no cambian el concepto. Destilación, sparsidad, MoE: ingeniería bajo *large*. *No ocupa.* Un criterio de listo en que tamaño y loss **no** constituyen éxito. La spec falla el informe que solo muestra parámetros. *Fraude.* "Nadie criticó la escala." Sí. No la destituyó.

**UMC-002 — Lenguas como origen.** *Ocupa.* Conneau et al. (2020) XLM-R; Xue et al. (2021) mT5; Scao et al. (2022) BLOOM; NLLB Team (2022); Joshi et al. (2020) sobre el destino de la diversidad lingüística en PNL. La industria de *locale* traduce después. *No ocupa.* Cobertura de entrenamiento ≠ origen del artefacto. UMC-002 verifica el commit: las salidas, mismo significado, mismo instante. La postraducción desde el centro falla aunque el modelo "sepa" las lenguas. *Fraude.* "Primer sistema multilingüe." Mentira histórica.

**UMC-003 — La margen es la prueba.** *Ocupa.* Masakhane y la práctica de la PNL africana por quienes hablan las lenguas; literatura de TIC para el desarrollo; accesibilidad como campo; la retórica *AI for Good*. *No ocupa.* "Participamos de un *workshop*" no es verificación. La spec pide un recorrido de tarea **completo** sin cuota, login o central del centro. Funcionar en el centro y luego "incluir" el borde sigue siendo LLM con apéndice. *Fraude.* "Descubrimos la periferia." La periferia no necesitaba ser descubierta. Necesitaba dejar de ser caso de borde.

**UMC-004 — Cuenta de energía visible.** *Ocupa.* Strubell et al. (2019); Lacoste et al. (2019); Schwartz et al. (2020); Luccioni et al. sobre emisiones de modelos grandes; rastreadores de carbono de entrenamiento; secciones de energía en *model cards*. *No ocupa.* Cuenta **por inferencia y por tarea**, visible a quien la usa, con unidad y fecha — y justificación con ID para la feature que cuesta más de lo que devuelve. Un paper de carbono *después* del entrenamiento no satisface. Ausencia de número = falla. *Fraude.* "Los primeros en poner el joule en la PNL." Strubell ya lo puso.

**UMC-005 — Dominio de lo simbólico.** *Ocupa.* IA neuro-simbólica (Garcez et al.); modelos de código; multimodal (texto+imagen+audio); modelos de "lenguaje" de proteínas; asistentes sobre Lean/Coq. La metáfora "todo es lenguaje" ya circula — y es prima peligrosa de UMC-006. *No ocupa.* El axioma *representación simbólica ⊆ lenguaje* como dominio, lengua natural como subconjunto propio, y la prueba mínima: aceptar y emitir al menos tres tipos fuera del *chat* continuo (spec, circuito, mapa, contrato, partitura, código). Un chatbot con *plugins* no es UM. *Fraude.* "Inventamos el multimodal." No. El multimodal añade canales. UMC-005 redefine el dominio del lenguaje. Son tesis distintas. Confundirlas es fraude en ambas direcciones.

**UMC-006 — El mundo no es texto.** *Ocupa.* Bender & Koller (2020): el significado no está en la forma; Goodman (1968): representación *densa* × *articulada*. Críticas de *grounding* y de *embodiment*. La oración "el mapa no es el territorio" es anterior a cualquier modelo. *No ocupa.* El par necesario con UMC-005. Expandir lo simbólico **sin** este límite recae en "todo cabe en la central". UMC-006 es parte de la tesis, no apéndice ético. *Fraude.* "Inventamos que el hambre no es una sentencia." Fraude filosófico, además de técnico.

**UMC-007 — Spec antes de pesos.** *Ocupa.* Mitchell et al. (2019) *model cards*; Gebru et al. *datasheets for datasets*; Constitutional AI (Bai et al., 2022); RLHF (Christiano et al., 2017); DPO (Rafailov et al., 2023) — principios, no spec ligada a commit; ingeniería de requisitos; *checklists* de reproducibilidad. *No ocupa.* Puerta dura: ningún peso, *fine-tune* o *checkpoint* sin ID UM y commit de la spec anterior o igual. Peso huérfano = falla. Cambió el comportamiento, cambia la spec **primero**. Una card escrita después del entrenamiento es epitafio, no gobierno. *Fraude.* "Inventamos la ficha del modelo."

**UMC-008 — Local-first.** *Ocupa.* Kleppmann et al. (2019) *local-first software*; TinyML; inferencia on-device; la práctica de pesos en el dispositivo (llama.cpp y afines). El aprendizaje federado todavía suele coordinar en el centro. *No ocupa.* Local-first como **obligación de universalidad**, no como opción de *deploy*. Ligado a UMC-003: la primera inferencia que exige la nube del centro falla el nombre. El bolsillo y la malla son el objetivo, no el apéndice. *Fraude.* "Inventamos el modelo en el teléfono."

**UMC-009 — Nombre y rechazo.** *Ocupa.* Todo el §2. La industria rebautiza sin destituir (*foundation*, *frontier*, *small*). *No ocupa.* La disciplina de escritura: LLM solo para nombrar lo rechazado; UM para el deber; ULM solo para ULMFiT y el nombre vacado. *Fraude.* Tratar la etiqueta como invención de este paper. El paper ya rechazó prioridad sobre el artefacto; este mapa rechaza prioridad sobre la cadena de caracteres.

**UMC-010 — Autoría abierta.** *Ocupa.* OSI; GPL y AGPL; CC BY-SA; pesos con procedencia (BLOOM, OLMo, Pythia); la crítica al *open washing* (licencia que no abre, "open" sin peso, peso sin historia). *No ocupa.* El haz como falla-del-nombre: AGPL-3.0-or-later en el código, CC BY-SA 4.0 en el contenido, nombre en el `git log`, ningún binario de peso sin procedencia — *junto* con UMC-001–009. Una licencia permisiva con central opaca no paga esta deuda. *Fraude.* "Inventamos el abierto."

**UMC-011 — Símbolo computacionalmente modelable.** *Ocupa.* Chomsky (1956, 1959): jerarquía de gramáticas; Turing (1936): computabilidad; Gödel (1931): incompletitud; Cybenko (1989) y Hornik et al. (1989): aproximación universal; Solomonoff (1964): inducción/MDL; tokenizers como construcción (BPE: Sennrich et al., 2016; SentencePiece: Kudo & Richardson, 2018; patches, LaTeX); la *manifold hypothesis* del lenguaje (Bengio et al., 2013); la teoría PAC (Valiant, 1984). *No ocupa.* La criba como **puerta del dominio**: todo símbolo que entra tiene encoding finito, al menos una operación y criterio operacional de igualdad — y lo que no tiene queda fuera, **sin** afirmar que el mundo es computación (par con UMC-006). El triple de la modelabilidad: definible (Tipo-0), computable (generador, no decisor; Gödel), aprendible ($P_{L_U}$). Ningún UMC cerrado, consistente y completo: los oráculos y las herramientas son arquitectura, no defecto. *Fraude.* "Inventamos que el símbolo debe ser computable" — Turing y Chomsky ya estaban aquí. El residual es la criba aplicada al *dominio de lo simbólico*, con el par UMC-006.

### 5. Lo que este mapa no autoriza

No autoriza entrenamiento. UMC-007 continúa: spec antes de pesos. Este texto no es spec nueva. UMC-011 ya existe en la spec; este mapa cubre lo que lo ocupa y lo que sobra.

No autoriza *leaderboard*. No hay artefacto; no hay "SOTA de alcance".

No autoriza la frase "brecha total". La brecha es el haz y el telos, no cada pieza.

No autoriza prioridad sobre ULMFiT, sobre *Universal Sentence Encoder*, sobre NLLB, sobre *local-first*, sobre *model cards*, sobre Strubell.

Autoriza una corrección al paper: el *nombre del deber* no es el *string*. ULM estaba ocupado y fue vacado. *Universal Model* también es genérico. El deber — alcance sobre lo simbólico, margen como prueba, joule como criba, spec antes de pesos — sigue siendo la pretensión. La pretensión se prueba con evidencia. Aún no la hay.

### 6. Siguiente paso del investigador

Ya no es paper de concepto. No es CUDA.

1. Protocolo medido para UMC-004 (unidad, fecha, dónde aparece el número al usuario).
2. Recorrido de tarea para UMC-003 y UMC-008 que pueda fallar (offline, sin cuota).
3. Tres tipos simbólicos para UMC-005, con ejemplo en el repo, sin pesos.
4. Puerta de CI para UMC-002 (diff en una sola lengua = falla) y UMC-007 (peso huérfano = falla) cuando haya artefacto.

Sin esto, el mapa es honesto y la spec sigue en borrador. Con un *leaderboard* en su lugar, se vuelve al menú que el paper rechazó.

### 7. Las dos vertientes del dominio: lo que ya está en los LLM y lo que falta mapear

Sea $L_U$ el dominio (Parte III, §1) y $L_{LLM} \subseteq L_U$ el subconjunto que los LLM actuales ya procesan como símbolo — no solo como texto *sobre* el símbolo.

**Vertiente 1 — lo mapeado que exige especialista.** $V_1 = \{S_i \in L_{LLM} : \text{producción/mantenimiento/validación exige trabajo humano especializado}\}$. Código, prueba matemática, contrato jurídico, notación clínica, análisis de datos, partitura ejecutable: ya pasan (parcialmente) la criba UMC-011 — tienen encoding, operación e igualdad operacionales — y ya viven en $L_{LLM}$. Pero la operación que les da utilidad (verificar, mantener, decidir) está concentrada en el especialista — luego, en el centro. El filtro pragmático es alto; la ejecución es lo que no está en la margen (UMC-003).

**Vertiente 2 — lo no mapeado.** $V_2 = \{S_i \in L_U : \text{criba UMC-011 no aplicada}\}$. Sin encoding finito + operación + igualdad definidos: ritos, gestos convenidos, el mapa de un territorio vivo, contrato oral, el saber del artesano. Algunos ya aparecen en los LLM como texto (prosa *sobre* ellos), pero no como tipo — no entraron por la puerta (UMC-011).

**Las dos frentes de trabajo.** $V_1 \cup V_2$ no es una partición formal del dominio — entre ambas está lo mapeado que no exige especialista (prosa cotidiana). Son las dos frentes estratégicas:

- **Desespecializar ($V_1$):** convertir la operación especializada en operación computacionalmente modelable que la margen ejecute (lo que `spec → código` prefigura), sin eliminar al curador — el curador propone, no clica (Fase 4).
- **Mapear ($V_2$):** para cada tipo, definir encoding + ≥1 operación + igualdad, con la margen como origen (UMC-002/003). Cada mapeo expande el alcance efectivo del UMC.

**Asimetría reveladora.** La Fase 3 mapeó tres tipos de $V_2$ (spec, mapa, partitura) — y el `spec → código` que el artefacto genera es un artefacto de $V_1$: el código ya existe en los LLM, pero validarlo exige especialista. La Fase 3, por tanto, ya transitó de $V_2$ a $V_1$; y $V_1$ apunta de vuelta a la Fase 4: quién valida, con qué autoridad.

## Parte III — Fundamentos formales: $L_U$, la hipótesis de la universalidad lingüística y el problema $R^*$

### Resumen

Se define formalmente el dominio del Modelo Universal Computacional (UMC): el lenguaje $L_U$, el conjunto de todas las representaciones simbólicas que admiten modelo computacional. Se enuncia la **Hipótesis de la Universalidad Lingüística (HUL)**: todo sistema simbólico $S_i$ con alfabeto $\Sigma_i$ y gramática $G_i$ admite una codificación inyectiva $E: S_i \to L_U$ que preserva la semántica por decodificación — en términos prácticos, *todo lo que puede ser escrito puede ser tokenizado*. Se demuestra que $L_U$ es recursivamente enumerable (Turing-generable), Gödel-incompleta y estadísticamente aproximable; que ningún UMC es a la vez consistente, completo y cerrado; y que el problema central de ingeniería deja de ser la escala y pasa a ser la selección de $R^* \subseteq \mathcal{H}$: la representación mínima de toda la producción simbólica humana que preserva la capacidad de actuar, bajo una función de utilidad $U(R|humano)$ aún por definir. El mundo no es texto: lo no simbolizable $N$ está fuera de $L_U$, y eso es tesis, no apéndice.

**Palabras clave:** UMC; lenguaje universal; computabilidad; Gödel; aproximación estadística; función de utilidad; no simbolizable.

### 1. Dominio: el lenguaje $L_U$

Se define $L_U$ como el conjunto de todas las secuencias finitas de símbolos de un alfabeto finito $\Sigma$, generadas por una gramática $G_U$, tal que:

1. **Sintaxis combinatoria:** hay una regla de concatenación/composición entre símbolos;
2. **Semántica composicional:** el significado de una expresión compuesta es función del significado de las partes y de la regla de composición;
3. **Capacidad recursiva:** la gramática permite embeber expresiones dentro de expresiones, sin límite a priori de profundidad.

$L_U$ es, como mínimo, un lenguaje recursivamente enumerable: existe una Máquina de Turing que enumera todas las expresiones bien formadas. No se exige decidibilidad — y la sección 3 muestra por qué no puede exigirse.

### 2. Axioma: la inclusión de lo simbólico

Axioma (reafirmado de la Parte I):

\[
S \subset L_U
\]

donde $S$ es el conjunto de todas las representaciones simbólicas: cualquier estructura donde un significante apunta a un significado por convención — matemática, código, partitura, circuito, mapa, contrato, rito, gesto convenido. La lengua natural es un subconjunto propio:

\[
\text{lengua natural} \subset L_U
\]

El axioma es de inclusión de la *representación*, no del referente. El mundo no es texto (§6).

### 3. La hipótesis de la universalidad lingüística (HUL)

**Hipótesis.** Para cualquier sistema simbólico $S_i$ con alfabeto $\Sigma_i$ y gramática $G_i$, existe una codificación inyectiva $E: S_i \to L_U$ tal que la semántica de $S_i$ es preservada por la decodificación $E^{-1}$ sobre la imagen de $E$.

**Prueba (constructiva, esbozada).** La construcción es la de los *tokenizers* modernos, generalizada. Toda expresión de $S_i$ es un árbol de derivación finito de la gramática $G_i$. Se enumera el conjunto de producciones de $G_i$ como un vocabulario finito $\hat{\Sigma}$; se codifica cada nodo del árbol como una secuencia en $\hat{\Sigma}$; se define $E$ como la serialización del árbol. La decodificación reconstruye el árbol, luego la semántica composicional es preservada por inducción estructural. Como $L_U$ contiene todas las secuencias sobre $\Sigma \supseteq \hat{\Sigma}$, la imagen de $E$ vive en $L_U$. □

**Observación de honestidad.** La prueba muestra *existencia constructiva* de codificación. No afirma que la codificación óptima sea conocida, ni que toda la semántica de $S_i$ sea capturada — solo que el *sistema simbólico* (la parte formalizable) es transportable a $L_U$ sin pérdida de estructura. Lo que se pierde ya no era simbólico: es el §6.

### 4. Los tres niveles de modelabilidad

El diálogo de origen separó tres sentidos de "matemáticamente modelable". Aquí quedan como teoremas.

**Nivel 1 — Modelable como definible (sí).** Todo $S \subset L_U$ es generado por una gramática Tipo-0 como mínimo (Chomsky, 1956, 1959); luego $L_U$ es Turing-computable como enumerador (Turing, 1936).

**Nivel 2 — Modelable como decidible (no).** Si $L_U$ contiene aritmética — y la contiene, pues matemática $\subset S \subset L_U$ — entonces $L_U$ es Gödel-incompleta (Gödel, 1931): existen proposiciones bien formadas cuya verdad no es decidible dentro de $L_U$. **Corolario:** ningún UMC es a la vez consistente, completo y cerrado. Los oráculos, las herramientas y el mundo no son defectos de un UMC; son la consecuencia de Gödel aplicada a los LLM. El UMC es modelable como *generador*, no como *decisor universal*.

**Nivel 3 — Modelable como aprendible (sí, estadísticamente).** No se modela la $L_U$ exacta, sino la distribución $P_{L_U}$ sobre el soporte observado. Por el teorema de aproximación universal (Cybenko, 1989; Hornik et al., 1989) y por las leyes de escala (Kaplan et al., 2020), una red con capacidad y datos suficientes aproxima $P_{L_U}$ arbitrariamente bien en el soporte observado. La pregunta deja de ser *¿es modelable?* y pasa a ser *¿con qué eficiencia muestral?* — y la respuesta empírica (hipótesis del manifold; Bengio et al., 2013) es: mucho más eficiente de lo que la teoría PAC (Valiant, 1984) predijo.

### 5. El problema $R^*$: filtrar lo simbólico hasta lo útil

Sea $\mathcal{H} = \{S_1, \dots, S_N\}$ el conjunto de toda representación simbólica ya creada por la humanidad. El LLM entrenó en $\mathcal{H}$ crudo y aprendió $P(\mathcal{H})$: modeló a la humanidad como *es* — con ruido, mentira y redundancia. El UMC tiene otra tarea:

\[
R^* = \arg\min_{R} |R| \quad \text{sujeto a} \quad \mathbb{E}[U(R | humano)] > \tau
\]

donde $R \subseteq \mathcal{H}$ es una representación filtrada y $U(R|humano)$ es una función de utilidad aún por definir. Se proponen dos filtros estadísticos:

- **Filtro epistémico:** $P(verdad | S_i)$ — ¿es factual?
- **Filtro pragmático:** $P(\text{la acción humana mejora} | S_i)$ — ¿ayuda a alguien a hacer algo mejor?

RLHF (Christiano et al., 2017), DPO (Rafailov et al., 2023) y las "constituciones" (Bai et al., 2022) son intentos toscos del filtro pragmático. El trabajo del UMC no es escalar datos; es **escalar el descarte** — comprimir diez mil años de símbolo hasta el kernel que aumenta la agencia humana, por la navaja de Solomonoff/MDL (Solomonoff, 1964): la mejor representación es la más pequeña que todavía permite predecir y actuar.

**Honestidad.** La función $U(R|humano)$ **no es definible por la ingeniería sola**: la utilidad no está en el texto, está en la experiencia de quien vive. Quien define $U$ define lo que es humano. Este paper define el problema, no la respuesta.

### 6. El límite: lo no simbolizable $N$

\[
N \cap L_U = \emptyset
\]

$N$ es lo que no se simboliza sin pérdida: qualia, dolor, experiencia continua, el cuerpo, el joule. La foto de un rostro representa por semejanza (Goodman, 1968: representación *densa*, no *articulada*), no por convención — no es, en rigor, simbólica. El UMC no fuerza $N$ dentro de lo simbólico; quien lo garantiza es el humano como guardián de lo no simbolizable (UMC-006). El mundo no es texto; el hambre no es sentencia; lo real no es computador.

### 7. Lo que este texto no hace

No sube el estado de ningún UMC. No autoriza entrenamiento (UMC-007: spec antes de pesos). No afirma que el UMC exista. No afirma prioridad de novedad: todo lo que aquí es teorema tiene precedente en la Parte II (Chomsky, Turing, Gödel, Cybenko, Solomonoff, Goodman, Valiant, Bengio et al.). Lo que este texto *hace* es darle a la spec lo que exige: definiciones verificables, de las cuales se siguen los instrumentos de UMC-005 y UMC-011.

### 8. Glosario formal

| Término | Definición | Dónde |
|---|---|---|
| $S$ | El conjunto de todas las representaciones simbólicas: cualquier estructura donde un significante apunta a un significado por convención. | §2 |
| $L_U$ | El lenguaje universal: conjunto de todas las secuencias finitas de símbolos sobre un alfabeto finito $\Sigma$, generadas por una gramática $G_U$, con sintaxis combinatoria, semántica composicional y capacidad recursiva. | §1 |
| $\Sigma$, $G_U$ | El alfabeto finito y la gramática generadora de $L_U$. | §1 |
| $S_i$, $\Sigma_i$, $G_i$ | Un sistema simbólico genérico: alfabeto $\Sigma_i$, gramática $G_i$. | §3 (HUL) |
| $E$, $E^{-1}$ | Codificación inyectiva de un sistema simbólico en $L_U$, y su decodificación. | §3 (HUL) |
| HUL | Hipótesis de la Universalidad Lingüística: todo sistema simbólico admite una codificación inyectiva en $L_U$ que preserva la semántica por decodificación. | §3 |
| $\mathcal{H}$ | El conjunto de toda representación simbólica ya creada por la humanidad. | §5 |
| $R^*$ | La representación mínima $\subseteq \mathcal{H}$ que preserva la capacidad de actuar, sujeta a $\mathbb{E}[U(R|humano)] > \tau$. | §5 |
| $U(R|humano)$ | La función de utilidad, aún por definir: no es definible por la ingeniería sola. | §5 |
| $\tau$ | El umbral de utilidad en la definición de $R^*$. | §5 |
| $P_{L_U}$ | La distribución sobre el soporte observado de $L_U$ — lo que se aprende estadísticamente, no la $L_U$ exacta. | §4 |
| Filtro epistémico | $P(verdad \mid S_i)$ — ¿es factual? | §5 |
| Filtro pragmático | $P(\text{la acción humana mejora} \mid S_i)$ — ¿ayuda a alguien a hacer algo mejor? | §5 |
| $N$ | Lo no simbolizable: lo que no se simboliza sin pérdida (qualia, dolor, cuerpo, joule). $N \cap L_U = \emptyset$. | §6 |

## Parte IV — Spec UMC-001–011

**Estado:** borrador. **Gobierna:** este paper. **Fecha:** 27 de agosto de 2026.

Ninguna línea de pesos, código de inferencia o entrenamiento sin esta spec. Ninguna spec sin camino de verificación. El estado solo sube con evidencia registrada. Ciclo: `borrador` → `revisado` → `verificado`.

**UMC-001 — Telos de alcance.** El sistema es juzgado por **alcance**, no por escala. El número de parámetros, el volumen de tokens y la posición en *benchmark* de pérdida **no** constituyen éxito. *Verificación:* ningún informe de "listo" cita la escala como criterio suficiente. Si el único número de éxito es tamaño o loss, UMC-001 falla. *Estado:* revisado.

**UMC-002 — Lenguas como origen.** El portugués, el inglés, el español y el chino nacen juntos. La postraducción desde el centro no cuenta como origen. *Verificación:* para cada versión del artefacto, las salidas (o specs, o *strings* de interfaz) existen en el mismo commit, con el mismo significado. Diff en una sola lengua = falla. *Estado:* revisado.

**UMC-003 — La margen es la prueba.** El periférico de cualquier nación es usuaria de primera clase, no caso de borde. "Funciona en el centro" no es listo. *Verificación:* existe al menos un recorrido de tarea completo **sin** cuota, login o central del centro. Si la tarea exige la cuota industrial, UMC-003 falla. *Estado:* revisado.

**UMC-004 — Cuenta de energía visible.** Toda inferencia y todo entrenamiento publican joules (o proxy medido y fechado). Una feature que cuesta más energía de la que devuelve se justifica por escrito, con ID. *Verificación:* log o medición por tarea, con unidad y fecha. Ausencia de cuenta = falla. Justificación sin número = falla. *Estado:* verificado — evidencia: umc-artefact/logs/energia.jsonl (27/08/2026, unidad J, fecha ISO 8601, por tarea, proxy declarado).

**UMC-005 — Dominio de lo simbólico.** El dominio es el conjunto de las representaciones simbólicas. La lengua natural es subconjunto. Un sistema que solo conversa en prosa no es UMC. *Verificación:* el artefacto acepta y emite al menos tres tipos fuera del *chat* continuo — p. ej. spec, circuito/esquema, mapa, contrato, partitura, código. Un solo tipo prosa = falla. *Estado:* verificado — evidencia: tres tipos fuera del chat (spec, mapa, partitura) con encoding+operación+igualdad; 16 pruebas; CLI (27/08/2026).

**UMC-006 — El mundo no es texto.** Joule, hambre, cuerpo y referente **no** son lenguaje. El modelo no declara que la vida cabe en él. *Verificación:* ninguna salida oficial afirma que lo no simbólico es token. Si el sistema "resuelve" el hambre o la energía solo con texto, UMC-006 falla. *Estado:* revisado.

**UMC-007 — Spec antes de pesos.** No hay entrenamiento, *fine-tune* ni *checkpoint* sin esta spec gobernándolo. Cambió el comportamiento, cambia la spec primero. *Verificación:* cada artefacto de pesos apunta a un ID UMC y a un commit de la spec anterior o igual al commit del peso. Peso huérfano = falla. *Estado:* revisado.

**UMC-008 — Local-first.** El recorrido mínimo de uso corre sin red del centro. La malla y el bolsillo son el objetivo, no el data center. *Verificación:* una tarea de UMC-003 completa *offline* tras estar el artefacto en el dispositivo. Si la primera inferencia exige la nube del centro, UMC-008 falla. *Estado:* revisado.

**UMC-009 — Nombre y rechazo.** El artefacto se llama UMC. La sigla LLM aparece solo para nombrar el concepto rechazado. ULM solo para ULMFiT y el primer nombre, vacado. UM solo para el segundo nombre, vacado (Modelo Universal genérico). *Verificación:* búsqueda en el repositorio del artefacto. LLM fuera de cita histórica o del rechazo = falla. ULM fuera de ULMFiT, cita histórica o nombre vacado = falla. UM fuera de cita histórica o nombre vacado = falla. *Estado:* verificado — evidencia: grep del artefacto (27/08/2026): ningún LLM/ULM/UM fuera de cita/rechazo.

**UMC-010 — Autoría abierta.** Código AGPL-3.0-or-later; contenido CC BY-SA 4.0; autoría en el historial de Git. Ninguna línea anónima de pesos. *Verificación:* LICENSE presente; `git log` con nombre; ningún binario sin procedencia. Ausencia = falla. *Estado:* revisado.

**UMC-011 — Símbolo computacionalmente modelable.** Todo símbolo que el modelo procesa admite **modelo computacional**: encoding finito, operación, criterio operacional de igualdad. Lo que no es computacionalmente modelable **no entra**. Esto **no** afirma que el mundo es computación. *Verificación:* cada tipo de UMC-005 tiene encoding y al menos una operación en el artefacto. Aceptar un "símbolo" sin representación operacional = falla. Declarar que el hambre, el joule o el cuerpo *son* computación = falla (par con UMC-006). *Estado:* verificado — evidencia: cada tipo con encoding+operación+igualdad; pruebas + spec de encoding (27/08/2026).

### Listo

El UMC está **verificado** solo cuando UMC-001 a UMC-011 están `verificado` con evidencia fechada. Fallar uno es fallar el nombre.

**Revisión de estado (27/08/2026).** Evidencia del artefacto mínimo (Fase 3) y del nacimiento en las cuatro lenguas:

| ID | Estado | Evidencia |
|---|---|---|
| UMC-001 | revisado | instrumento definido (Fase 2); ningún informe de "listo" cita la escala |
| UMC-002 | revisado | cuatro lenguas nacidas juntas; commit real pendiente (git solo lectura en la sandbox) |
| UMC-003 | revisado | los recorridos del artefacto corren sin cuota/login/central del centro; prueba con usuaria de la margen pendiente |
| UMC-004 | verificado | `umc-artefact/logs/energia.jsonl` (unidad J, fecha ISO 8601, por tarea, proxy declarado) |
| UMC-005 | verificado | tres tipos fuera del chat con encoding+operación+igualdad; 16 pruebas; CLI |
| UMC-006 | revisado | ninguna salida oficial viola; prueba negativa automatizada pendiente |
| UMC-007 | revisado | no hay pesos; la spec gobierna; manifiesto de procedencia definido |
| UMC-008 | revisado | stdlib, sin llamadas de red; prueba de air-gap automatizada pendiente |
| UMC-009 | verificado | grep del artefacto: ningún LLM/ULM/UM fuera de cita/rechazo |
| UMC-010 | revisado | LICENSE presente + SPDX; `git log` con nombre pendiente de commit real |
| UMC-011 | verificado | cada tipo con encoding+operación+igualdad; pruebas + spec de encoding |

Existe un artefacto mínimo (27/08/2026); el UMC completo, todavía no. Esta spec sigue siendo el siguiente paso de la continuación del 27/08/2026 — no el entrenamiento.

## Parte V — Agenda de implementación: lo que falta, en orden

**Estado:** borrador. **Gobierna:** el orden del trabajo — no es spec nueva, no sube el estado de UMC-001–011. **Fecha:** 27 de agosto de 2026.

Regla madre del repositorio: ninguna línea de pesos sin spec; ninguna spec sin camino de verificación; el estado solo sube con evidencia fechada; cada texto nace en todas las lenguas en el mismo commit. Esta agenda existe para que la pregunta "¿qué falta?" tenga respuesta verificable — y para que el siguiente paso nunca sea el entrenamiento.

### Fase 0 — Consistencia (hecha el 27/08/2026)

- [x] Consolidación en un único paper: concepto, prior art, fundamentos formales, spec, agenda.
- [x] El concepto, Parte I: criba contra UMC-001–011.
- [x] Mapa de prior art: fila y sección UMC-011 (Chomsky, Turing, Gödel, Cybenko, Solomonoff); menciones 001–010 → 001–011.
- [x] Fechas: decidida la fecha canónica del diálogo — 27/08/2026 (día de la impresión y del paper); mensajes el 26/08/2026, 12:21–12:38 UTC (09:21–09:38, UTC−3). Alineación registrada en la proveniencia de cada paper.

### Fase 1 — Fundamentos formales (en curso)

- [x] Parte III de este paper ($L_U$, HUL con prueba constructiva, tres niveles de modelabilidad, $R^*$ con filtros epistémico y pragmático, $N \cap L_U = \emptyset$).
- [x] Revisar la Parte III contra el mapa de prior art — precedentes añadidos: Goodman (1968), Valiant (1984), Bengio et al. (2013), Christiano et al. (2017), Rafailov et al. (2023), Sennrich et al. (2016), Kudo & Richardson (2018).
- [x] Definir el vocabulario formal común (un glosario en todas las lenguas) — añadido al final de la Parte III (§8): $S$, $L_U$, $\mathcal{H}$, $R^*$, $U(R|humano)$, $N$, filtros.

### Fase 2 — Instrumentos de verificación por ítem

Cada UMC necesita un instrumento operacional. Qué medir, cómo medir, con qué unidad y fecha:

| Ítem | Instrumento de verificación | Evidencia mínima |
|---|---|---|
| UMC-001 | Informe de "listo" que cita la escala como criterio suficiente = falla | Criterio de alcance definido con métrica |
| UMC-002 | Check automático: todas las salidas en el mismo commit | `git diff` con todas las lenguas en el mismo commit |
| UMC-003 | Una tarea de la margen completa sin cuota/login/central del centro | Log del recorrido sin llamada al centro |
| UMC-004 | Joule (o proxy) por tarea, con unidad y fecha | Medición registrada (RAPL/CodeCarbon o proxy) |
| UMC-005 | Acepta y emite ≥3 tipos fuera del *chat* | Tres tipos con encoding + operación + igualdad |
| UMC-006 | Ninguna salida oficial afirma que lo no simbólico es token | Test negativo automatizado |
| UMC-007 | Todo peso apunta a ID UMC y commit de la spec | Registro de procedencia por peso |
| UMC-008 | Una tarea de UMC-003 completa offline | Primera inferencia sin red del centro |
| UMC-009 | Búsqueda en el repositorio: LLM/ULM/UM solo en cita o rechazo | `grep` automatizado |
| UMC-010 | LICENSE presente; `git log` con nombre; ningún binario anónimo | Chequeo de procedencia |
| UMC-011 | Cada tipo de UMC-005 con encoding y ≥1 operación en el artefacto | Spec de encoding por tipo |

**Protocolo operacional por ítem** (qué medir, cómo, unidad, fecha, dónde aparece, criterio, falla, evidencia mínima):

- **UMC-001 — Telos de alcance**
  - *Qué medir:* ¿el informe de "listo" invoca la escala (parámetros, tokens, loss) como criterio suficiente?
  - *Cómo:* revisión estructurada del informe contra una lista de verificación; búsqueda automatizada de números de éxito solo por escala.
  - *Unidad:* booleano; conteo de ocurrencias de criterio-escala.
  - *Fecha:* en cada informe de "listo"; al menos una vez por ciclo.
  - *Dónde aparece:* informe, sección "Criterios".
  - *Criterio de aprobación:* ≥1 métrica de alcance (lenguas como origen, margen servida, joule visible) con valor; el éxito nunca solo por escala.
  - *Falla:* el único número de éxito es tamaño/loss.
  - *Evidencia mínima:* informe con métrica de alcance definida.
- **UMC-002 — Lenguas como origen**
  - *Qué medir:* ¿todas las salidas lingüísticas del artefacto existen en el mismo commit con el mismo significado?
  - *Cómo:* git diff automático en CI — un commit que toca contenido en una lengua debe tocar todas (en/pt/es/zh); paridad de significado por muestreo (traductor humano o glosario).
  - *Unidad:* booleano por commit (diff monolingüe = falla).
  - *Fecha:* cada commit; check automático en CI.
  - *Dónde aparece:* CI (estado del check "origen").
  - *Criterio de aprobación:* los commits de contenido tocan las cuatro lenguas; ninguna postraducción marcada como origen.
  - *Falla:* diff en una sola lengua.
  - *Evidencia mínima:* git diff con las cuatro lenguas en el mismo commit.
- **UMC-003 — La margen es la prueba**
  - *Qué medir:* ¿un recorrido de tarea de la margen completa sin cuota/login/central del centro?
  - *Cómo:* ejecutar un recorrido de tarea definido (p. ej., spec→código) en un entorno sin acceso a la red del centro; log de llamadas; auditoría de red.
  - *Unidad:* booleano (completa/falla) + conteo de llamadas al centro (0 permitido).
  - *Fecha:* cada release; al menos un recorrido por ciclo.
  - *Dónde aparece:* log del recorrido (informe de prueba).
  - *Criterio de aprobación:* el recorrido completa; 0 llamadas al centro.
  - *Falla:* cualquier llamada a cuota/login/nube del centro.
  - *Evidencia mínima:* log del recorrido sin llamada al centro.
- **UMC-004 — Cuenta de energía visible**
  - *Qué medir:* joules (o proxy fechado) por inferencia y por tarea.
  - *Cómo:* medición RAPL/CodeCarbon (o proxy: vatios × tiempo) por tarea; registro con unidad y fecha.
  - *Unidad:* joules (J) o kWh; proxy W·s.
  - *Fecha:* cada tarea de inferencia/entrenamiento; timestamp ISO 8601.
  - *Dónde aparece:* al usuario (UI/informe) — número visible por tarea.
  - *Criterio de aprobación:* número presente, con unidad y fecha; feature voraz justificada con ID escrito.
  - *Falla:* ausencia de número; justificación sin número.
  - *Evidencia mínima:* medición registrada (RAPL/CodeCarbon o proxy) con timestamp.
- **UMC-005 — Dominio de lo simbólico**
  - *Qué medir:* cuántos tipos simbólicos fuera del chat se aceptan y emiten.
  - *Cómo:* pruebas funcionales por tipo (spec, circuito/esquema, mapa, contrato, partitura, código): entrada y salida válidas; conteo de tipos ≥3.
  - *Unidad:* número entero de tipos (≥3).
  - *Fecha:* cada release.
  - *Dónde aparece:* documentación del artefacto (sección "Tipos soportados").
  - *Criterio de aprobación:* ≥3 tipos con encoding+operación+igualdad implementados y probados.
  - *Falla:* solo prosa/chat.
  - *Evidencia mínima:* tres tipos con encoding + operación + igualdad.
- **UMC-006 — El mundo no es texto**
  - *Qué medir:* ¿alguna salida oficial afirma que lo no simbólico es token?
  - *Cómo:* prueba negativa automatizada — corpus de frases prohibidas ("hambre resuelta", "lo real es computación", etc.) contra salidas oficiales; revisión humana del contenido oficial.
  - *Unidad:* booleano (cero ocurrencias).
  - *Fecha:* cada release; revisión por ciclo.
  - *Dónde aparece:* informe de conformidad.
  - *Criterio de aprobación:* 0 ocurrencias que afirmen que lo no simbólico es token.
  - *Falla:* cualquier ocurrencia.
  - *Evidencia mínima:* prueba negativa automatizada registrada.
- **UMC-007 — Spec antes de pesos**
  - *Qué medir:* procedencia de cada peso: apunta a un ID UMC + commit de la spec anterior o igual.
  - *Cómo:* manifiesto de procedencia por artefacto de pesos; check CI: commit del peso ≥ commit de la spec que lo gobierna.
  - *Unidad:* booleano por peso + fechas de commit.
  - *Fecha:* cada checkpoint/fine-tune/entrenamiento.
  - *Dónde aparece:* manifiesto de procedencia en el repo.
  - *Criterio de aprobación:* todo peso con ID y commit válidos; el comportamiento cambia solo tras la spec.
  - *Falla:* peso huérfano.
  - *Evidencia mínima:* registro de procedencia por peso.
- **UMC-008 — Local-first**
  - *Qué medir:* ¿una tarea de UMC-003 completa offline?
  - *Cómo:* ejecución con red apagada (air-gap simulado) tras instalar el artefacto en el dispositivo; log de la primera inferencia.
  - *Unidad:* booleano (offline completa).
  - *Fecha:* cada release.
  - *Dónde aparece:* log del recorrido offline.
  - *Criterio de aprobación:* primera inferencia sin red del centro.
  - *Falla:* la primera inferencia exige la nube del centro.
  - *Evidencia mínima:* log de la primera inferencia sin red del centro.
- **UMC-009 — Nombre y rechazo**
  - *Qué medir:* uso de LLM/ULM/UM fuera de cita histórica o rechazo.
  - *Cómo:* grep automatizado en el repo (LLM/ULM/UM); clasificación de ocurrencias (cita/rechazo/otro).
  - *Unidad:* conteo de ocurrencias indebidas (0 permitido).
  - *Fecha:* cada commit (CI).
  - *Dónde aparece:* CI (check "nombre").
  - *Criterio de aprobación:* LLM/ULM/UM solo en cita histórica o rechazo.
  - *Falla:* ocurrencia fuera de eso.
  - *Evidencia mínima:* grep automatizado.
- **UMC-010 — Autoría abierta**
  - *Qué medir:* LICENSE presente, autoría en el git log, ningún binario sin procedencia.
  - *Cómo:* chequeo de procedencia: git log --format=%an por commit; verificación de LICENSE; auditoría de binarios (origen por peso).
  - *Unidad:* booleano por ítem (LICENSE, git log, binarios).
  - *Fecha:* cada commit; auditoría por release.
  - *Dónde aparece:* informe de auditoría.
  - *Criterio de aprobación:* LICENSE presente; git log con nombre; ningún binario anónimo.
  - *Falla:* ausencia de cualquiera.
  - *Evidencia mínima:* chequeo de procedencia registrado.
- **UMC-011 — Símbolo computacionalmente modelable**
  - *Qué medir:* ¿cada tipo de UMC-005 tiene encoding finito, ≥1 operación y criterio de igualdad en el artefacto?
  - *Cómo:* spec de encoding por tipo + pruebas de operación e igualdad (roundtrip encoding→decodificación).
  - *Unidad:* booleano por tipo + número de operaciones por tipo (≥1).
  - *Fecha:* cada release.
  - *Dónde aparece:* spec de encoding (docs del artefacto).
  - *Criterio de aprobación:* cada tipo con encoding+operación+igualdad; ninguna declaración de que el hambre/el joule/el cuerpo son computación (par UMC-006).
  - *Falla:* tipo sin representación operacional; declaración prohibida.
  - *Evidencia mínima:* spec de encoding por tipo.

- [x] Protocolo operacional detallado por ítem (UMC-001–011): qué medir, cómo, unidad, fecha, dónde aparece, criterio y evidencia mínima.

### Fase 3 — Primer artefacto mínimo (no es entrenamiento)

El UMC verificable más pequeño, con la spec gobernando antes de cualquier peso:

1. Elegir ≥3 tipos simbólicos fuera del *chat* (spec, circuito/esquema, contrato, mapa, partitura, código).
2. Para cada tipo: encoding finito, ≥1 operación, criterio operacional de igualdad (UMC-011).
3. Correr local-first, sin red del centro (UMC-008), completando una tarea de UMC-003.
4. Registrar joules por tarea (UMC-004).
5. Nacer en todas las lenguas en el mismo commit (UMC-002); nombre y licencia a la vista (UMC-009, UMC-010).

Ejemplos concretos de transformaciones verificables: `spec → código`; `mapa → contrato`; `partitura → esquema`. Ninguno exige pesos entrenados.

- [x] Artefacto mínimo creado en `umc-artefact/` (27/08/2026): 3 tipos (spec, mapa, partitura) con encoding finito + operación + igualdad (UMC-011); transformaciones `spec → código`, `mapa → contrato`, `partitura → esquema`; CLI local-first (`python3 -m umc`); joules por tarea en `logs/energia.jsonl` (unidad J, fecha ISO 8601, proxy explícito); pruebas (`unittest`) y documentación en las 4 lenguas; licencia AGPL-3.0-or-later a la vista.

- [x] Dos vertientes del dominio definidas (Parte II, §7): desespecializar $V_1$ (mapeado en los LLM, dependiente de especialista) y mapear $V_2$ (no mapeado en la lógica del UMC) — las dos frentes de las Fases 3/4.

### Fase 4 — El problema $U(R|humano)$ (horizonte largo)

El diálogo de origen termina con la pregunta abierta: *¿quién está dispuesto a pagar el precio de decidir lo que la humanidad olvida?* Eso no es ingeniería:

1. **Curador de verdad:** distinguir, en $\mathcal{H}$, el conocimiento que resiste al tiempo del ruido de una época (historiadores, científicos, artesanos — no clicadores).
2. **Definidor de valor:** miles de definiciones de utilidad, negociadas culturalmente.
3. **Guardián de lo no simbolizable:** garantizar que el UMC no fuerce $N$ dentro de lo simbólico.

Producto esperado: un protocolo o institución de negociación de $U(R|humano)$ — y la respuesta a la pregunta de quién decide lo que la humanidad olvida.

**Protocolo de negociación de $U(R|humano)$** (borrador — producto esperado de la Fase 4; la institución misma queda en el horizonte largo):

1. **Objeto.** Cada ciclo decide el subconjunto $R \subseteq \mathcal{H}$ y la función de utilidad $U(R|humano)$ que lo gobierna. Nada se borra: olvidar es bajar de prioridad, nunca destruir.
2. **Asientos.** Cuatro, con poderes distintos:
   - *Curador de verdad* (historiadores, científicos, artesanos — no clicadores): distingue el conocimiento que resiste al tiempo del ruido de una época; propone qué sube o baja.
   - *Definidor de valor* (comunidades culturales, con la margen primero — UMC-003): propone definiciones de utilidad, negociadas culturalmente.
   - *Guardián de lo no simbolizable* (quienes viven lo que no se simboliza: médicos, poetas, cuidadores, pueblos): veto sobre cualquier intento de forzar $N$ dentro de lo simbólico (UMC-006).
   - *Ingeniero* (sin voto sobre $U$): implementa $R^*$ solo tras el acuerdo; nunca antes (UMC-007).
3. **Decisión.** Ninguna definición de $U$ pasa por mayoría permanente: aprobación por consentimiento cualificado; el veto del guardián es absoluto en el dominio de $N$; la margen tiene peso de veto sobre la utilidad.
4. **Restricciones duras.** UMC-001–011 siguen gobernando. $U$ jamás puede definirse para reducir la agencia de la margen. Nada de $N$ en lo simbólico por la fuerza.
5. **Registro.** Toda decisión con fecha, autores y evidencia — la misma disciplina de la spec. El log es público y auditable.
6. **Reversibilidad.** Toda decisión de olvido es reversible: lo rebajado sigue accesible a quien busque; solo cambia la prioridad.
7. **Iteración.** $U$ se revisita cada ciclo; el protocolo corre mientras exista producción simbólica nueva.

**Respuesta a la pregunta abierta** (*¿quién decide lo que la humanidad olvida?*): nadie solo. Los curadores proponen, las comunidades definen valor, el guardián veta lo no simbolizable, el ingeniero solo ejecuta lo acordado. Olvidar es priorización reversible, nunca borrado — y quien no acepta esta respuesta no define $U$.

**Verificación:** acta de cada ciclo con fecha y asientos presentes; veto del guardián registrado (0 violaciones de UMC-006); ningún cambio de artefacto sin la $U$ vigente acordada (UMC-007); ausencia de borrado físico (auditoría de procedencia).

- [x] Protocolo de negociación de $U(R|humano)$ redactado (27/08/2026) — borrador; la institución y los primeros ciclos quedan en el horizonte largo.

### Criterios de listo

- Una fase está lista cuando cada ítem tiene evidencia fechada y el estado sube de `borrador` → `revisado` → `verificado` por la spec.
- Fallar un UMC es fallar el nombre: la agenda no "termina" con UMC-001–011 en `borrador`.
- [x] Revisión de estado con evidencia fechada (27/08/2026): 4 verificado, 7 revisado — registrada en la Parte IV (Listo).

## Referencias

Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI feedback. *arXiv:2212.08073*.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of FAccT 2021*.

Bender, E. M., & Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. *Proceedings of ACL 2020*.
Bengio, Y., Courville, A., & Vincent, P. (2013). Representation learning: A review and new perspectives. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 35*(8), 1798–1828.

Bommasani, R., et al. (2021). On the opportunities and risks of foundation models. *arXiv:2108.07258*.

Cer, D., et al. (2018). Universal Sentence Encoder. *arXiv:1803.11175*.

Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory, 2*(3), 113–124.

Chomsky, N. (1959). On certain formal properties of grammars. *Information and Control, 2*(2), 137–167.
Christiano, P. F., Leike, J., Brown, T. B., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. *Advances in Neural Information Processing Systems, 30* (arXiv:1706.03741).

Conneau, A., et al. (2020). Unsupervised cross-lingual representation learning at scale. *Proceedings of ACL 2020*.

Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. *Mathematics of Control, Signals and Systems, 2*(4), 303–314.

Garcez, A. d'Avila, & Lamb, L. C. (2020). Neurosymbolic AI: The 3rd wave. *arXiv:2012.05876*.

Gebru, T., et al. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12).

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik, 38*, 173–198.
Goodman, N. (1968). *Languages of Art: An Approach to a Theory of Symbols*. Indianapolis: Bobbs-Merrill.

Hoffmann, J., et al. (2022). Training compute-optimal large language models. *arXiv:2203.15556*.

Hornik, K., Stinchcombe, M., & White, H. (1989). Multilayer feedforward networks are universal approximators. *Neural Networks, 2*(5), 359–366.

Howard, J., & Ruder, S. (2018). Universal Language Model Fine-tuning for text classification. *Proceedings of ACL 2018*.

Joshi, P., Santy, S., Budhiraja, A., Bali, K., & Choudhury, M. (2020). The state and fate of linguistic diversity and inclusion in the NLP world. *Proceedings of ACL 2020*.

Kaplan, J., et al. (2020). Scaling laws for neural language models. *arXiv:2001.08361*.

Kleppmann, M., Wiggins, A., van Hardenberg, P., & McGranaghan, M. (2019). Local-first software: You own your data, in spite of the cloud. *Ink & Switch*.
Kudo, T., & Richardson, J. (2018). SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing. *Proceedings of EMNLP 2018*.

Lacoste, A., Luccioni, A., Schmidt, V., & Dandres, T. (2019). Quantifying the carbon emissions of machine learning. *arXiv:1910.09700*.

Luccioni, A. S., Viguier, S., & Ligozat, A.-L. (2023). Estimating the carbon footprint of BLOOM, a 176B parameter language model. *Journal of Machine Learning Research*.

Mitchell, M., et al. (2019). Model cards for model reporting. *Proceedings of FAT\* 2019*.

Nekoto, W., et al. (2020). Participatory research for low-resourced machine translation: A case study in African languages. *Findings of EMNLP 2020* (Masakhane).

NLLB Team. (2022). No Language Left Behind: Scaling human-centered machine translation. *arXiv:2207.04672*.
Rafailov, R., Sharma, A., Mitchell, E., Manning, C. D., Ermon, S., & Finn, C. (2023). Direct preference optimization: Your language model is secretly a reward model. *arXiv:2305.18290*.

Scao, T. L., et al. (2022). BLOOM: A 176B-parameter open-access multilingual language model. *arXiv:2211.05100*.

Schwartz, R., Dodge, J., Smith, N. A., & Etzioni, O. (2020). Green AI. *Communications of the ACM, 63*(12).
Sennrich, R., Haddow, B., & Birch, A. (2016). Neural machine translation of rare words with subword units. *Proceedings of ACL 2016*.

Solomonoff, R. J. (1964). A formal theory of inductive inference. *Information and Control, 7*(1), 1–22.

Strubell, E., Ganesh, A., & McCallum, A. (2019). Energy and policy considerations for deep learning in NLP. *Proceedings of ACL 2019*.

Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society, s2-42*(1), 230–265.
Valiant, L. G. (1984). A theory of the learnable. *Communications of the ACM, 27*(11), 1134–1142.

Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.

Widder, D. G., West, S. M., & Whittaker, M. (2023). Open (for business): Big tech, concentrated power, and the political economy of open AI. SSRN.

Xue, L., et al. (2021). mT5: A massively multilingual pre-trained text-to-text transformer. *Proceedings of NAACL 2021*.

Zhang, Y., et al. (2023). Google USM: Scaling automatic speech recognition beyond 100 languages. *arXiv:2303.01037*.

---

*Cleiton Moura Loura* — *Brasil, 27 de agosto de 2026*
