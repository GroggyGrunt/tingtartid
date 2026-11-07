# tingtartid.no — instruks til Claude Code

Offentlig forside for `tingtartid.no`: en Allemanns-«butikk» der ingenting kan kjøpes. Plan og alt som er avgjort står i `DESIGN.md` (design først, ett spørsmål om gangen, milepæler på «kjør på»).

- `./hent.sh` kopierer panel-SVG-ene og trace-fonten fra `~/Projects/allemanns` (privat repo, siden skal ikke være avhengig av det).
- `python3 bygg.py` lager sidene i `docs/` (GitHub Pages). Tekster og moduler står øverst i `bygg.py`, hver tekst som (norsk, engelsk).
- Ren HTML og CSS, litt JS bare for språkvalget. Ingen rammeverk, ingen bygging utover `bygg.py`.
- Siden er offentlig: ingen skjema, ingen innsamling, ingen sporing, ingen personopplysninger, ingen lovnader om salg.
- DNS for `tingtartid.no` ligger i Cloudflare: ikke endre uten å spørre.
- Svar på norsk. Commit med den globale git-identiteten.
