#!/bin/sh
# Henter panelbilder og trace-fonten fra allemanns-repoet, så siden ikke er avhengig av det.
set -e
A=${ALLEMANNS:-$HOME/Projects/allemanns}
cd "$(dirname "$0")"
mkdir -p docs/bilder
for par in fyr:takt4 kilde:tone bre:bre juv:maske dam:finger skred:kovolutt flo:modulator delta:roer \
           elv:nivaa os:hoere myr:stoey sti:sti varde:varde kart:kart bekk:bekk; do
  cp "$A/vcv/res/${par#*:}.svg" "docs/bilder/${par%%:*}.svg"
done
# GLYPHS og GLYPH_W fra rot_panel.py uten å importere den (den trenger pcbnew)
python3 - "$A/tools/rot_panel.py" > glyphs.json <<'EOF'
import ast, json, sys
v = {n.targets[0].id: ast.literal_eval(n.value) for n in ast.parse(open(sys.argv[1]).read()).body
     if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") in ("GLYPHS", "GLYPH_W")}
print(json.dumps(v, ensure_ascii=False))
EOF
echo "hentet $(ls docs/bilder | wc -l) bilder og glyphs.json"
