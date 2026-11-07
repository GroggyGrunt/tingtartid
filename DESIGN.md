# tingtartid.no: offentlig forside

Plan først, ett spørsmål om gangen, bygges i milepæler når gromle sier «kjør på».

## Visjon (gromle, 2026-11-07)
En veldig fancy, men litt frustrerende side på `tingtartid.no`. Den ser ut som en nettbutikk for **Allemanns** (Eurorack-modulene i `~/Projects/allemanns`), men ingenting kan kjøpes, og det kommer ikke tydelig fram hva produktene er. Ett helhetlig uttrykk bygget på Allemanns.

## Avgjort
- Tema: bare Allemanns (nobb holdes utenfor).
- **Ingen kasse og ingen lureri.** Ingen handlekurv, ingen betaling, ingen skjema. Knapper som ser ut som «Kjøp» lenker bare videre: til neste modul, tilbake til forsiden eller lignende. Frustrasjonen er at det aldri går an å kjøpe noe, ikke at noen blir lurt.
- **To språk:** engelsk og norsk med språkvalg.
- **Avsløres:** modulnavn, høytsvevende fjas om funksjon og bruk, og ekte tekniske data (HP, strømforbruk, innganger og utganger). Hva modulene faktisk er og gjør, sies ikke rett ut.
- Uttrykket hentes fra Allemanns-panelene: sort, gull, hvitt, bart FR4; høydekurver som henger sammen over kantene; varden som logo; trace-fonten; gull = ut, hvitt = inn; modulnavn er terrengord med kotehøyde.
- **Moduler: alt som har panel** (rundt 15): serien i SERIES.md (takt/fyr, roer, hoere, finger, kovolutt, tone, maske, modulator, nivaa, stoey), bre, og de rare (varde, sti, bekk, kart).
- Bilder: panel-SVG-ene i `allemanns/vcv/res/` (17 stk) og `allemanns-rack.png`, pluss nye bilder av alle tre slag: produktfoto (panelene rendret som ekte moduler, gull som glinser), stemningsbilder (fjell, skog, varder, modul på stein; ComfyUI i `grafisk/`) og kart/terreng (høydekurver i Allemanns-stil fra panelenes høydefelt).
- Bildene kopieres inn i repoet av et lite skript (`hent.sh`) fra `../allemanns`, så siden ikke er avhengig av det private repoet.
- **Hosting: GitHub Pages** fra et offentlig repo `GroggyGrunt/tingtartid` (bare siden: HTML, CSS, bilder). Statisk, ikke på Pi-en. DNS i Cloudflare pekes dit når siden er klar (spør før).
- Det er greit at Allemanns-bildene ligger offentlig selv om allemanns-repoet er privat: bare bilder, ingen lovnader.

## Milepæler
1. ✅ (2026-11-07) **Skjelett og uttrykk:** forside, én side per modul, språkvalg (NO/EN), panel-SVG-ene som produktbilder, «Kjøp»-knapper som lenker videre, høydekurver som bakgrunn. Ren HTML og CSS, litt JS for språkvalget. Ses lokalt.
2. ✅ (2026-11-07) **Tekst:** fjas og tekniske data for alle modulene, på begge språk.  Tellinger fra panelgeneratorene i allemanns; strømtrekk er ikke målt og står som «ikke målt». Høydekurver i bakgrunnen flyttet til milepæl 3.
3. ✅ (2026-11-07) **Bilder:** høydekurver bak racket som møter panelkantene og bak produktsidene (`terreng.py`); produktfoto som 3D-vipping med gullglans i nettleseren (`vipp.js`) i stedet for rendrede bilder; tre stemningsbilder fra ComfyUI (varde, skog, os; `stemning.sh`). Et bilde av en «modul på stein» ble forkastet: modellen lager en annen, rar maskin med falsk logo.
4. ✅ (2026-11-07) **Ut på nett:** repo `GroggyGrunt/tingtartid` (offentlig), GitHub Pages, DNS i Cloudflare for `tingtartid.no` og `www` (spør før), HTTPS. Pages bygger fra `main:/docs`, så `git push` publiserer. DNS: apex A 185.199.108–111.153 og AAAA 2606:50c0:8000–8003::153, `www` CNAME `groggygrunt.github.io`, alle uten proxy.

## Åpne spørsmål
Ingen før milepæl 1.
