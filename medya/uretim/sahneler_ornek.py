"""Gün 1 sahne görselleri: Fonrunch ve DİLLİ (1080x1920, temsili arayüz çizimleri)."""
import math, random, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
FD = Path("/home/claude/vikki_ortak/engine/vikki/fonts")
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/claude/gun1/assets")
OUT.mkdir(parents=True, exist_ok=True)


def F(name, size):
    return ImageFont.truetype(str(FD / f"{name}.ttf"), size)


BOLD, MED, REG, DJ = "Poppins-Bold", "Poppins-Medium", "Poppins-Regular", "DejaVuSans-Bold"


def bg(top, bottom, glow=None, seed=1):
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / H
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    if glow:
        g = Image.new("RGB", (W, H), (0, 0, 0))
        gd = ImageDraw.Draw(g)
        for (x, y, r, col) in glow:
            gd.ellipse([x - r, y - r, x + r, y + r], fill=col)
        import numpy as np
        g = g.filter(ImageFilter.GaussianBlur(160))
        arr = np.asarray(im, dtype="float32") + np.asarray(g, dtype="float32") * 0.55
        im = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))
    # ince yıldız/nokta dokusu (Noyansis gece teması)
    d = ImageDraw.Draw(im)
    rnd = random.Random(seed)
    for _ in range(90):
        x, y = rnd.randrange(W), rnd.randrange(H)
        a = rnd.randrange(40, 110)
        d.point((x, y), fill=(a, a, a + 20))
    return im


