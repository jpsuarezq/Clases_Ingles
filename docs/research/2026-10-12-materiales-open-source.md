# Research: materiales open source para las cuatro habilidades

**Ticket:** #7
**Fecha:** 2026-10-12
**Método:** `research` skill, solo web. Repo es **público**, así que solo se puede copiar lo de
licencia abierta.

**Clave de veredicto usada:**
- ✅ **COPIAR** — puede ir al repo público (con condiciones indicadas)
- 🔗 **SOLO LINK** — gratis en su propio sitio, pero la licencia prohíbe republicarlo; nunca tratarlo como fuente reutilizable
- ⛔ **EVITAR** — licencia restrictiva o por obra; no construir ejercicios encima
- ⚠️ **SIN VERIFICAR** — sin declaración de licencia; por defecto se trata como solo link

---

## 1. La verdad corta

| Skill | Mejor fuente reutilizable | Mejor complemento de solo link |
|---|---|---|
| **Listening** | **VOA Learning English** (dominio público), **Everyday Conversations** (US State Dept, PD), **Mozilla Common Voice** (CC0, con tag de acento US/GB/AU/NZ) | BBC Learning English, British Council, ELLLO, Randall's |
| **Reading** | **VOA**, **Wikinews (CC BY)**, **Simple English Wikipedia (CC BY-SA 4.0)**, **Project Gutenberg (PD)** | News in Levels, Breaking News English, ReadWorks |
| **Writing** | Prompts propios + modelos de **VOA/Wikinews**, **Tatoeba (CC BY 2.0 FR)**, **CommonLit (CC BY-NC-SA)** | British Council Writing, samples oficiales de IELTS |
| **Speaking** | **Common Voice (CC0)** shadowing por acento, **IPA Chart (CC BY-SA 4.0)**, **Praat (GPL)** | Forvo, YouGlish, audio de diccionarios |

**Verdad dura para planificar:** **no existe audio de curso británico/australiano/neozelandés
con licencia abierta.** El requisito de acentos británicos hay que cubrirlo con (a) clips de
Common Voice etiquetados por acento (CC0), (b) lectores de LibriVox de esos países (PD), y
(c) BBC/British Council **solo como destino de escucha**, nunca como material incrustado.

---

## 2. LISTENING

### ✅ VOA Learning English — https://learningenglish.voanews.com/
**Dominio público**, declarado por primera parte: *"All text, audio and video material produced
exclusively by the Voice of America is in the public domain"* y *"You are allowed to reprint them
for educational and commercial purposes, with credit to learningenglish.voanews.com"*.
**Contenido:** MP3 + transcript completo + quiz por artículo; series de gramática e idiomas
(*Let's Learn English* A1–A2, *Everyday Grammar*, **Words and Their Stories** — idiom genuino,
*American Stories*). **Nivel A1–C1**, explícitamente graduado.
**⚠ Caveats de sus propios términos:** lo con fuente **AP/Reuters/AFP NO es dominio público**
(mayormente fotos/gráficos — saltear), y el nombre/logo "VOA" es trademark.
**Encaje de formato:** ideal para **HTML standalone** — el MP3 va a `assets/`, `<audio>` +
pregunta → validación, feedback citando la línea del transcript.

### ✅ Everyday Conversations: Learning American English (US Dept. of State)
https://americanenglish.state.gov/resources/everyday-conversations-learning-american-english
**Dominio público** — la página de Copyright Info del sitio remite a state.gov: *"Unless a
copyright is indicated, information on State Department websites is in the public domain and may
be copied and distributed without permission."* Sin indicador de copyright en la página del recurso.
**Contenido:** PDF completo + **~40 diálogos MP3 descargables**, deliberadamente contrastados:
*Formal Greetings* vs *Informal Greetings*, *Formal Introductions* vs *Informal*, llamada
telefónica, médico, direcciones, supermercado, dar opiniones/consejo… **Nivel A2.**
**Encaje:** **el mejor activo para ejercicios HTML** — un diálogo MP3 por página. Los pares
formal/informal están hechos a medida para ejercicios **markdown** de "¿qué registro es?"

