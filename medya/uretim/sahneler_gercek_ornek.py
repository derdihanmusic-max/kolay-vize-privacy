"""Gerçek ekran görüntüleriyle sahne üretimi (1080x1920): telefon çerçevesi + marka renkleri."""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
FD = Path("/home/claude/vikki_ortak/engine/vikki/fonts")
EK = Path("/home/claude/kolay-vize-privacy/medya/uretim/ekranlar")
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/claude/gun1/gercek")
OUT.mkdir(parents=True, exist_ok=True)
F = lambda n, s: ImageFont.truetype(str(FD / f"{n}.ttf"), s)
BOLD, MED, REG = "Poppins-Bold", "Poppins-Medium", "Poppins-Regular"


def gradient(top, bottom, glows=()):
    t = np.linspace(0, 1, H)[:, None, None]
    arr = np.array(top, "float32") * (1 - t) + np.array(bottom, "float32") * t
    arr = np.repeat(arr, W, axis=1)
    if glows:
        g = Image.new("RGB", (W, H))
        d = ImageDraw.Draw(g)
        for x, y, r, c in glows:
            d.ellipse([x - r, y - r, x + r, y + r], fill=c)
        arr = arr + np.asarray(g.filter(ImageFilter.GaussianBlur(170)), "float32") * 0.6
    return Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))


def rounded(im, r):
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], r, fill=255)
    out = Image.new("RGBA", im.size)
    out.paste(im.convert("RGB"), (0, 0), m)
    return out


def phone_with(bg, shot, top=470, max_w=700, max_h=1380, bezel=(10, 13, 22), edge=(52, 62, 88), anchor="top"):
    """Ekran görüntüsünü telefon çerçevesine yerleştirir. anchor=top: uzun ekranı üstten kırpar."""
    im = Image.open(shot).convert("RGB")
    scale = max_w / im.width
    sw, sh = max_w, int(im.height * scale)
    im = im.resize((sw, sh), Image.LANCZOS)
    if sh > max_h:  # uzun ekran: üst kısmı göster
        im = im.crop((0, 0, sw, max_h)) if anchor == "top" else im.crop((0, sh - max_h, sw, sh))
        sh = max_h
    pad = 22
    fw, fh = sw + pad * 2, sh + pad * 2 + 40
    x0 = (W - fw) // 2
    y0 = top
    # gölge
    sh_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh_l).rounded_rectangle([x0 + 8, y0 + 30, x0 + fw + 8, y0 + fh + 30], 70, fill=(0, 0, 0, 160))
    bg.paste(sh_l.filter(ImageFilter.GaussianBlur(28)), (0, 0), sh_l.filter(ImageFilter.GaussianBlur(28)))
    d = ImageDraw.Draw(bg)
    d.rounded_rectangle([x0, y0, x0 + fw, y0 + fh], 70, fill=bezel, outline=edge, width=4)
    d.rounded_rectangle([x0 + fw / 2 - 60, y0 + 14, x0 + fw / 2 + 60, y0 + 34], 10, fill=(0, 0, 0))
    scr = rounded(im, 46)
    bg.paste(scr, (x0 + pad, y0 + pad + 40), scr)
    return bg


def ctext(d, cx, y, s, font, fill):
    d.text((cx - d.textlength(s, font=font) / 2, y), s, font=font, fill=fill)


def icon(path, size, radius_ratio=0.22, white_tile=False):
    im = Image.open(path).convert("RGB").resize((size, size), Image.LANCZOS)
    return rounded(im, int(size * radius_ratio))


