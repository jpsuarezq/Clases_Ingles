#!/usr/bin/env python3
"""Extrae los diálogos de *Everyday Conversations* (US Dept. of State, dominio público)
y los deja en `tools/corpus/dialogos.yaml`.

El PDF es una fuente, no un artefacto: este script se puede re-correr cuando quieras.
No lo guardamos al repo, solo su texto ya extraído.

Uso:
    python3 tools/extraer-dialogos.py <ruta-al.pdf>
"""

import re
import subprocess
import sys
from pathlib import Path

import yaml


def extraer_texto(pdf: Path) -> str:
    r = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"pdftotext falló: {r.stderr.strip()[:200]}")
    return r.stdout


def partir_dialogos(texto: str) -> list[dict]:
    """Separa por cabecera `Dialogue N-M: Título` y agrupa los turnos."""
    lineas = texto.splitlines()
    # El índice del PDF escribe `1-5` y el cuerpo `1.5`. Un solo separador mal
    # entendido pierde el diálogo entero en silencio, así que se normaliza antes.
    for i, l in enumerate(lineas):
        if m := re.match(r"^(\s*Dialogue\s+\d+)\.(\d+:\s*.+?)\s*$", l):
            lineas[i] = f"{m.group(1)}-{m.group(2)}"
    cabeceras = [(i, m.group(0)) for i, l in enumerate(lineas)
                 if (m := re.match(r"\s*Dialogue (\d+-\d+):\s*(.+?)\s*$", l))]

    dialogos = []
    for k, (ini, _) in enumerate(cabeceras):
        fin = cabeceras[k + 1][0] if k + 1 < len(cabeceras) else len(lineas)
        m = re.match(r"\s*Dialogue (\d+-\d+):\s*(.+?)\s*$", cabeceras[k][1])
        num, titulo = m.group(1), m.group(2)

        # El índice del PDF también tiene estas cabeceras, pero sin turnos debajo.
        turnos, hablante_actual = [], None
        for l in lineas[ini + 1:fin]:
            s = l.strip()
            if not s or s.isdigit():
                continue
            t = re.match(r"^([A-Z][A-Z .'-]{1,40}):\s*(.*)$", s)
            if t:
                hablante_actual = t.group(1).strip()
                texto_turno = t.group(2).strip()
                if texto_turno:
                    turnos.append({"de": hablante_actual, "d": texto_turno})
            elif turnos and hablante_actual:
                # continuación de la línea anterior, el PDF corta a ~70 caracteres
                turnos[-1]["d"] += " " + s

        if len(turnos) >= 3:  # el índice tiene 0 turnos; un diálogo real tiene varios
            dialogos.append({"num": num, "titulo": titulo, "turnos": turnos})

    # el índice y el cuerpo repiten los mismos números: quedarse con el más largo
    por_num = {}
    for d in dialogos:
        if d["num"] not in por_num or len(d["turnos"]) > len(por_num[d["num"]]["turnos"]):
            por_num[d["num"]] = d
    return [por_num[k] for k in sorted(por_num, key=lambda x: (int(x.split("-")[0]), int(x.split("-")[1])))]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    pdf = Path(sys.argv[1])
    if not pdf.exists():
        raise SystemExit(f"no existe {pdf}")

    dialogos = partir_dialogos(extraer_texto(pdf))
    if not dialogos:
        raise SystemExit("no se extrajo ningún diálogo — revisá el PDF")

    salida = Path(__file__).resolve().parent / "corpus" / "dialogos.yaml"
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(
        "# GENERADO por tools/extraer-dialogos.py — Everyday Conversations,\n"
        "# US Dept. of State, dominio público (ver tools/corpus/FUENTES.md)\n"
        + yaml.safe_dump(dialogos, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8")

    turnos = sum(len(d["turnos"]) for d in dialogos)
    palabras = sum(len(t["d"].split()) for d in dialogos for t in d["turnos"])
    print(f"✓ {len(dialogos)} diálogos · {turnos} turnos · {palabras:,} palabras")
    print(f"  → {salida}")
    for d in dialogos[:5]:
        print(f"    {d['num']:>6}  {d['titulo']:<38} {len(d['turnos'])} turnos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