### ✅ Mozilla Common Voice — https://commonvoice.mozilla.org/datasets
**CC0** (declarado en la página y en el datasheet).
**Contenido:** corpus inglés 27.0 — **2,59 M de clips leídos en voz alta, 100.546 hablantes**,
MP3 + transcript, con **acentos auto-reportados**: US 22.2%, **England 7.9%, Australia 2.7%,
New Zealand 0.8%**, Escocia, Canadá, India, Irlanda, Gales…
**⚠ Dos condiciones de Mozilla:** **no re-hospedar/espejar el dataset** "in whole or in part", y
**nunca identificar hablantes**. En la práctica: elegir unos pocos clips a mano está bien, espejar
en masa no.
**Encaje:** **HTML** — "escuchá y elegí el acento", toggle GB/US/AU/NZ.

### ✅ LibriVox — https://librivox.org/
**Dominio público / CC0** ("All LibriVox Recordings are in the Public Domain").
~200k capítulos de audiolibros leídos por voluntarios; lectores de UK, US, Australia, NZ →
**acentos con licencia abierta**. Nivel realista **B1+** (registro literario, no graduado).
⚠ Para usuarios no-EEUU: el estatus PD depende de la norma local del libro subyacente — quedarse
con obras pre-1929.

### 🔗 SOLO LINK — los populares
- **BBC Learning English** — su propia página: *"You are not permitted to copy, broadcast,
  download, store, transmit, show or play in public, adapt or change in any way the content"*.
  Excelente como **destino recomendado**; **nunca** como fuente de ejercicios.
- **British Council LearnEnglish** — ©, sin concesión CC en ninguna parte.
- **Randall's ESL Cyber Listening Lab** — gratis online, pero vende licencias de contenido.
- **ELLLO** — ⚠️ **sin página de licencia**; footer "elllo productions © copyright 2026".
  **Tratar como solo link** hasta que aparezca una declaración.
- **OpenLearn (The Open University)** — ✅ texto **CC BY-NC-SA 4.0**, pero su política **excluye**
  del CC a "video and photographic images" y "sound recordings" → ✅ texto, 🔗 **audio/video solo link**.

---

## 3. READING

### ✅ Wikinews — https://en.wikinews.org/
**CC BY 4.0** (footer del sitio; los dumps registran CC BY 2.5). **Attribution-only, sin
share-alike, sin NC** — la licencia más permisiva del grupo Wikimedia.
Noticias cortas, inglés llano. Ideal para tareas de **resumen** (puente Reading → Writing).

### ✅ Wikipedia / Simple English Wikipedia
**CC BY-SA 4.0**. Wikipedia ≈ **B2+** para un A2; **Simple English ≈ B1**, usable en A2 con
andamiaje. **Condiciones:** atribución **y share-alike** — los extracts adaptados hay que
licenciarlos compatible BY-SA, y marcar esos archivos claramente.

### ✅ Project Gutenberg — https://www.gutenberg.org/
Obras subyacentes en **dominio público**. 75k+ libros, **sin audio**. Nivel B1–C1; registro
a menudo **datado**.
**⚠** No reproducir el header/logo "Project Gutenberg™" — es trademark; quitar el envoltorio,
quedar con la obra.

### ✅ (condicional) CommonLit
**CC BY-NC-SA 4.0** para originales; algunos textos son dominio público.
**Contenido:** textos + preguntas de comprensión + vocabulario — **estructura pregunta-primero
idéntica al formato markdown elegido**. Nivel mayormente **B1–C1**.
**✅ solo si el repo se mantiene estrictamente no-comercial**, con atribución, y cualquier
lección adaptada se re-licencia BY-NC-SA.

### ✅ Textos de gobierno bajo licencia abierta (solo registro formal)
- **Reino Unido — Open Government Licence v3**: copiar, publicar, distribuir, adaptar,
  explotar comercial y no comercialmente → ✅ con atribución + aviso OGL.
- **Australia — CC BY 3.0 AU** por defecto → ✅ **inglés australiano** con atribución.
- **Nueva Zelanda — CC BY 4.0** por defecto → ✅ **inglés neozelandés** con atribución.
- **Registro:** formal/burocrático, B1+; útil para minar ideas de IELTS Task 1/2, **no coloquial**.

### 🔗 SOLO LINK — los que la gente toma por gratis
- **Breaking News English** — las propias condiciones prohíben reproducir online: *"Permission is
  not granted to reproduce the Article, the exercises that go with it, or any material from this
  website on any other website, social media platform, online video sharing platform, blog, app,
  Learning Management System…"*. Solo copias de papel y links al HTML. **Los dos formatos de
  ejercicio elegidos son exactamente lo que prohíbe.**
