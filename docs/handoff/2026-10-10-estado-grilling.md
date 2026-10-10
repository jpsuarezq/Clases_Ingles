# Handoff — Clases_Ingles / effort A2→B2→IELTS

**Fecha:** 2026-10-10
**Estado:** wayfinder charting, en pausa a mitad de la Ronda 3 del grilling. **No hay mapa creado todavía.**
**Próxima sesión:** responder Q13–Q17, nombrar el destino, y arrancar el charting real (crear mapa + tickets + blocking).

> Los números `Q1`–`Q17` de este documento usan **la numeración del grilling de esta sesión**
> (Ronda 1 = Q1–Q6, Ronda 2 = Q7–Q12, Ronda 3 = Q13–Q17).

---

## 1. Qué es este esfuerzo

Diseñar un programa de inglés de 13 semanas para llevar a una persona de A2 hacia B2, orientado a
**IELTS Academic**, con ejercicios diarios repartidos en reading, writing, speaking y listening.
El output es una **bitácora personal** (no un curso publicable): el repo registra el avance real de
una persona con ~30–60 min/día.

Enfoque pedido explícitamente por el usuario:
- Método lo más **sencillo posible** para alguien que se le dificulta
- Ejercicios **interactivos y explicativos** (no listas de ejercicios mecánicos)
- **Frases coloquiales** del inglés real en todo el material
- Speaking: **fonemas** con ejercicios prácticas específicas para **hablantes de español**
- Recursos de internet accesibles, tips de aprendizaje

## 2. Estado del entorno (ya hecho, no rehacer)

| Qué | Estado |
| --- | --- |
| `gh` 2.102.0 | instalado, autenticado como `jpsuarezq`, scopes `gist,read:org,repo` |
| credential helper | `gh auth setup-git` ejecutado → `~/.gitconfig` |
| Skills de Matt Pocock | 38 instaladas global en `~/.agents/skills/` |
| Repo | `github.com/jpsuarezq/Clases_Ingles`, público, branch `main` |
| Config de agents | commit `136dd12` — ver `AGENTS.md` y `docs/agents/` |
| Labels | 5 de triage + 5 `wayfinder:*` creados en GitHub |

⚠️ **Node:** el `node` por default es v20.20.2 (instalación manual en `/usr/local/bin`) y está
**tapando** al v22.22.1 de apt en `/usr/bin/node`. Para correr `npx`:
`PATH=/usr/bin:$PATH npx ...`

## 3. La restricción que domina todo

**Presupuesto: ≤60 min/día, 7 días/semana, 13 semanas → ~91 h techo, ~65–70 h realista.**

Eso está **muy por debajo** de las ~200 h guiadas que el objetivo IELTS band 7–8 exige desde A2.
De ahí que el destino (Q13) tenga que redefinirse con honestidad. La aritmética es firme; los
números exactos de referencia los traen las investigaciones de §7.

## 4. Decisiones ya cerradas

| # | Pregunta | Respuesta |
| --- | --- | --- |
| Q1 | La promesa de los 3 meses | "Implica lo que sea necesario" — el research define la honestidad del marco |
| Q2 | Quién es el estudiante | Es para el usuario, **pero el material debe servir para cualquiera** |
| Q3 | Presupuesto diario | 30 min/día como piso |
| Q4 | Qué significa "A2" hoy | **No hay test.** Es solo un punto de partida percibido |
| Q5 | Qué significa "B2" al final | Objetivo **IELTS**; para medir, tests gratuitos (Cambridge One, EF SET, Duolingo) |
| Q6 | Recursos y dinero | **ELSA Speak Pro** + algunos PDFs; el resto, recursos de internet accesibles y fáciles, con tips |
| Q7 | ¿30 min techo o mínimo? | "El tiempo que sea necesario, pero **máximo 1 hora por día**" |
| Q8 | ¿5 días o 7? | **Los 7 días** |
| Q9 | Prioridad entre habilidades | **Rotar por día de semana** (con base fija diaria, propuesta en §6) |
| Q10 | ¿Repo curso o bitácora? | **(b) Bitácora personal** |
| Q11 | ¿SRS / Anki? | **Sí**, si lo recomiendo |
| Q12 | ¿IELTS académico o general? | **Academic** |

