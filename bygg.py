#!/usr/bin/env python3
"""Bygger tingtartid.no til docs/ (GitHub Pages). Kjør ./hent.sh først når panelene er endret.

Hver tekst er (norsk, engelsk). Begge ligger i HTML-en, språkvalget skjuler den ene (sprak.js).
"""
import html, json
from pathlib import Path

ROT = Path(__file__).parent
UT = ROT / "docs"
_F = json.loads((ROT / "glyphs.json").read_text())
GLYPHS, GLYPH_W = _F["GLYPHS"], _F["GLYPH_W"]

# navn, HP, høyde (U), kotehøyde, fjell, type, fjas (no, en). Rekkefølgen er butikkens (signalveien).
MODULER = [
    ("fyr", 8, 3, 1392, "Stetind", "digital", ("Pulsen alt annet følger.", "The pulse everything else follows.")),
    ("kilde", 8, 3, 2469, "Galdhøpiggen", "digital", ("Der det begynner.", "Where it begins.")),
    ("bre", 8, 3, 1957, "Høgste Breakulen", "digital", ("Én kilde, mange bekker, samtidig.", "One source, many streams, at once.")),
    ("juv", 8, 3, 604, "Preikestolen", "analog", ("Strømmen smalner.", "The stream narrows.")),
    ("dam", 8, 3, 2178, "Rondeslottet", "analog", ("Slipper gjennom så mye du vil.", "Lets through as much as you like.")),
    ("skred", 8, 3, 1550, "Romsdalshorn", "analog", ("Stiger og faller.", "Rises and falls.")),
    ("flo", 8, 3, 448, "Reinebringen", "analog", ("Tidevann. Og fjære.", "Tide. And ebb.")),
    ("delta", 8, 3, 1743, "Besseggen", "analog", ("Én strøm deler seg i mange.", "One stream becomes many.")),
    ("elv", 8, 3, 182, "Vøringsfossen", "analog", ("Bekkene samles.", "The streams gather.")),
    ("os", 4, 3, 0, "havet", "analog", ("Der alt renner ut.", "Where it all runs out.")),
    ("myr", 4, 3, 1690, "Hårteigen", "analog", ("Støy og tilfeldigheter.", "Noise and chance.")),
    ("sti", 8, 3, 2286, "Snøhetta", "digital", ("Turen du gikk, spilt av igjen.", "The trip you took, played back.")),
    ("varde", 8, 3, 2405, "Store Skagastølstind", "digital", ("Viser vei. Steg for steg.", "Shows the way. Step by step.")),
    ("kart", 8, 3, 1883, "Gaustatoppen", "blank", ("En sjettedel av Norge i sikte.", "A sixth of Norway in view.")),
    ("bekk", 20, 1, None, None, "analog", ("Små bekker gjør stor elv.", "Small brooks make a big river.")),
]

T = {  # faste tekster
    "butikk": ("Butikken", "The shop"),
    "kjop": ("Kjøp", "Buy"),
    "tilbake": ("Tilbake til butikken", "Back to the shop"),
    "moh": ("moh.", "m a.s.l."),
    "spek": ("Tekniske data", "Specifications"),
    "bredde": ("Bredde", "Width"),
    "hoyde": ("Høyde", "Height"),
    "type": ("Type", "Type"),
    "kote": ("Kotehøyde", "Spot height"),
    "strom": ("Strøm", "Power"),
    "lager": ("På lager", "In stock"),
    "lager_v": ("Nei", "No"),
    "ingress": ("Moduler for den som går sin egen vei. Gull ut, hvitt inn.",
                "Modules for those who walk their own path. Gold out, white in."),
    "analog": ("analog", "analogue"), "digital": ("digital", "digital"), "blank": ("blank", "blank"),
    "fot": ("Allemannsretten gjelder. Ingenting her er til salgs.", "The right to roam applies. Nothing here is for sale."),
}


def t(par, tag="span"):
    """Begge språk i ett element."""
    no, en = (html.escape(s) for s in par)
    return f'<{tag} class="no">{no}</{tag}><{tag} class="en" lang="en">{en}</{tag}>'