def rr(d, box, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def phone(im, x0=190, y0=560, w=700, h=1240):
    """Telefon çerçevesi çizer, ekran kutusunu döndürür."""
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle([x0 + 10, y0 + 30, x0 + w + 10, y0 + h + 30], 90, fill=(0, 0, 0, 170))
    sh = sh.filter(ImageFilter.GaussianBlur(30))
    im.paste(sh, (0, 0), sh)
    d = ImageDraw.Draw(im)
    rr(d, [x0, y0, x0 + w, y0 + h], 90, fill=(18, 20, 28), outline=(70, 76, 96), width=4)
    sx0, sy0, sx1, sy1 = x0 + 26, y0 + 26, x0 + w - 26, y0 + h - 26
    rr(d, [sx0, sy0, sx1, sy1], 68, fill=(12, 16, 28))
    rr(d, [x0 + w / 2 - 70, y0 + 44, x0 + w / 2 + 70, y0 + 78], 17, fill=(0, 0, 0))
    return (sx0, sy0, sx1, sy1)


def ctext(d, cx, y, s, font, fill):
    w = d.textlength(s, font=font)
    d.text((cx - w / 2, y), s, font=font, fill=fill)


# ---------------------------------------------------------------- FONRUNCH
FG = (45, 212, 160)      # Fonrunch yeşili
FBG = ((8, 14, 26), (10, 30, 34))


def f_app_header(d, s, title="Fonrunch"):
    sx0, sy0, sx1, _ = s
    d.text((sx0 + 50, sy0 + 90), title, font=F(BOLD, 44), fill=(235, 240, 245))
    rr(d, [sx1 - 120, sy0 + 92, sx1 - 50, sy0 + 140], 24, fill=(30, 40, 52))
    d.ellipse([sx1 - 102, sy0 + 104, sx1 - 78, sy0 + 128], fill=FG)


def fonrunch_1():
    im = bg(*FBG, glow=[(540, 1250, 420, (20, 120, 95))], seed=11)
    d = ImageDraw.Draw(im)
    chips = [("Hisse", 150, 700, (99, 102, 241)), ("Fon", 640, 640, (45, 212, 160)),
             ("Altın", 250, 1010, (234, 179, 8)), ("Döviz", 600, 960, (56, 189, 248)),
             ("Kripto", 170, 1330, (249, 115, 22)), ("Nakit", 620, 1290, (148, 163, 184)),
             ("Banka A", 120, 1600, (71, 85, 105)), ("Cüzdan", 600, 1560, (71, 85, 105))]
    f = F(BOLD, 52)
    for (t, x, y, c) in chips:
        tw = d.textlength(t, font=f)
        rr(d, [x, y, x + tw + 110, y + 112], 56, fill=(20, 28, 40), outline=c, width=4)
        d.ellipse([x + 30, y + 40, x + 62, y + 72], fill=c)
        d.text((x + 80, y + 22), t, font=f, fill=(235, 240, 245))
    # dağınık kesik çizgiler
    for (a, b) in [((300, 810), (690, 750)), ((420, 1120), (690, 1070)), ((330, 1440), (700, 1400))]:
        for k in range(0, 20, 2):
            p = [a[i] + (b[i] - a[i]) * k / 20 for i in range(2)]
            q = [a[i] + (b[i] - a[i]) * (k + 1) / 20 for i in range(2)]
            d.line([tuple(p), tuple(q)], fill=(60, 72, 90), width=4)
    return im


def fonrunch_2():
    im = bg(*FBG, glow=[(540, 1150, 380, (20, 110, 90))], seed=12)
    s = phone(im)
    d = ImageDraw.Draw(im)
    sx0, sy0, sx1, sy1 = s
    f_app_header(d, s)
    rr(d, [sx0 + 40, sy0 + 190, sx1 - 40, sy0 + 470], 40, fill=(20, 32, 40))
    d.text((sx0 + 80, sy0 + 220), "Toplam değer", font=F(MED, 34), fill=(150, 165, 180))
    d.text((sx0 + 80, sy0 + 270), "₺ ——", font=F(BOLD, 96), fill=(240, 245, 248))
    # dağılım çubuğu
    parts = [(0.34, (99, 102, 241), "Hisse"), (0.22, (45, 212, 160), "Fon"), (0.18, (234, 179, 8), "Altın"),
             (0.14, (56, 189, 248), "Döviz"), (0.12, (249, 115, 22), "Kripto")]
    x = sx0 + 60; bw = (sx1 - 60) - (sx0 + 60); y = sy0 + 540
    for i, (p, c, _) in enumerate(parts):
        ww = bw * p
        d.rectangle([x, y, x + ww - 6, y + 44], fill=c)
        x += ww
    y = sy0 + 640
    for (p, c, n) in parts:
        rr(d, [sx0 + 40, y, sx1 - 40, y + 104], 30, fill=(20, 28, 38))
        d.ellipse([sx0 + 78, y + 36, sx0 + 110, y + 68], fill=c)
        d.text((sx0 + 140, y + 26), n, font=F(MED, 40), fill=(225, 232, 240))
        rr(d, [sx1 - 230, y + 40, sx1 - 230 + int(150 * p / 0.34), y + 64], 12, fill=c)
        y += 122
    return im


def fonrunch_3():
    im = bg(*FBG, glow=[(540, 1150, 380, (20, 110, 90))], seed=13)
    s = phone(im)
    d = ImageDraw.Draw(im)
    sx0, sy0, sx1, sy1 = s
    f_app_header(d, s, "Risk")
    cx, cy, r = (sx0 + sx1) / 2, sy0 + 560, 230
    d.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=(40, 52, 66), width=46)
    segs = [(180, 240, (45, 212, 160)), (240, 300, (234, 179, 8)), (300, 330, (249, 115, 22))]
    for a, b, c in segs:
        d.arc([cx - r, cy - r, cx + r, cy + r], a, b, fill=c, width=46)
    ang = math.radians(318)
    d.line([(cx, cy), (cx + (r - 50) * math.cos(ang), cy + (r - 50) * math.sin(ang))], fill=(240, 245, 248), width=12)
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=(240, 245, 248))
    ctext(d, cx, cy + 40, "Portföy risk skoru", F(MED, 38), (160, 172, 186))
    y = cy + 140
    for (k, v, c) in [("En büyük pozisyon", "Tek varlık", (249, 115, 22)),
                      ("Yoğunlaşma", "Yüksek", (234, 179, 8)),
                      ("Varlık sayısı", "5 tür", (45, 212, 160))]:
        rr(d, [sx0 + 40, y, sx1 - 40, y + 116], 30, fill=(20, 28, 38))
        d.text((sx0 + 70, y + 36), k, font=F(MED, 33), fill=(205, 214, 224))
        tw = d.textlength(v, font=F(BOLD, 33))
        d.text((sx1 - 70 - tw, y + 36), v, font=F(BOLD, 33), fill=c)
        y += 134
    return im


