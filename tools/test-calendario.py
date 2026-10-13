#!/usr/bin/env python3
"""Verifica el calendario contra lo que #9 y #13 decidieron.

Si alguno de estos falla, el generador va a producir 90 días equivocados.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calendario as C

fallas = []


def check(nombre, cond, extra=""):
    if cond:
        print(f"  ✓ {nombre}")
    else:
        fallas.append(nombre)
        print(f"  ✗ {nombre}" + (f"  → {extra}" if extra else ""))


print("\n── rotación (#13: L → W → S → R, cíclica, a partes iguales) ──")
esperada = ["listening", "writing", "speaking", "reading"]
check("los primeros 4 días son L, W, S, R",
      [C.habilidad(d) for d in range(1, 5)] == esperada,
      str([C.habilidad(d) for d in range(1, 5)]))
check("cicla 22 veces sin desviarse",
      all(C.habilidad(d) == esperada[(d - 1) % 4] for d in range(1, 91) if C.mock(d) is None))
conteo = {h: sum(1 for d in range(1, 91) if C.habilidad(d) == h) for h in esperada}
base = [C.ROTACION[(d - 1) % 4] for d in range(1, 91)]
cb = {h: base.count(h) for h in esperada}
check("la rotación pura, sin mocks, es pareja", max(cb.values()) - min(cb.values()) <= 1, str(cb))
dias_mock = [d for d in range(1, 91) if C.mock(d)]
desvian = [d for d in range(1, 91) if C.habilidad(d) and C.habilidad(d) != base[d - 1]]
check("las únicas habilidades que se desvían son días de mock",
      all(d in dias_mock for d in desvian), str(desvian))
check("el día del EF SET no tiene habilidad: es las cuatro a la vez", C.habilidad(90) is None)
check("reparto resultante", True, str(conteo))

print("\n── fonemas (#9: tres fases, cinco tramos de 6 días) ──")
check("15 tramos × 6 días = 90", len([t for _, ts in C.FASES for t in ts]) * 6 == 90)
check("cada fase tiene 5 tramos", all(len(ts) == 5 for _, ts in C.FASES))

# el orden exacto de #9
orden = [t[0] for _, ts in C.FASES for t in ts]
check("el contraste del día 1 es acento-lexico", C.fonema(1)["contraste"] == "acento-lexico")
check("schwa empieza el día 7", C.fonema(7)["contraste"] == "schwa")
check("function-words empieza el día 13", C.fonema(13)["contraste"] == "function-words")
check("ritmo/chunking/linking empieza el día 19", C.fonema(19)["contraste"] == "ritmo-chunking-linking")
check("el bloque 2 empieza el día 31", C.fonema(31)["bloque"] == 2)
check("/ɪ/-/iː/ empieza el día 31", C.fonema(31)["contraste"] == "i-versus-i-larga")
check("el bloque 3 empieza el día 61", C.fonema(61)["bloque"] == 3)
check("/θ/ empieza el día 61 — TARDE a propósito", C.fonema(61)["contraste"] == "th")
check("/j/-/dʒ/ arranca el día 79 — al final, es el menos evidenciado", C.fonema(79)["contraste"] == "j-versus-dzh")
check("el día 90 cierra en integracion", C.fonema(90)["contraste"] == "integracion")
check("ningún contraste se repite fuera de su tramo de 6",
      all(C.fonema(d)["contraste"] == C.fonema(d - 1)["contraste"] for d in range(2, 91)
          if (d - 1) % 6 != 0))

print("\n── el orden interno de cada bloque (#9: articulatoria → percepción → producción) ──")
check("día 1 del bloque es explicación", all(C.fonema(d)["etapa"] == "explicacion" for d in range(1, 91, 6)))
check("días 2–3 son percepción", all(C.fonema(d)["etapa"] == "percepcion" for d in range(2, 91, 6))
      and all(C.fonema(d)["etapa"] == "percepcion" for d in range(3, 91, 6)))
check("días 4–5 son producción", all(C.fonema(d)["etapa"] == "produccion" for d in range(4, 91, 6))
      and all(C.fonema(d)["etapa"] == "produccion" for d in range(5, 91, 6)))
check("día 6 del bloque es consolidación", all(C.fonema(d)["etapa"] == "consolidacion" for d in range(6, 91, 6)))

print("\n── ELSA (#9: percepción con feedback, 2 de 6 días, NO los 6) ──")
elsa_por_bloque = [sum(1 for o in range(6) if C.fonema(i * 6 + o + 1)["elsa"]) for i in range(15)]
check("ELSA va exactamente 2 días en cada bloque de 6", all(e == 2 for e in elsa_por_bloque), str(elsa_por_bloque))
check("ELSA cae SOLO en los días de percepción",
      all(C.fonema(d)["elsa"] == (C.fonema(d)["etapa"] == "percepcion") for d in range(1, 91)))
check("ELSA va 30 de 90 días", sum(1 for d in range(1, 91) if C.fonema(d)["elsa"]) == 30)

print("\n── mocks (#13: semanas 4 y 10 L+R en dos días; semana 13 EF SET) ──")
check("semana 4 tiene mock", C.semana(C.MOCKS[4]["dias"][0]) == 4)
check("semana 10 tiene mock", C.semana(C.MOCKS[10]["dias"][0]) == 10)
check("semana 13 tiene mock", C.semana(C.MOCKS[13]["dias"][0]) == 13)
check("los BC son L+R en dos días consecutivos",
      C.MOCKS[4]["skills"] == ["listening", "reading"] and C.MOCKS[4]["dias"][1] - C.MOCKS[4]["dias"][0] == 1)
check("el EF SET de cierre es el día 90", C.MOCKS[13]["dias"] == [90])
check("el mock toma el día: día 27 es listening", C.habilidad(27) == "listening")
check("el mock toma el día: día 28 es reading", C.habilidad(28) == "reading")
check("la rotación retoma después del mock — día 29 vuelve a listening",
      C.habilidad(29) == "listening", C.habilidad(29))
check("sin mocks fuera de las semanas 4, 10 y 13",
      all(C.semana(d) in (4, 10, 13) for d in range(1, 91) if C.mock(d)))

print("\n── consistencia con dia-001, que ya existe ──")
f1 = C.fonema(1)
check("día 1: habilidad listening", C.habilidad(1) == "listening")
check("día 1: bloque 1", f1["bloque"] == 1)
check("día 1: contraste acento-lexico", f1["contraste"] == "acento-lexico")
check("día 1: etapa explicacion", f1["etapa"] == "explicacion")
check("día 1: ELSA no va", f1["elsa"] is False)

print("\n── la vista de 90 días tiene que sobrevivir al None del día 90 ──")
import contextlib
import io

buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf):
        C.main()
    out = buf.getvalue()
    check("main() imprime los 90 días sin crashear", out.count("\n") == 92,
          f"{out.count(chr(10))} líneas")
    check("el día 90 se muestra como 'las 4'", "— las 4 —" in out)
except Exception as e:  # noqa: BLE001
    check("main() imprime los 90 días sin crashear", False, repr(e))

print(f"\n{'Todas las invariantes se cumplen' if not fallas else str(len(fallas)) + ' FALLAS'}")
for f in fallas:
    print(f"  · {f}")
sys.exit(1 if fallas else 0)
