#!/usr/bin/env python3
"""Bygger tingtartid.no til docs/ (GitHub Pages). Kjør ./hent.sh først når panelene er endret.

Hver tekst er (norsk, engelsk). Begge ligger i HTML-en, språkvalget skjuler den ene (sprak.js).
Tellingene av kontakter og kontroller er hentet fra panelgeneratorene i allemanns (2026-11-07).
"""
import html, json
from pathlib import Path

ROT = Path(__file__).parent
UT = ROT / "docs"
_F = json.loads((ROT / "glyphs.json").read_text())
GLYPHS, GLYPH_W = _F["GLYPHS"], _F["GLYPH_W"]


def mod(navn, hp, kote, fjell, typ, linje, fjas, u=3, skjerm=False, **deler):
    return dict(navn=navn, hp=hp, u=u, kote=kote, fjell=fjell, typ=typ, linje=linje, fjas=fjas, skjerm=skjerm,
                deler=deler)


# Rekkefølgen er butikkens (omtrent signalveien). Fjaset skal antyde, aldri si rett ut hva modulen er.
MODULER = [
    mod("fyr", 8, 1392, "Stetind", "digital",
        ("Pulsen alt annet følger.", "The pulse everything else follows."),
        ("Et fyr blinker ikke for sin egen skyld. Fyr holder takten for alt som ferdes i mørket, og sender den videre "
         "gjennom ni utløp. På skjermen regner det, baller spretter, og av og til spiller en liten robot trommer. "
         "Ingen vet helt hvorfor.",
         "A lighthouse does not blink for its own sake. Fyr keeps time for everything that travels in the dark and "
         "sends it on through nine outlets. On its screen it rains, balls bounce, and now and then a small robot "
         "plays the drums. Nobody quite knows why."),
        skjerm=True, inn=3, ut=9, enkoder=2, knapp=1, lys=12),
    mod("kilde", 8, 2469, "Galdhøpiggen", "digital",
        ("Der det begynner.", "Where it begins."),
        ("Alt som renner, startet en gang som en kilde. Denne er intet unntak. Den store knotten løfter og senker "
         "vannet en hel etasje av gangen, og den vet nøyaktig hvor den skal, én volt om gangen. Fem utløp, fem "
         "temperamenter.",
         "Everything that flows once started as a spring. This one is no exception. The big knob raises and lowers "
         "the water a whole storey at a time, and it knows exactly where it is going, one volt at a time. Five "
         "outlets, five temperaments."),
        inn=4, ut=5, knott=5, bryter=1),
    mod("bre", 8, 1957, "Høgste Breakulen", "digital",
        ("Én kilde, mange bekker, samtidig.", "One source, many streams, at once."),
        ("En bre er tålmodig. Den samler snø i hundre år og slipper den løs i fire bekker på en gang, bekker som "
         "alltid stemmer med hverandre. Gi den et lite dytt, så rasler de av gårde én og én.",
         "A glacier is patient. It gathers snow for a hundred years and lets it go as four streams at once, streams "
         "that always agree with each other. Give it a little push and they tumble off one by one."),
        skjerm=True, inn=6, ut=3, enkoder=2, knapp=1),
    mod("juv", 8, 604, "Preikestolen", "analog",
        ("Strømmen smalner.", "The stream narrows."),
        ("Mellom to bratte vegger må alt passere. Det som er for lyst, slipper ikke gjennom. Det som er for mørkt, "
         "heller ikke, om du vil. Skru opp, og veggene begynner å synge.",
         "Between two steep walls, everything must pass. What is too bright does not get through. Neither does what "
         "is too dark, if you like. Turn it up and the walls begin to sing."),
        inn=5, ut=3, knott=4, lys=1),
    mod("dam", 8, 2178, "Rondeslottet", "analog",
        ("Slipper gjennom så mye du vil.", "Lets through as much as you like."),
        ("Demningen bestemmer. Tre luker, og et vann som bare renner når noen gir lov. Den kan stå litt på gløtt "
         "for dem som ikke orker å bestemme seg, og det som ikke slipper ut ett sted, renner over i neste.",
         "The dam decides. Three gates, and water that only flows when someone says so. It can be left ajar for "
         "those who cannot make up their minds, and whatever does not get out in one place spills into the next."),
        inn=6, ut=3, knott=3, bryter=3, lys=3),
    mod("skred", 8, 1550, "Romsdalshorn", "analog",
        ("Stiger og faller.", "Rises and falls."),
        ("Først ingenting. Så alt på en gang. Så sakte, sakte tilbake. Skred har to løp: ett som venter så lenge du "
         "holder, og ett som går av seg selv, igjen og igjen, hvis du lar det.",
         "First nothing. Then everything at once. Then slowly, slowly back. Skred has two runs: one that waits as "
         "long as you hold on, and one that goes off by itself, again and again, if you let it."),
        inn=3, ut=2, knott=6, bryter=2, lys=2),
    mod("flo", 8, 448, "Reinebringen", "analog",
        ("Tidevann. Og fjære.", "Tide. And ebb."),
        ("Tre tidevann som aldri er helt enige. Det ene går så sakte at du må komme tilbake i morgen for å se at "
         "det har flyttet seg. Det andre så fort at det nesten blir en tone. Det tredje følger etter.",
         "Three tides that never quite agree. One moves so slowly you have to come back tomorrow to see that it "
         "has moved. Another so fast it almost becomes a tone. The third follows."),
        inn=3, ut=6, knott=3, bryter=3, lys=3),
    mod("delta", 8, 1743, "Besseggen", "analog",
        ("Én strøm deler seg i mange.", "One stream becomes many."),
        ("Ett inn, tre ut. Og tre til. Og tre til. Atten munninger fra én elv, og alle har akkurat det samme å si. "
         "Lysene viser hvilken vei det renner.",
         "One in, three out. And three more. And three more. Eighteen mouths from one river, and all of them have "
         "exactly the same thing to say. The lights show which way it flows."),
        inn=6, ut=18, lys=6),
    mod("elv", 8, 182, "Vøringsfossen", "analog",
        ("Bekkene samles.", "The streams gather."),
        ("Tre bekker kommer inn og blir én elv, men hvilken bredd de havner på, er opp til deg. Den nederste raden "
         "renner baklengs. Det er med vilje.",
         "Three streams come in and become one river, but which bank they end up on is up to you. The bottom row "
         "flows backwards. That is on purpose."),
        inn=3, ut=9, knott=6, lys=3),
    mod("os", 4, 0, "havet", "analog",
        ("Der alt renner ut.", "Where it all runs out."),
        ("Her slutter kartet. Alt du har bygget, renner ut i havet, eller rett inn i ørene dine. Det lille lyset "
         "sier fra når det blir for mye.",
         "This is where the map ends. Everything you have built runs out into the sea, or straight into your ears. "
         "The little light tells you when it gets too much."),
        inn=2, ut=3, knott=1, lys=1),
    mod("myr", 4, 1690, "Hårteigen", "analog",
        ("Støy og tilfeldigheter.", "Noise and chance."),
        ("Myra husker ingenting og sier hva som helst. Hvitt, rosa, og en tredje vei som holder fast på det "
         "tilfeldige akkurat lenge nok til at du rekker å høre det.",
         "The bog remembers nothing and says anything. White, pink, and a third way that holds on to chance just "
         "long enough for you to hear it."),
        inn=2, ut=3, lys=1),
    mod("sti", 8, 2286, "Snøhetta", "digital",
        ("Turen du gikk, spilt av igjen.", "The trip you took, played back."),
        ("Turen du syklet i fjor, en gang til. Hver bakke blir en tone, hvert hopp et dunk, og pulsen din blir en "
         "spenning. Står du stille, blir det stille. Ta med egen tur.",
         "The ride you did last year, once more. Every hill becomes a note, every jump a thud, and your pulse "
         "becomes a voltage. Stand still and it goes quiet. Bring your own ride."),
        skjerm=True, inn=3, ut=6, enkoder=2, knapp=1),
    mod("varde", 8, 2405, "Store Skagastølstind", "digital",
        ("Viser vei. Steg for steg.", "Shows the way. Step by step."),
        ("Fire vandrere, seksten varder hver. De går fram, tilbake, fram og tilbake, eller bare et eller annet sted. "
         "Noen ganger flytter noen på en stein mens du ikke ser.",
         "Four walkers, sixteen cairns each. They go forward, back, back and forth, or just somewhere. Sometimes "
         "someone moves a stone while you are not looking."),
        skjerm=True, inn=3, ut=6, enkoder=2, knapp=1),
    mod("kart", 8, 1883, "Gaustatoppen", "blank",
        ("En sjettedel av Norge i sikte.", "A sixth of Norway in view."),
        ("Et kart over de andre kartene. Det forklarer alt og gjør ingenting. Fra toppen ser du en sjettedel av "
         "landet, men ikke hvordan du kommer deg ned.",
         "A map of the other maps. It explains everything and does nothing. From the top you can see a sixth of the "
         "country, but not how to get down."),
        ),
    mod("bekk", 20, None, None, "analog",
        ("Små bekker gjør stor elv.", "Small brooks make a big river."),
        ("Tre bekker som bor i en stripe under alt det andre, med plass til flere. Den eneste her som ligger ned. "
         "Hvor de renner, står ikke på kartet.",
         "Three brooks living in a strip beneath everything else, with room for more. The only one here lying down. "
         "Where they flow is not on the map."),
        u=1, inn=3, knott=9),
]

