// Språkvalg: norsk eller engelsk, husket i nettleseren. Uten JS vises norsk.
(function () {
  var d = document.documentElement, lagret = null;
  try { lagret = localStorage.getItem("sprak"); } catch (e) {}
  d.lang = lagret || (/^(no|nb|nn)/i.test(navigator.language || "") ? "no" : "en");
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".sprak").addEventListener("click", function () {
      d.lang = d.lang === "no" ? "en" : "no";
      try { localStorage.setItem("sprak", d.lang); } catch (e) {}
    });
  });
})();
