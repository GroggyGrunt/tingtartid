#!/bin/sh
# Lager stemningsbildene på nytt (ComfyUI i ~/Projects/grafisk, Z-Image). Samme prompt og seed gir samme bilde.
set -e
U=$(cd "$(dirname "$0")" && pwd)/docs/bilder
cd ~/Projects/grafisk
lag() { .venv/bin/python -m verktøy.bilde "$2" "$U/stemning-$1.jpg" --modell zimage --stil ingen --bredde 1216 --hoyde 832 --seed "$3"; }
lag varde "A tall stone cairn on a bare Norwegian mountain ridge at blue hour, last golden light on distant peaks, low clouds in the valleys below, dark moody atmosphere, deep black shadows, warm gold highlights, cinematic landscape photograph, 35mm, fine detail" 1392
lag skog "Dark Norwegian pine forest at night, a small stream with mossy rocks, faint golden light reflecting on the wet stones, mist between the trees, very dark and quiet, cinematic photograph, black and gold tones" 2469
lag os "A river mouth meeting the dark sea on the Norwegian coast at dusk, smooth wet rocks, the last thin line of golden light on the horizon, calm water, very dark moody atmosphere, deep black shadows, cinematic landscape photograph, long exposure" 0