T = {  # faste tekster
    "kjop": ("Kjøp", "Buy"),
    "tilbake": ("Tilbake til butikken", "Back to the shop"),
    "moh": ("moh.", "m a.s.l."),
    "spek": ("Tekniske data", "Specifications"),
    "bredde": ("Bredde", "Width"),
    "type": ("Type", "Type"),
    "inn": ("Innganger", "Inputs"),
    "ut": ("Utganger", "Outputs"),
    "kontroller": ("Kontroller", "Controls"),
    "lys": ("Lys", "Lights"),
    "skjerm": ("Skjerm", "Screen"),
    "skjerm_v": ("1,69″ IPS, 240 × 280", "1.69″ IPS, 240 × 280"),
    "kote": ("Kotehøyde", "Spot height"),
    "strom": ("Strøm", "Power"),
    "strom_v": ("±12 V, 10-pins. Trekk ikke målt", "±12 V, 10-pin. Draw not measured"),
    "lager": ("På lager", "In stock"),
    "lager_v": ("Nei", "No"),
    "ingen": ("ingen", "none"),
    "ingress": ("Moduler for den som går sin egen vei. Gull ut, hvitt inn.",
                "Modules for those who walk their own path. Gold out, white in."),
    "om": ("Hvert panel er en bit av det samme kartet. Høydekurvene møtes over kantene, uansett hvilken rekkefølge du "
           "setter dem i. Hver modul er oppkalt etter noe i terrenget og merket med høyden til et fjell. Resten finner "
           "du ut av på turen.",
           "Every panel is a piece of the same map. The contour lines meet across the edges, whatever order you put "
           "them in. Every module is named after something in the terrain and marked with the height of a mountain. "
           "The rest you will find out on the way."),
    "analog": ("analog", "analogue"), "digital": ("digital", "digital"), "blank": ("blank", "blank"),
    "fot": ("Allemannsretten gjelder. Ingenting her er til salgs.", "The right to roam applies. Nothing here is for sale."),
}
DELER = {"knott": ("knott", "knotter", "knob", "knobs"), "enkoder": ("enkoder", "enkodere", "encoder", "encoders"),
         "bryter": ("bryter", "brytere", "switch", "switches"), "knapp": ("knapp", "knapper", "button", "buttons")}