def trace(tekst, klasse="trace"):
    """Tekst i trace-fonten (4 x 6-rutenett, streker) som inline SVG. Avstand som rot_panel.trace_strokes."""
    streker, x = [], 0
    for tegn in tekst.upper():
        for linje in GLYPHS[tegn]:
            streker.append(" ".join(f"{x + a},{b}" for a, b in linje))
        x += GLYPH_W.get(tegn, 4) + 1.5
    b = max(x - 1.5, 1)
    poly = "".join(f'<polyline points="{p}"/>' for p in streker)
    return (f'<svg class="{klasse}" viewBox="-1 -1 {b + 2} 8" role="img" aria-label="{html.escape(tekst)}">'
            f'<g fill="none" stroke="currentColor" stroke-linejoin="round" stroke-linecap="round">{poly}</g></svg>')


def side(tittel, innhold, beskrivelse):
    return f"""<!doctype html>
<html lang="no">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(tittel)}</title>
<meta name="description" content="{html.escape(beskrivelse)}">
<link rel="icon" href="varde.svg">
<link rel="stylesheet" href="stil.css">
<script src="sprak.js"></script>
</head>
<body>
<header class="topp">
  <a class="merke" href="./">{trace("Allemanns")}</a>
  <button class="sprak" type="button" aria-label="Språk / language"><span class="no">EN</span><span class="en">NO</span></button>
</header>
{innhold}
<footer class="fot">{t(T["fot"], "p")}<p class="kurver">tingtartid.no</p></footer>
</body>
</html>
"""


def kote(m):
    return "—" if m[3] is None else f'{m[3]} {t(T["moh"])}'


def forside():
    rack = "".join(
        f'<a class="modul u{m[2]}" href="{m[0]}.html" style="--hp:{m[1]}">'
        f'<img src="bilder/{m[0]}.svg" alt="{m[0]}"></a>'
        for m in MODULER)
    innhold = f"""<main>
<section class="helt">
  <h1>{trace("Allemanns", "trace stor")}</h1>
  {t(T["ingress"], "p")}
</section>
<section class="rack" aria-label="Moduler">{rack}</section>
</main>"""
    return side("Allemanns", innhold, "Allemanns. Gull ut, hvitt inn.")


def produkt(i):
    m, neste = MODULER[i], MODULER[(i + 1) % len(MODULER)]
    navn, hp, u, _, fjell, typ, fjas = m
    rader = [
        (T["bredde"], f"{hp} HP" if u == 3 else f"{hp} HP 1U"),
        (T["hoyde"], f"{u}U"),
        (T["type"], t(T[typ])),
        (T["kote"], kote(m) + (f" · {html.escape(fjell)}" if fjell else "")),
        (T["strom"], "±12 V"),
        (T["lager"], t(T["lager_v"])),
    ]
    spek = "".join(f"<tr><th>{t(k)}</th><td>{v}</td></tr>" for k, v in rader)
    innhold = f"""<main class="produkt u{u}">
<figure class="bilde"><img src="bilder/{navn}.svg" alt="{navn}"></figure>
<section class="info">
  <h1>{trace(navn, "trace stor")}</h1>
  <p class="pris">{kote(m)}</p>
  {t(fjas, "p")}
  <a class="kjop" href="{neste[0]}.html">{t(T["kjop"])}</a>
  <h2>{t(T["spek"])}</h2>
  <table class="spek">{spek}</table>
  <a class="tilbake" href="./">{t(T["tilbake"])}</a>
</section>
</main>"""
    return side(f"{navn} · Allemanns", innhold, fjas[1])


def varde_ikon():
    """Favicon: en liten varde i gull."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><g fill="#d2a54a">'
            '<ellipse cx="8" cy="3" rx="2" ry="1.4"/><ellipse cx="7.5" cy="6.3" rx="3.4" ry="1.7"/>'
            '<ellipse cx="8.3" cy="9.8" rx="4.6" ry="1.9"/><ellipse cx="8" cy="13.4" rx="6" ry="2"/></g></svg>')


def main():
    (UT / "index.html").write_text(forside())
    for i in range(len(MODULER)):
        (UT / f"{MODULER[i][0]}.html").write_text(produkt(i))
    (UT / "varde.svg").write_text(varde_ikon())
    (UT / "CNAME").write_text("tingtartid.no\n")
    print(f"bygget {len(MODULER) + 1} sider i {UT}")


if __name__ == "__main__":
    main()
