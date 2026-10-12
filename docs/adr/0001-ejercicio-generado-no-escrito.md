# El ejercicio del día es HTML generado, no escrito a mano

La unidad de trabajo del plan es una carpeta por día (`ejercicios/dia-001/` a `dia-090/`). Cada una
lleva un `datos.md` fuente, el `ejercicio.html` **generado** a partir de él, y un `registro.md` con
el resultado del día. El HTML es el único formato de ejercicio de los 90 días, en **formato B**
(panel de explicación permanente a la derecha), y no se edita a mano nunca.

## Considered Options

- **Escribir el HTML a mano cada día.** Rechazado: el prototipo único ya salió con 3 bugs al primer
  prueba en navegador (audio repetido entre variantes, audio ausente en una variante, selección
  invisible). Multiplicado por 90, cada bug futuro significaría arreglarlo 90 veces.
- **HTML + markdown como formatos paralelos, mismo contenido.** Rechazado por duplicación: dos
  copias del mismo ejercicio mantenidas durante 90 días es exactamente el formato que se vuelve
  insoportable en la semana 3.
- **Markdown solo, con respuestas al final.** Rechazado: no puede llevar audio, y el listening con
  variedad de acentos (británico, australiano, neozelandés además del americano) es requisito del
  objetivo IELTS.

## Consequences

- Cambiar el formato del ejercicio significa tocar **una** plantilla y regenerar los 90, no 90
  archivos. Esto es lo que hace reversible una decisión que, de otro modo, no lo sería.
- El `ejercicio.html` es un artefacto generado que **se commitea**: se necesita el archivo en disco
  para abrirlo con doble click, sin servidor ni red.
- Los 90 scaffolds se generan de una vez con los slots de contenido vacíos. El contenido real
  depende de las decisiones de #9 (secuencia fonética) y #11 (fuente del vocabulario), que están
  todavía abiertas.
- El **orden de rotación** de las cuatro habilidades no se decidió acá: depende de #13 (cadencia de
  mocks), porque un mock semanal ocupa un día que no es de skill.
- El registro del día usa un bloque YAML estricto para que el agregador pueda leerlo sin ambigüedad.
  El `band_estimado` queda con el slot vacío hasta que #12 defina la fórmula.