def t(par, tag="span"):
    """Begge språk i ett element."""
    no, en = (html.escape(s) for s in par)
    navn, *ekstra = tag.split(" ", 1)
    k = f" {ekstra[0].split('=')[1].strip(chr(34))}" if ekstra else ""
    return f'<{navn} class="no{k}">{no}</{navn}><{navn} class="en{k}" lang="en">{en}</{navn}>'


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
    return "—" if m["kote"] is None else f'{m["kote"]} {t(T["moh"])}'


def antall(n):
    return str(n) if n else t(T["ingen"])


def kontroller(d):
    """«5 knotter, 1 bryter» på begge språk."""
    no, en = [], []
    for k, (en1, fl, en_en, fl_en) in DELER.items():
        if d.get(k):
            n = d[k]
            no.append(f"{n} {en1 if n == 1 else fl}")
            en.append(f"{n} {en_en if n == 1 else fl_en}")
    return t((", ".join(no), ", ".join(en))) if no else t(T["ingen"])


def forside():
    rack = "".join(
        f'<a class="modul u{m["u"]}" href="{m["navn"]}.html" style="--hp:{m["hp"]}">'
        f'<img src="bilder/{m["navn"]}.svg" alt="{m["navn"]}"></a>'
        for m in MODULER)
    innhold = f"""<main>
<section class="helt">
  <h1>{trace("Allemanns", "trace stor")}</h1>
  {t(T["ingress"], "p")}
</section>
<section class="rack" aria-label="Moduler">{rack}</section>
<section class="om">{t(T["om"], "p")}</section>
</main>"""
    return side("Allemanns", innhold, T["ingress"][1])


