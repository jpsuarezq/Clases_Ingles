#!/usr/bin/env python3
"""Une `tools/corpus/` con `tools/calendario.py` y escribe `ejercicios/dia-NNN/datos.md`.

**El calendario decide lo estructurado; el corpus aporta el contenido.**

- Calendar (automático, cero intervención): `dia`, `semana`, `habilidad`, `mock`,
  y toda la `base_fija` — bloque, contraste, etapa, ELSA (#9, #13).
- Corpus (redacción): los ítems, el coloquial, el vocabulario y el cuerpo en prosa.

Si a un día le falta contenido, **no escribe nada** y lo reporta. Un `datos.md` a
medias no es un día: es un archivo que parece listo y no lo está.

Uso:
    python3 tools/generar-datos.py            # solo los días completos
    python3 tools/generar-datos.py --reporte  # qué falta, sin escribir nada
"""

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calendario as C

# Todo ítem necesita instrucción y explicación. Las opciones y la respuesta correcta
# solo aplican a los evaluables: speaking/writing son de producción y no las tienen
# (validate-schema.py lo admite, y acá hay que ser igual de laxo para no rechazar
# un día de speaking que sí está completo).
REQUIRED_ITEMS = ("instruccion", "por_que")
REQUIRED_VOCAB = ("palabra", "fuente", "uk", "us", "frase", "sentido")


def cargar_corpus(raiz: Path) -> dict:
    f = raiz / "tools" / "corpus" / "dias.yaml"
    if not f.exists():
        return {}
    d = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    return {int(k): v for k, v in d.items() if v}


def validar_dia(n: int, c: dict) -> list[str]:
    faltan = []
    if not c.get("items"):
        faltan.append("items")
    else:
        for i, it in enumerate(c["items"], 1):
            for k in REQUIRED_ITEMS:
                if k not in it or it[k] in (None, "", []):
                    faltan.append(f"items[{i}].{k}")
            if it.get("correcta") not in (None, "A", "B", "C", "D"):
                faltan.append(f"items[{i}].correcta inválida")
            if it.get("correcta") and len(it.get("opciones") or []) != 4:
                faltan.append(f"items[{i}].opciones necesita 4")
        if not any(it.get("correcta") for it in c["items"]):
            faltan.append("al menos un ítem evaluable")
    if len(c.get("vocabulario") or []) != 6:
        faltan.append(f"vocabulario ({len(c.get('vocabulario') or [])}/6)")
    else:
        for i, v in enumerate(c["vocabulario"], 1):
            for k in REQUIRED_VOCAB:
                if not v.get(k):
                    faltan.append(f"vocabulario[{i}].{k}")
            if v.get("fuente") not in ("material", "frecuencia"):
                faltan.append(f"vocabulario[{i}].fuente")
    if not c.get("coloquial"):
        faltan.append("coloquial")
    else:
        for i, x in enumerate(c["coloquial"], 1):
            if set(x) != {"expr", "uk", "us", "sentido"}:
                faltan.append(f"coloquial[{i}] necesita expr/uk/us/sentido")
    if not (c.get("cuerpo") or "").strip():
        faltan.append("cuerpo")
    if not (c.get("objetivo") or "").strip():
        faltan.append("objetivo")
    return faltan


def montar(n: int, c: dict) -> dict:
    """Calendar + corpus → el dict frontmatter de datos.md."""
    hab, fon, m = C.habilidad(n), C.fonema(n), C.mock(n)
    return {
        "dia": n,
        "semana": C.semana(n),
        "habilidad": hab,
        "drill": "drill-semanal" if C.dia_de_drill(n) else None,
        "mock": (m["semana"] if m else None),
        "base_fija": {
            "anki_nuevas": 6,
            "fonema": {
                "bloque": fon["bloque"],
                "contraste": fon["contraste"],
                "etapa": fon["etapa"],
                "elsa": fon["elsa"],
            },
        },
        "ejercicio": {
            "objetivo": c["objetivo"],
            "items": [
                {
                    "tipo": it.get("tipo", hab),
                    "instruccion": it["instruccion"],
                    "stimulus": it.get("stimulus", c.get("stimulus", "")),
                    "audio": it.get("audio", {"uk": None, "us": None}),
                    "opciones": [{"letra": o["letra"], "texto": o["texto"]}
                                 if isinstance(o, dict) else
                                 {"letra": chr(65 + i), "texto": o}
                                 for i, o in enumerate(it.get("opciones") or [])],
                    "correcta": it.get("correcta"),
                    "por_que": it["por_que"],
                }
                for it in c["items"]
            ],
        },
        "coloquial": c["coloquial"],
        "vocabulario": c["vocabulario"],
        **({"writing": c["writing"]} if hab == "writing" and c.get("writing") else {}),
    }


def volcar(n: int, fm: dict, cuerpo: str) -> str:
    head = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=100)
    return f"---\n{head}---\n\n{cuerpo.strip()}\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", action="store_true",
                    help="solo listar qué días faltan, sin escribir nada")
    args = ap.parse_args()

    raiz = Path(__file__).resolve().parent.parent
    corpus = cargar_corpus(raiz)
    completos, faltan = [], {}

    for n in range(1, 91):
        c = corpus.get(n)
        errs = validar_dia(n, c or {})
        if errs:
            faltan[n] = errs
        else:
            completos.append(n)

    if args.reporte:
        print(f"corpus: {len(corpus)} días con contenido · "
              f"{len(completos)} completos · {len(faltan)} incompletos\n")
        for n, e in faltan.items():
            print(f"  día {n:>2}: {', '.join(e)}")
        if not faltan:
            print("  ninguno")
        return 0

    escritos = 0
    for n in completos:
        c = corpus[n]
        carpeta = raiz / "ejercicios" / f"dia-{n:03d}"
        carpeta.mkdir(parents=True, exist_ok=True)
        (carpeta / "datos.md").write_text(
            volcar(n, montar(n, c), c["cuerpo"]), encoding="utf-8")
        escritos += 1

    print(f"✓ {escritos} datos.md escritos")
    if faltan:
        print(f"  ⚠ {len(faltan)} días sin contenido suficiente, NO escritos: "
              f"{', '.join(str(n) for n in sorted(faltan))}")
        print("  corré --reporte para ver el detalle")
    return 0


if __name__ == "__main__":
    sys.exit(main())
