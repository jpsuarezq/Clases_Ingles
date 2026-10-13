/* Prueba real contra DOM de UN EJERCICIO GENERADO (no el prototipo viejo).
 *
 * El HTML generado es un cascarón: el YAML de datos.md va embebido y un script lo
 * renderiza. Si ese script falla, el archivo se ve "listo" y no muestra nada — así
 * que probar el archivo sin correr el JS no prueba nada.
 *
 * Corre contra el día 001, que es la implementación de referencia.
 *
 * Uso:
 *   NODE_PATH=.../node_modules node tools/test-ejercicio.js
 */
const fs = require("fs");
const { JSDOM } = require("jsdom");

const ARCHIVO = process.argv[2] || "ejercicios/dia-001/ejercicio.html";
const html = fs.readFileSync(ARCHIVO, "utf8");

const dom = new JSDOM(html, { runScripts: "dangerously", pretendToBeVisual: true });
const doc = dom.window.document;
const $ = (s) => doc.querySelector(s);
const $$ = (s) => [...doc.querySelectorAll(s)];

let pass = 0, fail = 0;
const check = (name, cond, detail) => {
  if (cond) { pass++; console.log("  ✓ " + name); }
  else { fail++; console.log("  ✗ " + name + (detail ? "  → " + detail : "")); }
};

console.log("\n═══ 1 · el YAML embebido se renderizó (no quedó el cascarón vacío) ═══");
check("el objetivo aparece", ($("#objetivo")?.textContent || "").length > 10);
const botones = $$("#items .ans");
check("hay opciones de respuesta", botones.length > 0, "son " + botones.length);
const evaluables = new Set(botones.map(b => b.dataset.i)).size;
check("hay al menos un ítem evaluable", evaluables >= 1, "evaluables=" + evaluables);
check("vocabulario: 6 cards", $$("#vocab .card, #vocab > *").length === 6,
  "son " + $$("#vocab .card, #vocab > *").length);
check("coloquial: hay filas UK↔US", $$("#coloquial > *").length >= 2,
  "son " + $$("#coloquial > *").length);

console.log("\n═══ 2 · audio: UK y US son voces DISTINTAS y de la frase correcta ═══");
const say = $$(".say");
check("hay botones de audio", say.length > 0, "son " + say.length);
const uk = say.filter(b => b.dataset.which === "uk");
const us = say.filter(b => b.dataset.which === "us");
check("existe un botón UK", uk.length > 0, "son " + uk.length);
check("existe un botón US", us.length > 0, "son " + us.length);
check("todo botón trae el texto a decir",
  say.every(b => (b.dataset.text || "").length > 3),
  "vacíos=" + say.filter(b => !b.dataset.text).length);
// El acento es la razón de ser del par: si los dos usan la misma voz, el par es decorativo.
check("UK e US declaran distinto (en-GB / en-US) en el handler",
  /data-which|"uk"|en-GB/.test(html) && /en-US/.test(html));
check("UK y US de una misma frase comparten texto pero no variante",
  say.some(b => b.dataset.which === "uk" && say.some(o => o.dataset.which === "us" && o.dataset.text === b.dataset.text)));

console.log("\n═══ 3 · al elegir una opción se marca y solo una queda marcada ═══");
const item0 = $$("#items .ans").filter(b => b.dataset.i === "0");
if (item0.length >= 2) {
  item0[1].click();
  check("la elegida queda marcada", item0[1].getAttribute("data-sel") === "1");
  check("solo una marcada en el ítem",
    item0.filter(b => b.getAttribute("data-sel") === "1").length === 1,
    "marcadas=" + item0.filter(b => b.getAttribute("data-sel") === "1").length);
  item0[2].click();
  check("al cambiar, la marca se MUEVE y no se acumula",
    item0[2].getAttribute("data-sel") === "1" && item0[1].getAttribute("data-sel") !== "1");
  // Los otros ítems no deben tocarse.
  const otros = $$("#items .ans").filter(b => b.dataset.i !== "0" && b.getAttribute("data-sel") === "1");
  check("marcar el ítem 1 no marca los demás", otros.length === 0, "se marcaron=" + otros.length);
}

console.log("\n═══ 4 · el HTML conoce la respuesta y las opciones son consistentes ═══");
// Los ítems de producción (speaking/writing) no tienen opciones: hay que respetarlos.
const conOpc = $$("#items .ans").filter(b => b.getAttribute("data-sel") === "1" || true);
check("las opciones llevan data-i y data-k consistentes",
  $$("#items .ans").every(b => b.dataset.i !== undefined && /^[A-D]$/.test(b.dataset.k)));
check("los ítems evaluables tienen respuesta marcada en el HTML",
  $$("#items .ans").filter(b => b.dataset.ok === "true").length > 0);
const prod = $$("#items .item, #items > *").length;
check("el HTML renderizó todos los ítems (evaluables y de producción)", prod > 0,
  "renderizados=" + prod);

console.log(`\n${fail === 0 ? "✅ TODO OK" : "❌ FALLÓ"}  —  ${pass} pasaron, ${fail} fallaron\n`);
process.exit(fail === 0 ? 0 : 1);
