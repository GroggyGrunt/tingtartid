"""Høydekurver i Allemanns-stil til bakgrunnen (SVG, mm som i panelene).

Ved panelkantene er høyden bare en funksjon av y (samme som rot_panel.Panel.height), så kurvene her møter
kurvene i panelene der racket slutter. Utenfor racket tar bølger og åser over.
"""
import math, random

LEVEL = 0.1          # kotehøyde mellom kurvene, som i rot_panel
H = 128.5            # 3U


def kant(y):
    """Høyden ved alle panelkanter (rot_panel.Panel.height, base)."""
    return -0.024 * y + 0.12 * math.sin(0.11 * y)


def felt(seed, bredde, hull):
    """Høydefunksjon: kant(y) innenfor hull (racket), bølger og åser som vokser utover."""
    r = random.Random(seed)
    fase = [r.uniform(0, 2 * math.pi) for _ in range(4)]
    aaser = [(r.uniform(-bredde / 2, bredde / 2), r.uniform(0, H), r.uniform(-.9, .9), r.uniform(8, 22))
             for _ in range(int(bredde / 18))]

    def h(x, y):
        d = abs(x) - hull
        if d <= 0:
            return kant(y)
        e = min(1.0, d / 25)
        e = e * e * (3 - 2 * e)
        b = (0.35 * math.sin(x * 0.05 + y * 0.045 + fase[0]) + 0.25 * math.cos(y * 0.07 - x * 0.03 + fase[1])
             + 0.15 * math.sin(x * 0.11 + fase[2]) * math.cos(y * 0.09 + fase[3]))
        b += sum(a * math.exp(-((x - ax) ** 2 + (y - ay) ** 2) / (2 * s * s))
                 for ax, ay, a, s in aaser if abs(x - ax) < 3 * s)
        return kant(y) + e * b
    return h


def kurver(h, x0, x1, y0, y1, steg):
    """Marching squares. Gir {nivå: [linjestykker]}."""
    nx, ny = int((x1 - x0) / steg) + 1, int((y1 - y0) / steg) + 1
    xs = [x0 + i * steg for i in range(nx)]
    ys = [y0 + j * steg for j in range(ny)]
    v = [[h(x, y) for x in xs] for y in ys]
    lo, hi = math.floor(min(map(min, v)) / LEVEL), math.ceil(max(map(max, v)) / LEVEL)
    ut = {}
    for n in range(lo, hi + 1):
        lv, segs = n * LEVEL + 1e-9, []
        for j in range(ny - 1):
            for i in range(nx - 1):
                a, b, c, d = v[j][i] - lv, v[j][i + 1] - lv, v[j + 1][i + 1] - lv, v[j + 1][i] - lv
                xa, xb, ya, yb = xs[i], xs[i + 1], ys[j], ys[j + 1]
                p = []
                if (a > 0) != (b > 0): p.append((xa + steg * a / (a - b), ya))
                if (b > 0) != (c > 0): p.append((xb, ya + steg * b / (b - c)))
                if (d > 0) != (c > 0): p.append((xa + steg * d / (d - c), yb))
                if (a > 0) != (d > 0): p.append((xa, ya + steg * a / (a - d)))
                segs += [(p[q], p[q + 1]) for q in range(0, len(p) - 1, 2)]
        if segs:
            ut[n] = segs
    return ut


def kjede(segs):
    """Sett linjestykker sammen til lengre linjer (mindre fil)."""
    nk = lambda p: (round(p[0], 3), round(p[1], 3))
    ender = {}
    for s in segs:
        for p in s:
            ender.setdefault(nk(p), []).append(s)
    brukt, linjer = set(), []
    for s in segs:
        if id(s) in brukt:
            continue
        brukt.add(id(s))
        linje = [s[0], s[1]]
        for retning in (1, 0):
            while True:
                ende = linje[-1] if retning else linje[0]
                neste = next((t for t in ender.get(nk(ende), []) if id(t) not in brukt), None)
                if not neste:
                    break
                brukt.add(id(neste))
                ny = neste[1] if nk(neste[0]) == nk(ende) else neste[0]
                linje.append(ny) if retning else linje.insert(0, ny)
        linjer.append(linje)
    return linjer


def svg(seed, bredde, hull=0.0, steg=1.0):
    """Kurvekart bredde x H mm, sentrert på x = 0. Hver femte kurve hvit, resten FR4."""
    h = felt(seed, bredde, hull)
    sti = {True: [], False: []}
    for n, segs in kurver(h, -bredde / 2, bredde / 2, 0, H, steg).items():
        for l in kjede(segs):
            if hull and all(abs(x) < hull - 0.5 for x, _ in l):
                continue          # ligger bak racket
            sti[n % 5 == 0].append("M" + " ".join(f"{x:.1f} {y:.1f}" for x, y in l))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-bredde / 2} 0 {bredde} {H}" '
            f'preserveAspectRatio="xMidYMin slice"><g fill="none" stroke-linecap="round" stroke-linejoin="round">'
            f'<path stroke="#4a4434" stroke-width=".18" d="{"".join(sti[False])}"/>'
            f'<path stroke="#f4f1e8" stroke-opacity=".55" stroke-width=".2" d="{"".join(sti[True])}"/></g></svg>')


if __name__ == "__main__":
    # selvtest: kantene er like, og kurvene ved racket følger kant(y)
    f = felt(1, 600, 100)
    assert f(-50, 30) == kant(30) and abs(f(100.001, 77) - kant(77)) < 1e-6
    assert len(kjede([((0, 0), (1, 0)), ((1, 0), (2, 0)), ((5, 5), (6, 6))])) == 2
    print("ok")
