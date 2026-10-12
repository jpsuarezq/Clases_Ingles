# Curso de inglés (A2 → IELTS Academic)

Bitácora personal de una persona hispanohablante que estudia inglés 30–60 min al día durante
13 semanas, orientada a IELTS Academic. No es un curso para terceros.

## Estructura del plan

**Carpeta de día**:
Unidad de trabajo del plan: una carpeta por día del curso, nombrada por número de día del plan
(`dia-001/` a `dia-090/`), nunca por fecha. Contiene el ejercicio del día y su registro.
_Avoid_: unidad, lección, clase (la carpeta no es una clase ni un tema, es un día del plan)

**Ejercicio**:
El HTML interactivo del día, en formato B (panel de explicación permanente a la derecha). Va en la
carpeta de día. Es el único formato de ejercicio.
_Avoid_: tarea, práctica, actividad

**Base fija**:
Lo que se hace todos los días sin importar la habilidad que toque: repaso SRS de vocabulario y
drill de pronunciación, 10–15 minutos. Su material va **dentro** del ejercicio del día, no en un
archivo aparte.
_Avoid_: warm-up, rutina

**Bloque rotante**:
El ejercicio principal del día. Su habilidad rota entre reading, writing, speaking y listening.
_Avoid_: sección principal, parte principal

**Habilidad del día**:
Cuál de las cuatro rota hoy. Determina qué tipo de ejercicio se arma.
_Avoid_: skill del día, materia

**Datos del día**:
El archivo fuente del ejercicio, dentro de la carpeta de su día (`datos.md`). Contiene preguntas,
opciones, coloquial y vocabulario. De él se genera el HTML; el HTML no se edita a mano.
_Avoid_: contenido, fuente, input

**Generador**:
El artefacto que convierte los datos del día en el HTML del ejercicio. Se corre para las 90 carpetas
a la vez, no día por día.
_Avoid_: script, build, compilador

## Registro y medición

**Bloque de registro**:
El bloque de datos que el HTML entrega al terminar el ejercicio, listo para copiar y pegar en el
registro del día. Es la única forma de llenarlo: no se tipea a mano.
_Avoid_: resumen del día, output

**Registro del día**:
Qué se hizo el día y con qué resultado. Vive en la carpeta de su día, en un formato que el
agregador pueda leer.
_Avoid_: log, tracker, diary

**Agregador de registro**:
Artefacto generado que lee los registros de todas las carpetas de día y calcula el progreso. No se
escribe a mano: se genera desde los registros diarios.
_Avoid_: resumen, dashboard, informe

**Progreso**:
Cuántos días del plan están completados y con qué resultado, calculado por el agregador. Es la
única fuente de verdad sobre "dónde voy".
_Avoid_: avance, porcentaje de curso

## Nivel e idioma objetivo

**Ancla**:
El test con el que se mide el nivel: EF SET 4 skills, en la semana 0 y en la semana 13. Es el único
instrumento de medición; todo lo demás es dirección.
_Avoid_: diagnóstico, examen

**Banda**:
El nivel IELTS (0–9). Es una **estimación direccional**, no un resultado: el ancla no produce banda
oficial y pone "n/a" si el nivel cae en A1/A2. En este plan **solo se puede computar de Listening y
Reading** — Writing y Speaking no tienen forma gratuita de producirla, así que la banda registrada
es un **piso** del nivel real, no el nivel.
_Avoid_: score, puntaje IELTS, nivel

**Rotación**:
El orden fijo y cíclico de las habilidades del bloque rotante: Listening → Writing → Speaking →
Reading, y repite. Cuatro habilidades a partes iguales, sin ponderar hacia las que producen banda.
Un día de mock **toma el día** y la rotación retoma después de donde estaba.
_Avoid_: schedule, secuencia, plan semanal

**Drill de sección**:
Extracto oficial de un solo tipo de pregunta (una grabación de Listening, un pasaje de Reading). Es
el contenido normal del día cuando toca esa habilidad. No produce banda: sin las 40 preguntas
completas no hay conversión.
_Avoid_: práctica, mini-test, extracto

