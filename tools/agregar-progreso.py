#!/usr/bin/env python3
"""Agrega `ejercicios/dia-*/registro.md` en `progreso.md`.

La regla que gobierna todo esto es la de #12: **dos pistas de medición que nunca
se promedian**. `banda_medida` (L+R, computada) es contra la que se mide la meta.
`nivel_autoevaluado` (W+S) sirve para tendencia y **nunca da por cumplida la meta**.

Sale con 1 si algo falla.
"""

import statistics
import sys
from datetime import date
from pathlib import Path

import yaml

META_CIERRE = 5.0          # #13 — band de cierre a las 13 semanas
CRITERIOS = [
    ("task_response", "Task Response"),
    ("coherence_cohesion", "Coherence & Cohesion"),
    ("lexical_resource", "Lexical Resource"),
    ("grammatical_range_accuracy", "Grammatical Range & Acc."),
]
HABILIDADES = ["listening", "reading", "writing", "speaking"]


def frontmatter(path: Path):
    import re
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None


def media(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.mean(xs), 1) if xs else None


def tabla(filas, cab):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    out += ["| " + " | ".join(str(c) for c in f) + " |" for f in filas]
    return "\n".join(out)


def main():
    raiz = Path(__file__).resolve().parent.parent
    registros = []
    rotos = []
    for carpeta in sorted((raiz / "ejercicios").glob("dia-*")):
        r = carpeta / "registro.md"
        if not r.exists():
            rotos.append((carpeta.name, "falta registro.md"))
            continue
        fm = frontmatter(r)
        if fm is None:
            rotos.append((carpeta.name, "registro.md sin frontmatter YAML legible"))
            continue
        fm["_carpeta"] = carpeta.name
        registros.append(fm)

    registros.sort(key=lambda x: (x.get("dia") or 0))
    hechos = [r for r in registros if r.get("fecha") is not None]

    # ───────── cabecera ─────────
    L = ["# Progreso", "",
         f"**{len(hechos)} de 90 días registrados** · {round(len(hechos) / 90 * 100)}%", ""]

    # ───────── racha ─────────
    fechas = sorted(r["fecha"] for r in hechos)
    racha, mejor = 0, 0
    for a, b in zip(fechas, fechas[1:]):
        racha = racha + 1 if (b - a).days == 1 else 0
        mejor = max(mejor, racha)
    L += ["## Consistencia", "",
          "Lo que la investigación midió como predictora de progreso fue **lecciones completadas**,"
          " no minutos totales (Sudina & Plonsky, 287 aprendices).", "",
          f"- **Último día registrado:** {fechas[-1] if fechas else '—'}",
          f"- **Mejor racha:** {mejor + 1 if fechas else 0} días seguidos",
          f"- **Días registrados sin fecha:** {len(registros) - len(hechos)}", ""]

    # ───────── por habilidad ─────────
    filas = []
    for h in HABILIDADES:
        hs = [r for r in hechos if r.get("habilidad") == h]
        acu = [(r.get("ejercicio") or {}).get("aciertos") for r in hs]
        tot = [(r.get("ejercicio") or {}).get("total") for r in hs]
        a, t = sum(x for x in acu if x), sum(x for x in tot if x)
        filas.append([
            h, len(hs),
            f"{a} / {t}" if t else "—",
            f"{round(a / t * 100)}%" if t else "—",
        ])
    L += ["## Por habilidad", "", tabla(filas, ["Habilidad", "Días", "Aciertos", "Tasa"]), "",
          "> Los aciertos **no miden** speaking ni writing: la producción no se auto-corrige."
          " Ahí mandan `elsa_score` y la rúbrica de #8.", ""]

    # ───────── vocabulario y pronunciación ─────────
    ret = [(r.get("base") or {}).get("anki_retenidas") for r in hechos]
    ret = [x for x in ret if x is not None]
    L += ["## Vocabulario y pronunciación", "",
          f"- **Anki:** {sum(ret)} retenidas de {6 * len(ret)} intentos"
          + (f" — {round(sum(ret) / (6 * len(ret)) * 100)}%" if ret else ""),
          f"- **Fonemas practicados:** {sum(1 for r in hechos if (r.get('base') or {}).get('fonema_practicado'))}"
          f" de {len(hechos)} días registrados", ""]

    elsa = [(r["fecha"], (r.get("base") or {}).get("elsa_score")) for r in hechos]
    elsa = [(f, e) for f, e in elsa if e is not None]
    if elsa:
        L += [tabla([[str(f), e] for f, e in elsa], ["Fecha", "ELSA"]), ""]

    # ───────── LA SECCIÓN QUE #12 PROTEGE ─────────
    L += ["## Medición", "",
          "**Dos pistas que nunca se promedian** (#12). Contra la primera se mide la meta;"
          " la segunda sirve para ver la tendencia y **no puede dar por cumplida la meta**.", ""]

    med = [r.get("medicion") or {} for r in hechos]
    bm = [(r["fecha"], m.get("banda_medida")) for r, m in zip(hechos, med)
          if m.get("banda_medida") is not None]
    na = [(r["fecha"], m.get("nivel_autoevaluado")) for r, m in zip(hechos, med)
          if m.get("nivel_autoevaluado") is not None]

    L += [f"### Banda medida (L+R) · contra esta se mide la meta de {META_CIERRE}", ""]
    L += [tabla([[str(f), b, "computada"] for f, b in bm], ["Fecha", "Band", "Fuente"])
          if bm else "_Sin mediciones todavía._", ""]
    if bm:
        L += [f"Última: **{bm[-1][1]}** — faltan **{round(META_CIERRE - bm[-1][1], 1)}** para la meta.", ""]
    else:
        L += [f"Ningún registro tiene `banda_medida`, así que **la meta de {META_CIERRE} todavía no se"
              " puede evaluar**. Se llena con el formulario semanal de la biblioteca no oficial (#12).", ""]

    L += ["### Nivel autoevaluado (W+S) · tendencia", ""]
    L += [tabla([[str(f), n, "autoevaluada"] for f, n in na], ["Fecha", "Nivel", "Fuente"])
          if na else "_Sin autoevaluaciones todavía._", ""]
    if na:
        L += [f"Tendencia: primera **{na[0][1]}** → última **{na[-1][1]}**"
              f" · media **{media([n for _, n in na])}**", ""]

    # ───────── writing: la rúbrica de #8, criterio por criterio ─────────
    wr = [r["writing"] for r in hechos
          if r.get("habilidad") == "writing" and isinstance(r.get("writing"), dict)]
    if wr:
        L += ["### Writing — los 4 criterios oficiales (#8)", ""]
        filas = []
        for k, nom in CRITERIOS:
            vals = [w.get("criterios", {}).get(k) for w in wr]
            filas.append([nom, "25%", len([v for v in vals if v is not None]),
                          media(vals) if any(v is not None for v in vals) else "—"])
        L += [tabla(filas, ["Criterio", "Peso", "n", "Media"]), ""]

        sin_cita = [w for w in wr if not str(w.get("evidencia") or "").strip()]
        if sin_cita:
            L += [f"> ⚠ **{len(sin_cita)} de {len(wr)}** correcciones de writing **no tienen"
                  " `evidencia` citada.** #8 es tajante: *sin cita no hay nota*. Esas notas no"
                  " deberían contar para la tendencia.", ""]

    # ───────── pendiente ─────────
    faltan = 90 - len(registros)
    L += ["## Pendiente", "",
          f"- **{faltan} días** sin carpeta todavía.", ""]
    if rotos:
        L += ["| Carpeta | Problema |", "|---|---|"]
        L += [f"| {c} | {p} |" for c, p in rotos]
        L.append("")

    (raiz / "progreso.md").write_text("\n".join(L), encoding="utf-8")
    print(f"✓ progreso.md — {len(hechos)} días registrados, {faltan} faltantes")
    if rotos:
        print(f"  ⚠ {len(rotos)} registros ilegibles")
    return 0


if __name__ == "__main__":
    sys.exit(main())