def fonrunch_4():
    im = bg(*FBG, glow=[(540, 1150, 380, (20, 110, 90))], seed=14)
    s = phone(im)
    d = ImageDraw.Draw(im)
    sx0, sy0, sx1, sy1 = s
    f_app_header(d, s, "Piyasa radarı")
    rnd = random.Random(4)
    y = sy0 + 200
    for n in ["BIST 100", "USD/TRY", "EUR/TRY", "Gram altın", "Brent", "VIX"]:
        rr(d, [sx0 + 40, y, sx1 - 40, y + 140], 32, fill=(20, 28, 38))
        d.text((sx0 + 76, y + 44), n, font=F(MED, 42), fill=(225, 232, 240))
        # temsili küçük grafik (rakamsız)
        pts, v = [], 0.5
        for k in range(14):
            v = min(0.9, max(0.1, v + rnd.uniform(-0.18, 0.2)))
            pts.append((sx1 - 300 + k * 18, y + 112 - v * 84))
        col = FG if pts[-1][1] < pts[0][1] else (244, 114, 114)
        d.line(pts, fill=col, width=6, joint="curve")
        y += 160
    return im


def fonrunch_5():
    im = bg(*FBG, glow=[(540, 1150, 380, (20, 110, 90))], seed=15)
    s = phone(im)
    d = ImageDraw.Draw(im)
    sx0, sy0, sx1, sy1 = s
    f_app_header(d, s, "Koç")
    rr(d, [sx0 + 40, sy0 + 210, sx1 - 40, sy0 + 620], 40, fill=(16, 44, 42), outline=FG, width=3)
    rr(d, [sx0 + 76, sy0 + 248, sx0 + 176, sy0 + 348], 30, fill=FG)
    ctext(d, sx0 + 126, sy0 + 262, "K", F(BOLD, 56), (8, 30, 26))
    d.text((sx0 + 200, sy0 + 270), "Bulgu", font=F(BOLD, 40), fill=FG)
    lines = ["Portföyünün büyük", "kısmı tek bir", "varlıkta toplanmış."]
    y = sy0 + 380
    for L in lines:
        d.text((sx0 + 80, y), L, font=F(MED, 42), fill=(235, 242, 245)); y += 62
    y = sy0 + 680
    for t, w in [("Dağılımı incele", 0.8), ("Stres testi (Premium)", 0.62), ("30 günlük değerleme", 0.7)]:
        rr(d, [sx0 + 40, y, sx1 - 40, y + 110], 30, fill=(20, 28, 38))
        d.text((sx0 + 80, y + 32), t, font=F(MED, 38), fill=(205, 214, 224))
        ctext(d, sx1 - 90, y + 26, "›", F(BOLD, 48), (120, 134, 150))
        y += 128
    return im


def fonrunch_son():
    im = bg((6, 12, 22), (8, 34, 32), glow=[(540, 900, 440, (24, 130, 104))], seed=16)
    d = ImageDraw.Draw(im)
    rr(d, [390, 520, 690, 820], 80, fill=(14, 40, 38), outline=FG, width=6)
    # logo yerine basit grafik simgesi
    d.line([(450, 740), (510, 670), (565, 705), (630, 600)], fill=FG, width=22, joint="curve")
    d.ellipse([612, 582, 648, 618], fill=FG)
    ctext(d, 540, 900, "FONRUNCH", F(BOLD, 120), (240, 248, 246))
    ctext(d, 540, 1060, "Portföyünü anlayan bir koç.", F(MED, 52), (180, 200, 205))
    rr(d, [170, 1220, 910, 1350], 65, fill=FG)
    ctext(d, 540, 1255, "Google Play'de ücretsiz", F(BOLD, 48), (6, 30, 26))
    ctext(d, 540, 1440, "noyansis.com", F(BOLD, 56), (230, 238, 242))
    ctext(d, 540, 1720, "Bilgilendirme amaçlıdır, yatırım tavsiyesi değildir.", F(REG, 30), (130, 148, 158))
    ctext(d, 540, 1765, "Temsili arayüz görüntüleri.", F(REG, 30), (130, 148, 158))
    return im