**Mock sentado**:
Listening + Reading completos, con tiempo, puntuados. Solo hay material gratis para **tres** en todo
el plan, y se reparten en dos días consecutivos porque no caben en 60 minutos de una.
_Avoid_: examen de prueba, simulacro completo

## Vocabulario

**Deck**:
Un **solo** deck de Anki con tags, no decks separados por skill. Dos decks son dos sesiones, y la
frecuencia de práctica pesa más que los minutos. Los phonemas **no van acá**: van en el drill diario
del ejercicio, que tiene audio y días de producción.
_Avoid_: mazo, decks por skill, subdeck

**Card de vocabulario**:
La **frase coloquial completa**, no la palabra suelta. El frente trae la frase con audio UK y US; el
atras trae la palabra, su equivalente al otro lado del Atlántico, y el phonema del día. Captura
palabra, contexto de uso y par UK/US de una vez.
_Avoid_: flashcard, tarjeta, card L1→L2

**Tasa de vocabulario**:
Seis palabras nuevas por día, sostenidas durante las 90 jornadas. Cierra ~540 palabras contra una
brecha A2→B2 de 2.000–3.000 familias: el deck cubre alrededor de un quinto, y el resto lo pone la
exposición incidental de leer y escuchar todos los días.
_Avoid_: palabras por sesión, cuota diaria

**Fuente de vocabulario**:
Mixta. Las palabras salen del **material del día** —que ya trae contexto y encuentros— y se
completan con una **lista de frecuencia** cuando el material no llega a la cuota. Solo el material
sería temático; solo la lista, sin contexto.
_Avoid_: word list, fuente única

## Pronunciación

**Bloque fonético**:
Un tramo de días dedicado a un solo contraste, aprendido y cerrado antes de pasar al siguiente.
Los fonemas **no se intercalan**: la evidencia directa favorece el bloqueo para pronunciación
(Carpenter & Mueller, 2013, cuatro experimentos), a diferencia de lo que pasa con gramática.
_Avoid_: unidad fonética, lección de sonido

**Secuencia fonética**:
El orden interno de un bloque: **explicación articulatoria → percepción con feedback → producción**.
Trabajar solo percepción es la peor inversión si el objetivo es producir.
_Avoid_: rutina, progression

**Drill de phonema**:
El trabajo de pronunciación de la base fija diaria. Va en todos los días del ejercicio, dentro del
bloque fonético que toque.
_Avoid_: práctica de sonido, warm-up de pronunciación

## Medición

**Banda medida**:
La banda computada de Listening y Reading a partir del número de aciertos y las tablas raw→band
oficiales. Es la **única** pista que sirve para medir la meta de cierre, porque es lo comparable
con el EF SET. Nunca se promedia con la autoevaluada.
_Avoid_: band score, nivel medido

**Banda autoevaluada**:
La puntuación que uno se da en Writing y Speaking contra los descriptores oficiales de IELTS. Va
marcada con su fuente para que el agregador no la mezcle con la medida. Sirve para ver **tendencia**,
no para dar por cumplida la meta.
_Avoid_: band estimada, nivel percibido

**Punto de calibración**:
Los mocks sentados del British Council. Verifican si la dificultad de la biblioteca no oficial es
representativa: si la banda de la biblioteca se desvía mucho de la del BC, se corrige la estimación.
_Avoid_: control, chequeo, validación

**Lista de autoevaluación**:
La lista corta derivada de los descriptores oficiales de IELTS para Writing y Speaking. Es una
**traducción** de los descriptores del examinador, no una rúbrica propia — inventar una daría dos
estándares y el riesgo de que el propio sea más laxo que el del examen real.
_Avoid_: rúbrica, checklist, criterios

**Acento de producción**:
El acento que se practica al producir habla: americano. No es el único que se escucha — el
listening exige variedad británica, australiana y neozelandesa además del americano.
_Avoid_: acento, pronunciación americana
