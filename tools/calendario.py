#!/usr/bin/env python3
"""El calendario: dado un día 1–90, qué toca.

Tres fuentes, cero invención:

- **Rotación `L → W → S → R`** cíclica fija, a partes iguales (#13). Ponderar hacia
  L y R *"daría el metric y no el idioma"*.
- **Secuencia fonética** en tres bloques de 30, cada uno en cinco tramos de 6 días (#9),
  con el orden interno fijo `explicación → percepción → producción → consolidación`.
- **Mocks**: semanas 4 y 10 (BC, L+R en dos días consecutivos por el techo de 60 min)
  y semana 13 (EF SET, el ancla de cierre). #13.

Lo único que #13 no fijó es **qué día dentro de la semana** cae el mock. Acá va al
**final de la semana**, para que el drill de sección de esa semana lo preceda.
"""

ROTACION = ["listening", "writing", "speaking", "reading"]  # #13

ETAPAS = ["explicacion", "percepcion", "percepcion", "produccion", "produccion", "consolidacion"]

# (nombre, [5 tramos de 6 días]) — el orden de #9, que va de más a menos evidencia.
FASES = [
    ("1 · el sistema, no los fonemas", [
        ("acento-lexico",       "El error raíz: qué sílaba se acentúa y por qué se estira."),
        ("schwa",               "El fonema más frecuente del inglés: la sílaba no acentuada se apaga."),
        ("function-words",      "to, for, and, of, can — en inglés se aplastan; en español reciben vocal completa."),
        ("ritmo-chunking-linking", "Lo que IELTS nombra explícitamente en los indicadores de Pronunciación."),
        ("consolidacion",       "Shadowing de frases completas integrando todo el bloque."),
    ]),
    ("2 · las vocales que cambian el significado", [
        ("i-versus-i-larga",    "/ɪ/ vs /iː/ — ship/sheep, live/leave, slip/sleep."),
        ("ae-versus-e",         "/æ/ vs /e/ — bad/bed, man/men."),
        ("a-versus-schwa",      "/ʌ/ vs /ə/ — el contraste entre la vocal tónica y el schwa."),
        ("consonantes-finales", "Presencia de cierre y release: importa más que la voicing completa."),
        ("consolidacion",       "Consolidación del bloque de vocales."),
    ]),
    ("3 · los controvertidos y la integración", [
        ("th",                  "/θ/ y /ð/ — a propósito tarde: priorizarlo es «defendible pero discutido»."),
        ("t-d-tap",             "/t/, /d/ y la tap intervocálica — español dentales, inglés alveolares."),
        ("sonidos-debiles",     "/s/-/z/, /x/-/h/, /b/-/v/ — documentadas pero débilmente evidenciadas."),
        ("j-versus-dzh",        "/j/-/dʒ/ — al final: solo aparece en fuentes pedagógicas, sin estudio controlado."),
        ("integracion",         "Integración y auto-evaluación."),
    ]),
]

# Semana → (días, tipo). Semanas 4 y 10 duran dos días porque el BC son 1 h 40 (#13).
MOCKS = {
    4:  {"dias": [27, 28], "tipo": "bc-ielts-ready", "skills": ["listening", "reading"]},
    10: {"dias": [69, 70], "tipo": "bc-ielts-ready", "skills": ["listening", "reading"]},
    13: {"dias": [90],     "tipo": "ef-set-4-skills", "skills": ROTACION[:]},
}


def semana(dia: int) -> int:
    return -(-dia // 7)


def habilidad(dia: int):
    """La habilidad del día. El mock toma el día; si no, manda la rotación (#13).

    Devuelve `None` el día del EF SET de cierre: es una prueba de **las cuatro**
    habilidades en 90 minutos, no un día de rotación. Preguntarle su habilidad
    sería mentir sobre ese día.
    """
    for m in MOCKS.values():
        if dia in m["dias"]:
            if m["tipo"] == "ef-set-4-skills":
                return None
            return m["skills"][m["dias"].index(dia)]
    return ROTACION[(dia - 1) % 4]


def fonema(dia: int) -> dict:
    """Bloque, contraste, etapa y si va ELSA (#9)."""
    idx = (dia - 1) // 6
    offset = (dia - 1) % 6
    fase_i, tramo_i = divmod(idx, 5)
    fase, tramos = FASES[fase_i]
    contraste, descripcion = tramos[tramo_i]
    return {
        "bloque": fase_i + 1,
        "fase": fase,
        "contraste": contraste,
        "descripcion": descripcion,
        "dia_en_bloque": offset + 1,
        "etapa": ETAPAS[offset],
        # ELSA es percepción con feedback, y eso ocupa 2 de los 6 días (#9).
        # Los otros 4 son producción y consolidación: "el trabajo solo perceptual
        # es la peor inversión si el objetivo es producir".
        "elsa": ETAPAS[offset] == "percepcion",
    }


def mock(dia: int):
    """El mock que ocupa ese día, o None."""
    for semana_n, m in MOCKS.items():
        if dia in m["dias"]:
            return {"semana": semana_n, "tipo": m["tipo"], "paso": m["dias"].index(dia) + 1}
    return None


def dia_de_drill(dia: int) -> bool:
    """¿Es día de drill de sección? Todas las semanas, dentro del día de la skill (#13)."""
    return mock(dia) is None


def main():
    print(f"{'día':>3} {'sem':>3} {'habilidad':<10} {'bloque':>6} {'contraste':<24} {'etapa':<14} mock")
    print("─" * 88)
    for d in range(1, 91):
        f, m, h = fonema(d), mock(d), habilidad(d)
        print(f"{d:>3} {semana(d):>3} {(h or '— las 4 —'):<10} {f['bloque']:>6} "
              f"{f['contraste']:<24} {f['etapa']:<14} "
              f"{m['tipo'] if m else ''}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