**Contexto personal:** usuario hispanohablante, se percibe A2 sin test de respaldo.
Tiene ELSA Speak Pro y algunos libros en PDF (títulos pedidos en Q15, **no respondidos**).

## 5. Preguntas abiertas — ESPERANDO RESPUESTA

> **Q13 · El destino.** *(a)* Plan de 13 semanas + baseline medido + horizonte IELTS mapeado, con
> diagnóstico en las semanas 0–1 — **recomendado**; (b) plan orientado a readiness completo de IELTS
> — riesgo alto; (c) sprint de diagnóstico puro y re-planificación después.
> **Esta es la que bloquea todo lo demás.**

> **Q14 · Rotación semanal.** ¿Aceptás la rotación con base fija de §6, o el research de §7 sugiere
> algo mejor?

> **Q15 · Los PDFs.** Títulos exactos. Importa por copyright (repo público) y por variante
> British/American.

> **Q16 · Métricas semanales.** Propuesta: score ELSA + band IELTS de la sección del día + retención
> SRS. Falta confirmar.

> **Q17 · Variante British/American.** Propuesta: **British**, para no pelearse con la variante de
> IELTS. **Sin responder.**

## 6. Propuesta de rotación semanal (pendiente de Q14)

```
Base fija diaria (~10-15 min):  Vocabulario SRS (Anki) + review de pronunciación del día

Lunes     → Reading    45 min
Martes    → Writing    45 min
Miércoles → Listening  45 min
Jueves    → Speaking   45 min   (ELSA: fonema del día + shadowing)
Viernes   → Speaking   45 min   (día fuerte: shadowing + IELTS speaking parts)
Sábado    → Listening  45 min   (sección 4 del IELTS, la que más pesa)
Domingo   → Review     45 min   (mock semanal + repaso)
```

## 7. Investigación en vuelo

Dos subagentes corriendo en background. Cuando reporten, **no re-lanzar**:

| Sesión | Qué responde |
| --- | --- |
| `ses_edb722f2dffeCzYKYqq3YFnEpA` | Horas guiadas CEFR A2→B2 · si B2 es per-skill o unificado · descriptores can-do B2 (CEFR Companion 2020) · qué es alcanzable en 90–135 h · prioridades fonéticas del hablante de español |
| `ses_edb673f65ffegkYsb9Mqn9YRgi` | Blocked vs interleaved practice · duración y frecuencia de sesión · SRS/retrieval practice y ritmo de repaso · métodos de entrenamiento fonético que funcionan · evidencia sobre ELSA Speak y Duolingo · si 30–45 min diarios alcanzan |

Al aterrizar, sus hallazgos alimentan Q14 y Q16, y probablemente 2 tickets `wayfinder:research`.

## 8. Qué falta hacer después de esta pausa

1. Responder Q13–Q17 con el usuario.
2. **Nombrar el destino** (wayfinder paso 1, con grilling + domain-modeling).
3. Ronda 4 del grilling: **mapear el frontier**, breadth-first, para superficiear el resto de decisiones.
4. Crear el mapa: issue con label `wayfinder:map`.
5. Crear tickets hijos con labels `wayfinder:research|prototype|grilling|task`.
6. **Cablear blocking en una segunda pasada** (los issues necesitan ids antes de referenciarse).
7. Recién ahí: charting cierra la sesión. Charting no resuelve ningún ticket.

## 9. Suggested skills para el próximo agente

| Skill | Cuándo |
| --- | --- |
| `wayfinder` | Gobierna toda la sesión. Leer primero |
| `grilling` | Rondas 3 y 4 del charting. Llamarlo junto con `domain-modeling` |
| `domain-modeling` | Cada vez que se fije un término. Al chartar va a haber que escribir `GLOSSARY.md` |
| `research` | Para los dos subagentes de §7 y los tickets de research que surjan |
| `setup-matt-pocock-skills` | **Ya corrido.** No re-lanzar |

## 10. Notas de dominio para `GLOSSARY.md`

Cuando se armen los primeros tickets, estos términos necesitan definición canónica:
**habilidad** (reading/writing/speaking/listening — ¿se practican o se evalúan?), **ejercicio
interactivo** (¿con feedback? ¿autoevaluado?), **fonema vs fonética**, **frase coloquial**,
**baseline**, **SRS**, **band score**, **rotación** (blocked vs interleaved).