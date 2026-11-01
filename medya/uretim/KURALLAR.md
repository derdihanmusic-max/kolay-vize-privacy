# Noyansis günlük sosyal medya videoları

- Her gün 2 video: 10:00 ve 18:00 (Europe/Istanbul). Instagram Reels + TikTok + YouTube Shorts, Metricool markası `noyansis` (blogId 7718336).
- Sıra (her gün sıradaki iki ürün, 1 Kasım 2026 = gün 0): Fonrunch, DİLLİ, Kolay Vize, Piges One, Golrunch. Gün n: listedeki (2n) mod 5 ve (2n+1) mod 5. OpBo ve Vadem, Google Play'de herkese açık olana kadar sırada YOK (kullanıcı yayına aldığını söyleyince eklenir).
- Ürün bilgisi YALNIZ medya/uretim/urunler.md dosyasından (canlı siteden ve uygulamalardan doğrulanmış bilgi kartları). fonrunch-site deposundaki eski sayfalar güncel değildir, kullanılmaz. Uydurma özellik, sahte rakam, fiyat yazılmaz.
- Video VIKKI motoruyla (derdihanmusic-max/VIKKI_ORTAK, engine/) üretilir; kalite kontrolü PASSED olmalı. 1080x1920, ~20-25 sn, telifsiz müzik (engine/scripts/muzik_uret.py).
- Görseller: önce GERÇEK EKRANLAR (medya/uretim/ekranlar/<klasör>/app_*.png, web_*.png). Ekranı telefon çerçevesi içinde, ürünün renklerinde (renkler.json) bir zeminde göster; yakınlaşma/kaydırma ile hareket ver, uzun ekranlarda yukarı kaydır. Kapanış kartında ürün simgesi (simge.png) + Noyansis logosu (ekranlar/noyansis/logo.png). Gerçek ekranı olmayan ürün/sahne için temsili çizim (bkz. sahneler_ornek.py), ama ürünün gerçek renkleriyle.
- Her gün yeni sahne sırası, yeni kanca ve yeni metin; önceki günlerin tekrarı olmaz (Metricool'daki geçmiş gönderilere bak).
- Gerçek ekran kullanılan videoda açıklamaya "Görüntüler uygulamadan alınmıştır." yaz; çizim kullanılan videoda "Tanıtımda temsili arayüz görüntüleri kullanılmıştır." yaz.
- Üçüncü taraf içerik yok: haber başlıkları, başka kanalların yayınları, gerçek kişi fotoğrafları, Google Play arayüzü, resmî kurum logoları.
- Paylaşım metni eksiksiz: açıklama, Google Play linki (varsa), noyansis.com, uygun uyarılar (Fonrunch: yatırım tavsiyesi değildir), 8-10 hashtag; YouTube başlığı + etiketler + kategori; TikTok başlığı.
- Video dosyası medya/<urun>-YYYY-MM-DD.mp4 olarak bu depoya gönderilir; Metricool raw.githubusercontent.com adresinden çeker.

- Gerçek ekranlı sahneler için örnek betik: medya/uretim/sahneler_gercek_ornek.py (telefon çerçevesi, marka renkli zemin, simgeli kapanış kartı; 1 Kasım Fonrunch/DİLLİ videoları bununla yapıldı) ve medya/uretim/vikki_gorev_gercek_ornek.json. Yollar klon klasörüne göre düzenlenir. Gerçek ekranlı videolarda Instagram isAiGenerated, TikTok isAigc ve YouTube isAiGeneratedContent false.
