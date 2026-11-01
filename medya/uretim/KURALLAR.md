# Noyansis günlük sosyal medya videoları

- Her gün 2 video: 10:00 ve 18:00 (Europe/Istanbul). Instagram Reels + TikTok + YouTube Shorts, Metricool markası `noyansis` (blogId 7718336).
- Sıra (her gün sıradaki iki ürün, 1 Kasım 2026 = gün 0): Fonrunch, DİLLİ, OpBo, Piges One, Golrunch, Vadem, Kolay Vize. Gün n: listedeki (2n) mod 7 ve (2n+1) mod 7.
- Ürün bilgisi yalnız noyansis.com kaynağından (derdihanmusic-max/fonrunch-site → sites/noyansis/public/<urun>.html); sayfası olmayan ürün için kendi deposunun README'si. Uydurma özellik, sahte rakam, fiyat yazılmaz.
- Video VIKKI motoruyla (derdihanmusic-max/VIKKI_ORTAK, engine/) üretilir; kalite kontrolü PASSED olmalı. 1080x1920, ~20-25 sn, telifsiz müzik (engine/scripts/muzik_uret.py).
- Görseller: Noyansis gece teması, temsili arayüz çizimi (bkz. sahneler_ornek.py). Her gün yeni sahneler ve yeni metin; önceki günlerin tekrarı olmaz.
- Paylaşım metni eksiksiz: açıklama, Google Play linki (varsa), noyansis.com, uygun uyarılar (Fonrunch: yatırım tavsiyesi değildir), 8-10 hashtag; YouTube başlığı + etiketler + kategori; TikTok başlığı.
- Video dosyası medya/<urun>-YYYY-MM-DD.mp4 olarak bu depoya gönderilir; Metricool raw.githubusercontent.com adresinden çeker.
