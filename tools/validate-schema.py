#!/usr/bin/env python3
"""Valida `ejercicios/dia-NNN/{datos.md, registro.md}` contra el schema 0001.

Contrato: docs/schema/0001-datos-y-registro.md

Sale con 1 si algo falla, 0 si todo pasa. Corre sobre todos los `ejercicios/dia-*`
que encuentre, así que sirve igual con 1 carpeta que con 90.
"""

import re
import sys
from pathlib import Path

import yaml

HABILIDADES = {"listening", "reading", "writing", "speaking"}
ETAPAS = {"explicacion", "percepcion", "produccion", "consolidacion"}
FUENTES = {"material", "frecuencia"}
TIPOS = HABILIDADES
LETRAS = {"A", "B", "C", "D"}
FUENTE_BAND = {"computada", "autoevaluada"}
CRITERIOS = (
    "task_response",
    "coherence_cohesion",
    "lexical_resource",
    "grammatical_range_accuracy",
)


def frontmatter(path: Path):
    """Devuelve (frontmatter_dict, cuerpo_markdown, error_de_yaml).

    `error_de_yaml` es None si parseó. Si no parseó, trae el detalle de la línea —
    un "frontmatter ilegible" a secas le dice al usuario que algo falló, pero no dónde.
    """
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n?(.*)\Z", text, re.S)
    if not m:
        return None, None, "no arranca con '---' y cierra con '---'"
    try:
        return yaml.safe_load(m.group(1)), m.group(2), None
    except yaml.YAMLError as e:
        return None, None, str(e).replace("\n", " ")


def err(errors: Path, msg: str):
    errors.append(msg)