# ---------------------------------------------------------------- DİLLİ
BLUE, ORANGE = (59, 130, 246), (249, 115, 22)
DBG = ((10, 12, 30), (24, 16, 40))


def bubble(d, x0, y0, x1, text, col, font, tail="left", txtcol=(255, 255, 255)):
    lines = text.split("\n")
    tw = max(d.textlength(L, font=font) for L in lines) + 88
    if tail == "left":
        x1 = x0 + tw
    else:
        x0 = x1 - tw
    lh = font.size + 16
    h = 60 + lh * len(lines)
    rr(d, [x0, y0, x1, y0 + h], 46, fill=col)
    if tail == "left":
        d.polygon([(x0 + 40, y0 + h - 10), (x0 + 10, y0 + h + 34), (x0 + 100, y0 + h - 10)], fill=col)
    else:
        d.polygon([(x1 - 40, y0 + h - 10), (x1 - 10, y0 + h + 34), (x1 - 100, y0 + h - 10)], fill=col)
    y = y0 + 30
    for L in lines:
        d.text((x0 + 44, y), L, font=font, fill=txtcol); y += lh
    return y0 + h


def dilli_1():
    im = bg(*DBG, glow=[(260, 900, 300, (30, 60, 140)), (820, 1300, 300, (140, 60, 20))], seed=21)
    d = ImageDraw.Draw(im)
    bubble(d, 80, 720, 0, "Merhaba, bir sorum var…", BLUE, F(MED, 52))
    bubble(d, 0, 1000, 1000, "Excuse me, can you help?", ORANGE, F(MED, 52), tail="right")
    ctext(d, 540, 1330, "?", F(BOLD, 300), (90, 96, 130))
    return im


def person(d, cx, cy, col):
    d.ellipse([cx - 90, cy - 230, cx + 90, cy - 50], fill=col)
    d.pieslice([cx - 190, cy - 20, cx + 190, cy + 360], 180, 360, fill=col)


def dilli_2():
    im = bg(*DBG, glow=[(540, 1250, 360, (60, 50, 120))], seed=22)
    d = ImageDraw.Draw(im)
    person(d, 230, 1250, BLUE)
    person(d, 850, 1250, ORANGE)
    # masa
    rr(d, [60, 1430, 1020, 1500], 30, fill=(48, 44, 70))
    # telefon masada (ortada)
    rr(d, [380, 1060, 700, 1430], 44, fill=(20, 22, 32), outline=(90, 96, 120), width=4)
    rr(d, [400, 1080, 680, 1410], 32, fill=(14, 16, 30))
    rr(d, [420, 1140, 660, 1230], 24, fill=BLUE)
    rr(d, [420, 1260, 660, 1350], 24, fill=ORANGE)
    ctext(d, 540, 1157, "TR", F(BOLD, 44), (255, 255, 255))
    ctext(d, 540, 1277, "EN", F(BOLD, 44), (255, 255, 255))
    return im


def dilli_screen(a_text, a_col, b_text, b_col, active):
    im = bg(*DBG, glow=[(540, 1150, 380, (50, 50, 130))], seed=23)
    s = phone(im)
    d = ImageDraw.Draw(im)
    sx0, sy0, sx1, sy1 = s
    d.text((sx0 + 50, sy0 + 90), "DİLLİ", font=F(BOLD, 48), fill=(240, 242, 250))
    rr(d, [sx1 - 250, sy0 + 92, sx1 - 50, sy0 + 146], 27, fill=(30, 32, 52))
    ctext(d, sx1 - 150, sy0 + 98, "TR ⇄ EN", F(DJ, 30), (210, 214, 235))
    y = bubble(d, sx0 + 40, sy0 + 230, 0, a_text, a_col, F(MED, 42))
    bubble(d, 0, y + 80, sx1 - 40, b_text, b_col, F(MED, 42), tail="right")
    # alt düğmeler
    by = sy1 - 260
    for i, (lab, col) in enumerate([("Türkçe", BLUE), ("English", ORANGE)]):
        x0 = sx0 + 40 + i * ((sx1 - sx0 - 80) / 2 + 10)
        x1 = x0 + (sx1 - sx0 - 80) / 2 - 10
        on = (active == i)
        rr(d, [x0, by, x1, by + 190], 50, fill=col if on else (28, 30, 46), outline=col, width=5)
        ctext(d, (x0 + x1) / 2, by + 34, "●" if on else "○", F(DJ, 52), (255, 255, 255) if on else col)
        ctext(d, (x0 + x1) / 2, by + 108, lab, F(BOLD, 40), (255, 255, 255) if on else (210, 214, 235))
    return im


