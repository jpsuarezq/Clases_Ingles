# Schema 0001 — `datos.md` y `registro.md`

Contrato entre el **generador**, la **plantilla** y el **agregador**.

- `datos.md` → **fuente**. Lo escribe el generador, lo consume la plantilla.
- `ejercicio.html` → **generado**. Nunca se edita a mano (ADR 0001).
- `registro.md` → **bitácora**. Lo escribes tú; el agregador lo lee.

Cada campo cita el ticket que lo decidió. **Ningún campo de este documento es inventado acá.**

---

## 1. Por qué dos archivos y no uno

`datos.md` es **lo que se estudia**. `registro.md` es **lo que pasó**. Están separados porque la
plantilla necesita leer uno sin pisar el otro: el HTML se regenera las 90 veces que quieras, y tu
registro no se toca.

`datos.md` usa **frontmatter YAML + cuerpo markdown**. El frontmatter lleva todo lo estructurado —
lo que la plantilla debe renderizar sin ambigüedad. El cuerpo lleva **solo la explicación en
prosa** (el *por qué* articulatorio), que es lo único que no se puede expresar como dato.
`_10`

---

## 2. `ejercicios/dia-NNN/datos.md`

Carpeta por día, **solo el número, nunca fecha** — el plan es secuencia, no calendario. `_10`

### 2.1 Identidad

| Campo | Tipo | Notas |
| --- | --- | --- |
| `dia` | int 1–90 | El número de la carpeta. |
| `semana` | int 1–13 | `ceil(dia / 7)`. |
| `habilidad` | `listening \| reading \| writing \| speaking` \| `null` | El bloque rotante del día. `_14` Rotación `L → W → S → R` fija, a partes iguales. `_13` **`null` solo el día 90**: el EF SET de cierre cubre las **cuatro** habilidades en 90 minutos, no es un día de rotación. |
| `drill` | slug | El drill semanal de sección. `_13` |
| `mock` | int 1–3 \| `null` | **Solo** semanas 4, 10 y 13. `_13` |

### 2.2 `base_fija` — va los 90 días, sin excepción

| Campo | Tipo | Notas |
| --- | --- | --- |
| `anki_nuevas` | int | **6**, fijo. `_11` |
| `fonema.bloque` | `1 \| 2 \| 3` | 1 sistema · 2 vocales · 3 controvertidos. `_9` |
| `fonema.contraste` | slug | El contraste del bloque. `_9` |
| `fonema.etapa` | `explicacion \| percepcion \| produccion \| consolidacion` | El orden interno de cada bloque es fijo. `_9` |
| `fonema.elsa` | bool | `true` **solo 2 de los 6 días** del bloque. `_9` |

> **Por qué `elsa` es un booleano y no parte de `etapa`.** ELSA es percepción con feedback, y el
> research marca *"el trabajo solo perceptual es la peor inversión si el objetivo es producir"*. Si
> el drill fuera solo ELSA, el 100% de los días sería percepción. El booleano hace visible que el
> phonema **no** va al Anki `_11` y que la producción ocupa 2 de 6 días.

### 2.3 `ejercicio` — el bloque rotante

| Campo | Tipo | Notas |
| --- | --- | --- |
| `objetivo` | string | Una línea, en español. |
| `items[]` | lista | Cada ítem es una pregunta. |
| `items[].tipo` | `listening \| reading \| writing \| speaking` | Coincide con `habilidad`. |
| `items[].instruccion` | string | `"Escuchá (o leé) la frase dos veces antes de responder."` |
| `items[].stimulus` | string | El texto o la transcripción. |
| `items[].audio` | `{uk, us}` \| `null` | Rutas relativas. `null` mientras no se resuelva el audio. `_7` |
| `items[].opciones[]` | `{letra, texto}` | Cuatro. |
| `items[].correcta` | `A \| B \| C \| D` | |
| `items[].por_que` | string | Va al panel derecho, **siempre visible**. `_14` |

### 2.4 `coloquial` y `vocabulario` — no son lo mismo

**`coloquial`** es lo que se muestra debajo del ejercicio en UK↔US. `_14`

**`vocabulario`** son las **6 cards de Anki** del día. `_11`

| Campo | Tipo | Notas |
| --- | --- | --- |
| `vocabulario[].palabra` | string | |
| `vocabulario[].fuente` | `material \| frecuencia` | Mezcla: el material da contexto, la lista de frecuencia garantiza el núcleo. `_11` |
| `vocabulario[].frase` | string | **La frase coloquial completa, no la palabra suelta** — el frente de la card. `_11` |
| `vocabulario[].uk` / `.us` | string | El par obligatorio. `_17` |
| `vocabulario[].sentido` | string | En español. |

### 2.5 `writing` — solo en días de writing

| Campo | Tipo | Notas |
| --- | --- | --- |
| `tarea` | `task_1 \| task_2` | Task 2 es el default de práctica; Task 1 va al drill semanal. `_8` |
| `consigna` | string | La pregunta del examen. |
| `min_palabras` | int | 150 en Task 1, 250 en Task 2. `_8` |

### 2.6 Cuerpo markdown

La **única** prosa del archivo: el *por qué* articulatorio del phonema del día. Se inyecta
tal cual en el panel derecho.

---

## 3. `ejercicios/dia-NNN/registro.md`

Frontmatter YAML estricto arriba, **nota libre abajo**. `_10`

```yaml
---
fecha: null            # se completa al hacer el día; repetir el día la sobreescribe
dia: 1
semana: 1
habilidad: listening

base:
  anki_retenidas: null # de las 6
  fonema_practicado: null
  elsa_score: null

ejercicio:
  aciertos: null
  total: 4

writing: null          # objeto solo en días de writing; null en los demás
medicion:
  banda_medida: null         # L+R, COMPUTADA — contra esta se mide la meta
  nivel_autoevaluado: null   # W+S, TENDENCIA — nunca da por cumplida la meta
  band_fuente: null          # computada | autoevaluada | null
---
```

> **`band_fuente` no es decorativo.** Sin él el agregador no distingue **lo medido de lo opinado**,
> y los dos se promediarían — que es exactamente lo que #12 prohibió. `_12`

`writing`, cuando existe:

```yaml
writing:
  tarea: task_2
  criterios:
    task_response: null               # 25%
    coherence_cohesion: null          # 25%
    lexical_resource: null            # 25%
    grammatical_range_accuracy: null  # 25%
  evidencia: ""    # CITA OBLIGATORIA — si no hay cita literal, no hay nota. _8
  accion: ""       # UNA acción concreta. Sin rewrite sugerido. _8
```

---

## 4. Lo que este esquema **no** resuelve todavía

Declarado, no escondido:

- **Las rutas de audio** (`items[].audio`) quedan en `null`. #7 eligió las fuentes, pero nadie
  decidió todavía cómo se obtienen ni dónde viven los archivos.
- **La rotación exacta de `habilidad`** por día. #14 fijó *que* rota y que hay base fija; el
  orden concreto lo decide el drill de #13.
- **La fórmula que llena `banda_medida`.** #12 definió las dos pistas y las tablas raw→band; la
  conversión implementada todavía no existe.