def validar_datos(path: Path, errors: list):
    fm, body, yerr = frontmatter(path)
    if fm is None:
        return err(errors, f"datos.md: frontmatter ilegible — {yerr}")

    dia = fm.get("dia")
    if not isinstance(dia, int) or not 1 <= dia <= 90:
        err(errors, f"datos.md: 'dia' debe ser int 1–90, llegó {dia!r}")

    semana = fm.get("semana")
    if isinstance(dia, int) and semana != -(-dia // 7):
        err(errors, f"datos.md: 'semana' inconsistente — dia {dia} debería ser semana {-(-dia // 7)}, llegó {semana!r}")

    if fm.get("habilidad") not in HABILIDADES:
        err(errors, f"datos.md: 'habilidad' debe ser {sorted(HABILIDADES)}, llegó {fm.get('habilidad')!r}")

    if fm.get("mock") is not None and fm.get("mock") not in (1, 2, 3):
        err(errors, f"datos.md: 'mock' debe ser 1|2|3|null, llegó {fm.get('mock')!r}")

    # --- base_fija ---
    base = fm.get("base_fija") or {}
    if base.get("anki_nuevas") != 6:
        err(errors, f"datos.md: base_fija.anki_nuevas está fijado en 6 (#11), llegó {base.get('anki_nuevas')!r}")

    fon = base.get("fonema") or {}
    if fon.get("bloque") not in (1, 2, 3):
        err(errors, f"datos.md: fonema.bloque debe ser 1|2|3, llegó {fon.get('bloque')!r}")
    if fon.get("etapa") not in ETAPAS:
        err(errors, f"datos.md: fonema.etapa debe ser {sorted(ETAPAS)}, llegó {fon.get('etapa')!r}")
    if not isinstance(fon.get("elsa"), bool):
        err(errors, "datos.md: fonema.elsa debe ser booleano")
    if not fon.get("contraste"):
        err(errors, "datos.md: fonema.contraste falta")

    # --- ejercicio ---
    items = (fm.get("ejercicio") or {}).get("items")
    if not isinstance(items, list) or not items:
        return err(errors, "datos.md: ejercicio.items debe ser una lista no vacía")

    scoreables = 0
    for i, it in enumerate(items, 1):
        if it.get("tipo") not in TIPOS:
            err(errors, f"datos.md: items[{i}].tipo debe ser {sorted(TIPOS)}, llegó {it.get('tipo')!r}")
        if not it.get("instruccion"):
            err(errors, f"datos.md: items[{i}].instruccion falta")
        if not it.get("por_que"):
            err(errors, f"datos.md: items[{i}].por_que falta — es lo que va al panel derecho (#14)")

        opts = it.get("opciones") or []
        corr = it.get("correcta")

        if corr is not None:
            scoreables += 1
            if corr not in LETRAS:
                err(errors, f"datos.md: items[{i}].correcta debe ser A|B|C|D, llegó {corr!r}")
            if len(opts) != 4:
                err(errors, f"datos.md: items[{i}] con respuesta correcta necesita 4 opciones, llegó {len(opts)}")
            for o in opts:
                if set(o) != {"letra", "texto"}:
                    err(errors, f"datos.md: items[{i}].opciones debe ser {{letra, texto}}, llegó {sorted(o)}")
        elif opts:
            err(errors, f"datos.md: items[{i}] tiene opciones pero no 'correcta' — ¿qué responde el alumno?")

    if scoreables == 0:
        err(errors, "datos.md: ningún ítem es evaluable — el día no tendría aciertos que registrar")

    # --- coloquial / vocabulario ---
    vocab = fm.get("vocabulario")
    if not isinstance(vocab, list) or len(vocab) != 6:
        err(errors, f"datos.md: vocabulario debe tener exactamente 6 (#11), llegó {len(vocab) if isinstance(vocab, list) else vocab!r}")
    else:
        for j, v in enumerate(vocab, 1):
            for campo in ("palabra", "frase", "uk", "us", "sentido"):
                if not v.get(campo):
                    err(errors, f"datos.md: vocabulario[{j}].{campo} falta")
            if v.get("fuente") not in FUENTES:
                err(errors, f"datos.md: vocabulario[{j}].fuente debe ser {sorted(FUENTES)}, llegó {v.get('fuente')!r}")

    coloq = fm.get("coloquial")
    if not isinstance(coloq, list):
        err(errors, "datos.md: 'coloquial' debe ser una lista")
    else:
        for k, c in enumerate(coloq, 1):
            if set(c) != {"expr", "uk", "us", "sentido"}:
                err(errors, f"datos.md: coloquial[{k}] debe ser {{expr, uk, us, sentido}}, llegó {sorted(c)}")

    if fm.get("habilidad") == "writing":
        w = fm.get("writing")
        if not isinstance(w, dict):
            err(errors, "datos.md: habilidad=writing exige bloque 'writing'")
        else:
            if w.get("tarea") not in ("task_1", "task_2"):
                err(errors, f"datos.md: writing.tarea debe ser task_1|task_2, llegó {w.get('tarea')!r}")
            esperado = 150 if w.get("tarea") == "task_1" else 250
            if w.get("min_palabras") != esperado:
                err(errors, f"datos.md: writing.min_palabras para {w.get('tarea')} es {esperado} (#8), llegó {w.get('min_palabras')!r}")

    if not (body or "").strip():
        err(errors, "datos.md: el cuerpo markdown está vacío — es el por qué articulatorio del día")
    return scoreables


def validar_registro(path: Path, datos: dict | None, scoreables: int | None, errors: list):
    fm, body, yerr = frontmatter(path)
    if fm is None:
        return err(errors, f"registro.md: frontmatter ilegible — {yerr}")

    fecha = fm.get("fecha")
    if fecha is not None and not hasattr(fecha, "year"):
        err(errors, f"registro.md: 'fecha' debe ser fecha u null, llegó {fecha!r}")

    if datos:
        for campo in ("dia", "semana", "habilidad"):
            if fm.get(campo) != datos.get(campo):
                err(errors, f"registro.md: '{campo}' no coincide con datos.md ({datos.get(campo)!r} vs {fm.get(campo)!r})")

    base = fm.get("base") or {}
    if base.get("anki_retenidas") is not None and not isinstance(base.get("anki_retenidas"), int):
        err(errors, "registro.md: base.anki_retenidas debe ser int u null")

    ej = fm.get("ejercicio") or {}
    if ej.get("total") is not None and scoreables is not None and ej.get("total") != scoreables:
        err(errors, f"registro.md: ejercicio.total ({ej.get('total')}) no coincide con los ítems evaluables de datos.md ({scoreables})")

    med = fm.get("medicion") or {}
    bm, na, bf = med.get("banda_medida"), med.get("nivel_autoevaluado"), med.get("band_fuente")

    if bm is not None and not (0.0 <= float(bm) <= 9.0):
        err(errors, f"registro.md: medicion.banda_medida fuera de rango 0–9: {bm!r}")
    if na is not None and not (0.0 <= float(na) <= 9.0):
        err(errors, f"registro.md: medicion.nivel_autoevaluado fuera de rango 0–9: {na!r}")

    # La regla que #12 puso y que este chequeo defiende.
    if bm is not None and na is not None:
        err(errors, "registro.md: banda_medida y nivel_autoevaluado en el mismo registro — #12 prohibió promediar las dos pistas")
    if (bm is None) != (bf != "computada"):
        err(errors, f"registro.md: band_fuente='computada' va SOLO con banda_medida (L+R). llegó bf={bf!r}, bm={bm!r}")
    if bf is not None and bf not in FUENTE_BAND:
        err(errors, f"registro.md: band_fuente debe ser {sorted(FUENTE_BAND)} o null, llegó {bf!r}")

    if fm.get("habilidad") == "writing":
        w = fm.get("writing")
        if not isinstance(w, dict):
            err(errors, "registro.md: habilidad=writing exige bloque 'writing', llegó null")
        else:
            crit = w.get("criterios") or {}
            for c in CRITERIOS:
                if c not in crit:
                    err(errors, f"registro.md: writing.criterios.{c} falta (los 4 oficiales, 25% cada uno — #8)")
            if not (w.get("evidencia") or "").strip():
                err(errors, "registro.md: writing.evidencia vacía — cita obligatoria; sin cita no hay nota (#8)")
            if not (w.get("accion") or "").strip():
                err(errors, "registro.md: writing.accion vacía — debe dar UNA acción concreta (#8)")
    elif fm.get("writing") is not None:
        err(errors, "registro.md: 'writing' no nulo en un día que no es de writing")

    if not (body or "").strip():
        err(errors, "registro.md: la nota libre está vacía")


def main():
    raiz = Path(__file__).resolve().parent.parent
    carpetas = sorted((raiz / "ejercicios").glob("dia-*"))
    if not carpetas:
        print("no hay carpetas en ejercicios/", file=sys.stderr)
        return 1

    fallos = 0
    for carpeta in carpetas:
        errors: list = []
        d, r = carpeta / "datos.md", carpeta / "registro.md"
        scoreables = validar_datos(d, errors) if d.exists() else err(errors, "datos.md falta")
        datos = frontmatter(d)[0] if d.exists() else None
        if r.exists():
            validar_registro(r, datos, scoreables, errors)
        else:
            errors.append("registro.md falta")

        if errors:
            fallos += 1
            print(f"\n✗ {carpeta.name}")
            for e in errors:
                print(f"    {e}")
        else:
            print(f"✓ {carpeta.name}")

    print(f"\n{len(carpetas) - fallos}/{len(carpetas)} carpetas válidas")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