- **News in Levels** — ⚠️ **sin licencia encontrada**.
- **ReadWorks** — términos prohíben modificar/copiar/distribuir (verificación parcial).
- **ESL Fast, ManyThings, ESL Flow, ISL Collective** — ⚠️ sin licencia abierta; ISL Collective es
  por-worksheet bajo licencia del subidor → ⛔.

---

## 4. WRITING

**No existe un curso de writing A2 con licencia libre** que valga la pena; no encontré ninguno con
licencia abierta verificable. **Recomendación: construir los prompts vos** (los prompts no son
copyrightables), anclados en **textos modelo de licencia abierta.**

### ✅ Modelos copiables
- **VOA articles (PD)** — "leer → resumir / reescribir formalmente".
- **Wikinews (CC BY)** — resúmenes de actualidad; solo atribución, la licencia más fácil.
- **Tatoeba** — https://tatoeba.org/ — **CC BY 2.0 FR** para frases de texto. Pares **EN↔ES
  naturales y a menudo coloquiales** → perfecto para micro-writing A2: reordenar, traducir,
  corregir, expandir. ✅ copiar **con atribución de autor**. ⚠️ **El audio es por contribuyente** —
  algunos CC BY, muchos CC BY-NC; solo usar audio con campo de licencia CC BY.
- **CommonLit prompts (CC BY-NC-SA)** — ✅ bajo NC+SA.
- **Cartas en dominio público** (Gutenberg) — modelos de formal vs informal (Task 1 de IELTS),
  con el registro datado en mente.

### 🔗 Solo link
British Council Writing (©), **samples oficiales de IELTS** — Cambridge pide permiso escrito y el
branding IELTS es trademark. **⛔ nunca copiar preguntas, audio ni model answers band 9.**
Purdue OWL — ⚠️ licencia sin verificar.

---

## 5. SPEAKING (pronunciación, shadowing, drills de fonemas)

### ✅ Mozilla Common Voice (CC0) — corpus principal de shadowing
Elegir clips **por tag de acento**: US (modelo), **England, Australia, New Zealand** →
"escuchar → repetir → comparar". Clips de 5 s, ideales para drilling A2.

### ✅ IPA Chart — licencia verificada con su cadena de atribución exacta
*"As of July 2012, they are made freely available under a Creative Commons Attribution-Sharealike
4.0 International Deed (CC BY-SA 4.0)… there is no need to request permission"*.
**Uso:** los drills de contraste español→inglés (`/θ/ vs /s/`, `/ɪ/ vs /iː/`, `/æ/ vs /e/`) pueden
embeber el chart, con la atribución sugerida textual.

### ✅ Praat — https://www.fon.hum.uva.nl/praat/ — **GPL v3+**
El regrabado ve pitch/entonación/formantes al lado del modelo. **El único reemplazo abierto de
las apps de pronunciación de pago.** Es una herramienta a linkear, no contenido del repo.

### ✅ (verificar por archivo) Wiktionary / Wikimedia Commons / Lingua Libre
Audio de pronunciación **CC BY-SA 4.0 o PD por archivo**. ✅ en HTML **si se registra licencia +
autor de cada archivo** en un CREDITS; ⚠️ hay PD, BY-SA 3.0 y algunos non-free — **revisar la
página de cada archivo**.

### ✅ LibriVox (PD) — pasajes de shadowing más largos.

### 🔗 Solo link
**Forvo** (UGC, los contributors conservan derechos), **YouGlish** (©), audio de diccionarios
Cambridge/Oxford/M-W (propietario — gratis *escuchar en su sitio*, no extraer), British Council
Speaking (©), **Speechling** (⚠️ licencia sin verificar), **Duolingo** (©).

---

## 6. Lista de NO usar (frecuentemente llamados "gratis" y no lo son)

| Recurso | Por qué no | Veredicto |
|---|---|---|
| BBC Learning English / BBC Sounds | Prohíbe explícitamente copiar/descargar/adaptar | 🔗 |
| British Council LearnEnglish/TeachEnglish | © + Terms of Use, sin CC | 🔗 |
| Breaking News English | Prohíbe cualquier reproducción online o re-formateo | 🔗 |
| Materiales oficiales de IELTS (Cambridge/BC/IDP) | Copyright + trademark, "written permission required" | 🔗, ⛔ copiar |
| Randall's ESL Lab, ELLLO | Gratis online; licencia requerida / sin verificar | 🔗 |
| ReadWorks, News in Levels, ESL Fast, ManyThings | Términos prohíben redistribuir / sin licencia | 🔗 |
| ISL Collective | Licencia por obra, retenida por el subidor | ⛔ |
| Letras de canciones, scripts de cine/TV, Urban Dictionary, Reddit, casi todo YouTube | Todos los derechos reservados | ⛔ |
| Audio de diccionarios extraído | Propietario | 🔗 |

