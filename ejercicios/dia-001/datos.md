---
dia: 1
semana: 1
habilidad: listening
drill: primer-contacto
mock: null

base_fija:
  anki_nuevas: 6
  fonema:
    bloque: 1
    contraste: acento-lexico
    etapa: explicacion
    elsa: false

ejercicio:
  objetivo: "Detectar dónde cae el acento en inglés y por qué moverlo rompe la palabra."
  items:
    - tipo: listening
      instruccion: "Escuchá (o leé) la frase dos veces antes de responder."
      stimulus: "Sorry, I'm a bit knackered — can we push this to tomorrow?"
      audio:
        uk: null
        us: null
      opciones:
        - {letra: A, texto: "Que lo ayudes a terminar el trabajo hoy."}
        - {letra: B, texto: "Reprogramar la reunión para mañana."}
        - {letra: C, texto: "Que le pases un café."}
        - {letra: D, texto: "Que le expliques la tarea otra vez."}
      correcta: B
      por_que: >-
        La petición está en «push this to tomorrow». «Knackered» es solo el motivo
        (está cansado), no lo que pide. Pide con cortesía en vez de mandar: en inglés
        británico eso es lo normal en el trabajo, y sonar directo de más se lee como
        grosero.

    - tipo: listening
      instruccion: "¿En qué sílaba cae el acento? Marcá una."
      stimulus: "tomorrow"
      audio:
        uk: null
        us: null
      opciones:
        - {letra: A, texto: "to-MOR-row (segunda)"}
        - {letra: B, texto: "TO-mor-row (primera)"}
        - {letra: C, texto: "to-mor-ROW (tercera)"}
        - {letra: D, texto: "Todas igual, como en español."}
      correcta: A
      por_que: >-
        Es la segunda. En español la regla de acentuación la podés deducir de la
        terminación; en inglés el acento es parte de la palabra y no se deduce de nada.
        «Tomorrow» se acentúa en el medio y nadie lo escribió con tilde para avisarte.

    - tipo: speaking
      instruccion: "Decí las tres en voz alta, marcando la sílaba larga. Una sola línea."
      stimulus: "record (verbo) · record (sustantivo) · present (verbo)"
      audio:
        uk: null
        us: null
      opciones: []
      correcta: null
      por_que: >-
        re-CORD «grabar» contra PRE-sent «documento», y pre-SENT «presentar» contra
        PRE-sent «regalo». Mover el acento en inglés no hace la palabra más extranjera:
        la convierte en otra palabra. Ese es todo el argumento del día.

coloquial:
  - {expr: "push it to…", uk: "push it to", us: "reschedule", sentido: "Mover algo de fecha"}
  - {expr: "I'm beat", uk: "knackered", us: "beat", sentido: "Cansadísimo (la versión americana)"}

vocabulario:
  - palabra: knackered
    fuente: material
    uk: knackered
    us: beat
    frase: "Sorry, I'm a bit knackered — can we push this to tomorrow?"
    sentido: Cansadísimo, agotado
  - palabra: push it to…
    fuente: material
    uk: push it to
    us: reschedule
    frase: "Can we push this to tomorrow?"
    sentido: Mover algo de fecha
  - palabra: sorry
    fuente: material
    uk: sorry
    us: excuse me
    frase: "Sorry, do you mind if I sit here?"
    sentido: Disculpa — suaviza casi cualquier cosa
  - palabra: record (v)
    fuente: frecuencia
    uk: re-CORD
    us: re-CORD
    frase: "I'll record the meeting so you can listen later."
    sentido: Grabar. El acento va en la segunda.
  - palabra: present (v)
    fuente: frecuencia
    uk: pre-SENT
    us: pre-SENT
    frase: "I'm presenting the results on Friday."
    sentido: Presentar. Mismo spelling que el sustantivo, acento distinto.
  - palabra: about
    fuente: frecuencia
    uk: a-BOUT
    us: a-BOUT
    frase: "It'll take about five minutes."
    sentido: Aproximadamente. Acento en la segunda.
---

# Por qué el acento léxico va primero

En español la acentuación se deduce: si la palabra termina en vocal, n o s, el acento va en la
penúltima sílaba salvo tilde. Tenés una regla y la aplicás.

En inglés no hay regla. **El acento es parte de la palabra**, igual que el número de sílabas o las
letras que la componen. No se deduce de la ortografía ni del final. Por eso «tomorrow» no lleva
tilde y aun así se acentúa en el medio.

Eso tiene una consecuencia que te va a servir las 13 semanas: **un acento mal puesto no te hace
sonar exótico, te hace sonar otra palabra.** *re-CORD* es grabar; *PRE-sent* es un documento. No hay
segunda lectura posible.

Es el error raíz del hispanohablante, y va primero por eso — no por ser el más difícil, sino porque
todo lo demás se apoya acá. La sílaba acentuada es la que se **estira**, y todas las demás se
aplastan. Sin esa jerarquía no hay schwa que valga, ni function words que se reduzcan, ni ritmo que
se escuche.