def produkt(i):
    m, neste = MODULER[i], MODULER[(i + 1) % len(MODULER)]
    d = m["deler"]
    rader = [
        (T["bredde"], f'{m["hp"]} HP · {m["u"]}U' + (" (Intellijel)" if m["u"] == 1 else "")),
        (T["type"], t(T[m["typ"]])),
        (T["inn"], antall(d.get("inn"))),
        (T["ut"], antall(d.get("ut"))),
        (T["kontroller"], kontroller(d)),
        (T["lys"], antall(d.get("lys"))),
        (T["skjerm"], t(T["skjerm_v"]) if m["skjerm"] else t(T["ingen"])),
        (T["kote"], kote(m) + (f' · {html.escape(m["fjell"])}' if m["fjell"] else "")),
        (T["strom"], t(T["strom_v"]) if m["typ"] != "blank" else t(T["ingen"])),
        (T["lager"], t(T["lager_v"])),
    ]
    spek = "".join(f"<tr><th>{t(k)}</th><td>{v}</td></tr>" for k, v in rader)
    innhold = f"""<main class="produkt u{m["u"]}">
<figure class="bilde"><img src="bilder/{m["navn"]}.svg" alt="{m["navn"]}"></figure>
<section class="info">
  <h1>{trace(m["navn"], "trace stor")}</h1>
  {f'<p class="pris">{kote(m)}</p>' if m["kote"] is not None else ""}
  {t(m["linje"], "p class=\"linje\"")}
  {t(m["fjas"], "p")}
  <a class="kjop" href="{neste["navn"]}.html">{t(T["kjop"])}</a>
  <h2>{t(T["spek"])}</h2>
  <table class="spek">{spek}</table>
  <a class="tilbake" href="./">{t(T["tilbake"])}</a>
</section>
</main>"""
    return side(f'{m["navn"]} · Allemanns', innhold, m["linje"][1])


def varde_ikon():
    """Favicon: en liten varde i gull."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><g fill="#d2a54a">'
            '<ellipse cx="8" cy="3" rx="2" ry="1.4"/><ellipse cx="7.5" cy="6.3" rx="3.4" ry="1.7"/>'
            '<ellipse cx="8.3" cy="9.8" rx="4.6" ry="1.9"/><ellipse cx="8" cy="13.4" rx="6" ry="2"/></g></svg>')


def main():
    (UT / "index.html").write_text(forside())
    for i, m in enumerate(MODULER):
        (UT / f'{m["navn"]}.html').write_text(produkt(i))
    (UT / "varde.svg").write_text(varde_ikon())
    (UT / "CNAME").write_text("tingtartid.no\n")
    print(f"bygget {len(MODULER) + 1} sider i {UT}")


if __name__ == "__main__":
    main()