---

## 7. Picks finales por skill (1–2 principales + 2–3 de apoyo)

### 🎧 LISTENING
1. **Principal — VOA Learning English** (PD, ✅): MP3 + transcript + quiz, A1–C1.
   → *HTML:* una lección por página, `<audio>` + preguntas + feedback citando el transcript.
2. **Principal — Everyday Conversations, US State Dept** (PD, ✅): 40 diálogos A2, pares
   formal/informal. → *HTML:* listen-and-choose con validación instantánea; *markdown:* roleplay
   con llave de respuestas.
3. Apoyo — **Common Voice** (CC0, ✅) para micro-listening de **acentos GB/AU/NZ**; **LibriVox**
   (PD, ✅); **BBC Learning English** (🔗) como puntero "escuchá más acá", nunca embebido.

### 📖 READING
1. **Principal — VOA articles** (PD, ✅, A1–C1) graduados → cloze/gist en HTML.
2. **Principal — Wikinews** (CC BY, ✅) + **Simple English Wikipedia** (CC BY-SA, ✅) → resúmenes
   y paráfrasis (marcar archivos BY-SA con atribución y share-alike).
3. Apoyo — **Gutenberg** (PD, ✅), **CommonLit** (CC BY-NC-SA, ✅ con NC+SA), **GOV.UK (OGL) /
   AU (CC BY 3.0 AU) / NZ (CC BY 4.0)** para input de registro formal de IELTS Task 1/2.

### ✍️ WRITING
1. **Principal — prompts propios** anclados en modelos de VOA (PD) o Wikinews (CC BY):
   leer → resumir / reescribir formal↔informal (aprovechando el contraste de registro de
   Everyday Conversations).
2. **Principal — Tatoeba EN↔ES** (CC BY 2.0 FR, ✅ con atribución): micro-writing a granularidad A2.
3. Apoyo — CommonLit (✅ con NC+SA), cartas de Gutenberg (PD, ✅); 🔗 British Council Writing y
   model answers oficiales de IELTS (nunca copiar).

### 🗣️ SPEAKING
1. **Principal — Common Voice shadowing por acento** (CC0, ✅): "escuchá (US) → decí → grabá →
   compará", más variantes **GB/AU/NZ** de la misma frase para entrenar el oído de IELTS.
2. **Principal — IPA Chart** (CC BY-SA 4.0, ✅ con su cadena de atribución) para los drills de
   contraste español→inglés.
3. Apoyo — **LibriVox** (PD, ✅), audio de **Wiktionary/Commons** (por archivo, ✅ si se registra),
   **Praat** (GPL, ✅) para auto-chequear entonación. 🔗 Forvo, YouGlish, audio de diccionarios.

---

## 8. Mecánica de atribución para el repo público
Agregar un **`CREDITS.md`** (o front-matter por archivo) listando:
- **CC BY** (Wikinews, Tatoeba — autor + URL + licencia)
- **CC BY-SA** (Wikipedia/Wikisource, IPA chart, audio de Commons — atribución **y** share-alike
  aplican al texto adaptado; licenciar esos extracts como BY-SA)
- **CC BY-NC-SA** (CommonLit, texto de OpenLearn — mantenerlos en archivos marcados no-comercial)
- **PD/CC0** (VOA, State Dept, obras de Gutenberg, LibriVox, Common Voice — agradecer como
  cortesía, y notar la petición de Mozilla de "no espejar el dataset / no identificar hablantes")

**Nunca incluir contenido de** BBC, British Council, IELTS oficial, Breaking News English ni
ReadWorks — **linkearlos está bien** y se fomenta como destinos del alumno.

## 9. Licencias explícitamente sin verificar (tratar como solo link)
ELLLO, News in Levels, Purdue OWL, Speechling, Fun Easy English, ESL Fast / ManyThings,
ReadWorks (términos verificados solo vía copia de terceros — parcial), y las páginas de gobierno
AU/NZ/UK (licencia nacional verificada a nivel de política — **cada página individual hay que
revisarla por un aviso distinto**).