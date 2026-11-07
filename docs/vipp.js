// Produktsiden: panelet vipper etter pekeren, og glansen følger lyset. Av når brukeren vil ha lite bevegelse.
(function () {
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  document.addEventListener("DOMContentLoaded", function () {
    var fig = document.querySelector(".bilde"), v = fig && fig.querySelector(".vipp");
    if (!v) return;
    function sett(px, py) {             // px, py: -1 .. 1 fra midten
      v.style.transform = "rotateY(" + (px * 14) + "deg) rotateX(" + (-py * 10) + "deg)";
      v.style.setProperty("--gx", (50 + px * 60) + "%");
      v.style.setProperty("--gy", (50 + py * 60) + "%");
    }
    document.addEventListener("pointermove", function (e) {
      var r = v.getBoundingClientRect();
      var px = (e.clientX - r.left - r.width / 2) / (innerWidth / 2);
      var py = (e.clientY - r.top - r.height / 2) / (innerHeight / 2);
      sett(Math.max(-1, Math.min(1, px)), Math.max(-1, Math.min(1, py)));
    });
    document.addEventListener("pointerleave", function () { sett(0, 0); });
    sett(-0.35, -0.25);                 // litt på skrå fra start, som et produktfoto
  });
})();