def dilli_5():
    im = bg(*DBG, glow=[(540, 1150, 420, (60, 50, 130))], seed=25)
    d = ImageDraw.Draw(im)
    langs = ["Türkçe", "English", "Español", "Deutsch", "Français", "Italiano",
             "Русский", "Português", "Nederlands", "Polski", "Svenska", "Ελληνικά"]
    f = F(DJ, 50)
    cols = [BLUE, ORANGE, (168, 85, 247), (20, 184, 166)]
    y, i = 720, 0
    rows = [langs[0:2], langs[2:4], langs[4:6], langs[6:8], langs[8:10], langs[10:12]]
    for row in rows:
        widths = [d.textlength(t, font=f) + 100 for t in row]
        total = sum(widths) + 40 * (len(row) - 1)
        x = (W - total) / 2
        for t, w in zip(row, widths):
            c = cols[i % 4]; i += 1
            rr(d, [x, y, x + w, y + 110], 55, fill=(26, 26, 48), outline=c, width=4)
            d.text((x + 50, y + 24), t, font=f, fill=(238, 240, 250))
            x += w + 40
        y += 150
    ctext(d, 540, y + 40, "+ daha fazlası", F(MED, 48), (170, 176, 210))
    return im


def dilli_son():
    im = bg((8, 10, 26), (30, 16, 40), glow=[(380, 860, 300, (30, 70, 170)), (700, 860, 300, (170, 70, 20))], seed=26)
    d = ImageDraw.Draw(im)
    rr(d, [300, 560, 600, 790], 70, fill=BLUE)
    d.polygon([(340, 780), (320, 850), (420, 785)], fill=BLUE)
    rr(d, [480, 640, 780, 870], 70, fill=ORANGE)
    d.polygon([(740, 860), (760, 930), (660, 865)], fill=ORANGE)
    ctext(d, 450, 625, "Aa", F(BOLD, 88), (255, 255, 255))
    ctext(d, 630, 705, "Bb", F(BOLD, 88), (255, 255, 255))
    ctext(d, 540, 1000, "DİLLİ", F(BOLD, 140), (245, 246, 252))
    ctext(d, 540, 1180, "İki dil, bir telefon,", F(MED, 54), (190, 194, 222))
    ctext(d, 540, 1250, "kesintisiz sohbet.", F(MED, 54), (190, 194, 222))
    rr(d, [260, 1390, 820, 1520], 65, fill=(245, 246, 252))
    ctext(d, 540, 1423, "Google Play'den al", F(BOLD, 50), (20, 22, 44))
    ctext(d, 540, 1600, "noyansis.com", F(BOLD, 56), (230, 232, 245))
    ctext(d, 540, 1765, "Temsili arayüz görüntüleri.", F(REG, 30), (130, 134, 160))
    return im


SCENES = {
    "fon_1": fonrunch_1, "fon_2": fonrunch_2, "fon_3": fonrunch_3, "fon_4": fonrunch_4,
    "fon_5": fonrunch_5, "fon_son": fonrunch_son,
    "dil_1": dilli_1, "dil_2": dilli_2,
    "dil_3": lambda: dilli_screen("İstasyon nerede?", BLUE, "Where is the station?", (52, 56, 84), 0),
    "dil_4": lambda: dilli_screen("Two blocks ahead.", ORANGE, "İki sokak ileride.", (52, 56, 84), 1),
    "dil_5": dilli_5, "dil_son": dilli_son,
}

if __name__ == "__main__":
    for k, fn in SCENES.items():
        fn().save(OUT / f"{k}.png")
        print("ok", k)
