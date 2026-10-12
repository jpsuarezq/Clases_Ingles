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
oficial y pone "n/a" si el nivel cae en A1/A2.
_Avoid_: score, puntaje IELTS, nivel

**Acento de producción**:
El acento que se practica al producir habla: americano. No es el único que se escucha — el
listening exige variedad británica, australiana y neozelandesa además del americano.
_Avoid_: acento, pronunciación americana