def end_card(bg, ikon, name, tagline, cta, cta_fill, cta_text, notes, name_col=(245, 246, 250), sub_col=(190, 196, 215)):
    d = ImageDraw.Draw(bg)
    ic = icon(ikon, 300)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).rounded_rectangle([390, 470, 690, 770], 70, fill=(0, 0, 0, 170))
    bg.paste(glow.filter(ImageFilter.GaussianBlur(26)), (0, 14), glow.filter(ImageFilter.GaussianBlur(26)))
    bg.paste(ic, (390, 460), ic)
    ctext(d, 540, 820, name, F(BOLD, 116), name_col)
    ctext(d, 540, 975, tagline, F(MED, 50), sub_col)
    tw = d.textlength(cta, font=F(BOLD, 48)) + 140
    d.rounded_rectangle([540 - tw / 2, 1110, 540 + tw / 2, 1236], 63, fill=cta_fill)
    ctext(d, 540, 1143, cta, F(BOLD, 48), cta_text)
    ctext(d, 540, 1320, "noyansis.com", F(BOLD, 56), name_col)
    nl = icon(EK / "noyansis" / "logo.png", 72, 0.25)
    bg.paste(nl, (396, 1452), nl)
    d.text((488, 1462), "NOYANSİS", font=F(BOLD, 44), fill=sub_col)
    y = 1700
    for n in notes:
        ctext(d, 540, y, n, F(REG, 30), (150, 158, 178)); y += 44
    return bg


# ------------------------------------------------------------ FONRUNCH (lacivert + altın)
FTOP, FBOT = (6, 12, 28), (14, 30, 66)
FGLOW = [(540, 1250, 430, (120, 90, 25))]
fon = EK / "fonrunch"
FON = [
    ("fon_g1", "app_varliklarim_butce.png", 500),
    ("fon_g2", "app_tanitim_piyasa.png", 500),
    ("fon_g3", "app_tanitim_butce.png", 500),
    ("fon_g4", "app_zeka_lab.png", 470),
    ("fon_g5", "app_stres_lab.png", 470),
    ("fon_g6", "web_finans_panelim.png", 600),
]

# ------------------------------------------------------------ DİLLİ (mavi + turuncu)
DTOP, DBOT = (8, 14, 40), (26, 18, 46)
DGLOW = [(220, 1100, 330, (25, 70, 190)), (860, 1500, 330, (170, 70, 25))]
dil = EK / "dilli"
DIL = [
    ("dil_g1", "app_konusma.png", 470),
    ("dil_g2", "app_dil_secimi.png", 470),
    ("dil_g3", "app_konusma.png", 470),
    ("dil_g4", "app_ses_ayari.png", 470),
    ("dil_g5", "app_dil_listesi.png", 470),
]

if __name__ == "__main__":
    for name, shot, top in FON:
        bg = gradient(FTOP, FBOT, FGLOW)
        mw = 1000 if shot.startswith("web_") else 700
        phone_with(bg, fon / shot, top=top, max_w=mw, max_h=1330, edge=(120, 100, 60)).save(OUT / f"{name}.png")
    end_card(gradient((5, 10, 24), (16, 30, 62), [(540, 620, 360, (150, 110, 30))]), fon / "simge.png",
             "FONRUNCH", "Akıllı portföy koçu", "Google Play'de ücretsiz", (241, 212, 146), (20, 24, 40),
             ["Bilgilendirme amaçlıdır, yatırım tavsiyesi değildir.",
              "Piyasa verileri gösterge niteliğindedir, gecikmeli olabilir."]).save(OUT / "fon_gson.png")
    for name, shot, top in DIL:
        bg = gradient(DTOP, DBOT, DGLOW)
        anchor = "bottom" if name == "dil_g3" else "top"
        phone_with(bg, dil / shot, top=top, max_w=700, max_h=1330, edge=(80, 96, 150), anchor=anchor).save(OUT / f"{name}.png")
    end_card(gradient((8, 12, 34), (34, 18, 44), [(380, 600, 300, (30, 80, 200)), (700, 640, 300, (190, 80, 30))]),
             dil / "simge.png", "DİLLİ", "Konuş. Dilli çevirsin.", "Google Play'den al", (245, 246, 252), (20, 24, 50),
             ["Görüntüler uygulamadan alınmıştır."]).save(OUT / "dil_gson.png")
    print("ok")
