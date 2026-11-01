# Noyansis ürün bilgi kartları (senaryo motorunun kaynağı)

Kaynak: kullanıcının 1 Kasım 2026'da gönderdiği canlı noyansis.com, fonrunch.com, Google Play ve uygulama ekran görüntüleri.
Kural: Videoda ve açıklamada yalnız bu dosyadaki bilgiler kullanılır. Burada olmayan özellik, rakam, fiyat yazılmaz.
Ekranlar: `ekranlar/<klasör>/`. Renkler: `ekranlar/<klasör>/renkler.json`. Simge: `ekranlar/<klasör>/simge.png`.

Noyansis: İzmir merkezli bağımsız yazılım stüdyosu. Windows için kurumsal arşiv ve arama yazılımları; Android için finans, vade takibi, sesli çeviri, seyahat ve yaratıcı ses üretimi uygulamaları. Destek: destek@noyansis.com. Web: noyansis.com.

## Fonrunch (klasör: fonrunch)
- Kategori: Portföy koçu / finans. Google Play: https://play.google.com/store/apps/details?id=com.derdihan.portfoykocu (ücretsiz; reklam ve uygulama içi satın alma içerir). Web: fonrunch.com.
- Tek cümle: Hisse senedi, TEFAS fonları, altın, döviz ve kripto varlıklarını tek tabloda toplayıp riskini hesaplayan akıllı portföy koçu.
- Özellikler: otomatik risk ve varlık yoğunlaşma skoru; BIST 100, TEFAS ve TCMB piyasa radarı; banka şifresi istemez, veriler cihazda kalır; stres testleri ve 30 günlük değerleme; Varlıklarım & bütçem (Varlıklar, Gelir–Gider, Ödeme Planı); AI Koç; uygulama arka planı Beyaz / Gece mavisi / Siyah / Mor; web ile eşitleme.
- Premium (Portföy Zekâ Laboratuvarı): yoğunlaşma matematiği (HHI, etkin pozisyon), veri güveni ve kapsama, varlık sınıfı ve kur hassasiyeti, kişisel yoğunlaşma sınırı, stres laboratuvarı ve kayıp bütçesi, Monte Carlo hedef simülatörü, borsalar arası kıyas, tarihsel değerleme. Premium önizlemede analiz yapısı açık, sayısal sonuçlar kilitli.
- Konumlandırma (fonrunch.com): piyasa terminali değil, aracı kurum değil, tahmin makinesi değil; kişisel finansal teşhis ürünü. "Rapor, rakamı değil anlamını gösterir."
- Zorunlu uyarı: "Bilgilendirme amaçlıdır, yatırım tavsiyesi değildir." Piyasa verisi görünen ekranlarda: "Piyasa verileri gösterge niteliğindedir, gecikmeli olabilir."
- Öne çıkarılmaz: "Satış yakında" olan Portföy Check-Up ve Kişisel Senaryo Paketi.

## DİLLİ (klasör: dilli)
- Kategori: Sesli çeviri. Google Play: https://play.google.com/store/apps/details?id=com.dilli.mobile (uygulama içi satın alma; fiyat ve koşullar Play'de).
- Tek cümle: Akıcı karşılıklı diyaloglar için bas-konuş sesli tercüman. "Konuş. Dilli çevirsin."
- Özellikler: bas-konuş ile anlık çift yönlü sesli çeviri; "İki kişi, iki dil": konuşacak kişi kendi düğmesini basılı tutar, konuşur, bırakır, Dilli çevirip karşı tarafa sesli okur; internetsiz çeviri paketleri; ses cihazda işlenir, sunuculara gitmez (Google ML Kit); sıfır analiz ve takip; kulaklık ve Bluetooth ile ses aktarımı; çeviri sesi Varsayılan / Kadın / Erkek; geniş dil listesi.
- Renkler: "Sen" mavi, "Karşı taraf" turuncu.

## Kolay Vize (klasör: kolay-vize)
- Kategori: Seyahat & vize. Google Play: https://play.google.com/store/apps/details?id=com.kolayvize.app
- Tek cümle: Evrak listeni hazırla, randevularını hatırla, konsolosluk bilgilerine tek yerden ulaş. (Vize sürecini planla, belgelerini takip et, güvenilir hizmetleri keşfet.)
- Özellikler: hedef ülke, seyahat amacı, pasaport türü ve tarihlerle hazırlık; evrak kontrol listesi ve hazırlık yüzdesi; seyahat tarihine geri sayım; randevu merkezi (resmî portallara hızlı erişim) ve randevu hatırlatıcısı; hatırlatıcılar; konsolosluk rehberi; seyahat hizmetlerini haritada bulma; özeti paylaşma. Schengen, ABD, İngiltere ve diğer ülkeler.
- ZORUNLU açıklama cümlesi: "Kolay Vize bağımsız bir bilgilendirme uygulamasıdır; hiçbir devlet kurumunu, konsolosluğu veya vize başvuru merkezini temsil etmez, vize onayı ya da randevu garantisi vermez." Resmî kurum logosu kullanılmaz.
- Gizlilik: ana ekranda `app_ana_maskeli.png` kullanılır (ülke/tarih satırı bulanık). Kullanıcı onay verirse `app_ana.png`.

## OpBo (klasör: opbo)
- Kategori: Ses & müzik. DURUM: 1 Kasım 2026'da Google Play'de herkese açık değil (aramada çıkmıyor, kullanıcı "özel" dedi). Yayına alınana kadar videosu yapılmaz.
- Tek cümle: Kendi sesiyle özgün ses, vokal ve müzik üretmek isteyen içerik üreticileri için yaratıcı mobil ses stüdyosu.
- Özellikler: uçak modunda internetsiz metinden sese (TTS); üretilen sesi doğrudan videoya senkronize ekleme; ses ve video cihazda işlenir, internet gerektirmez; hafif, pratik arayüz.
- Ekran: yok (yalnız simge). Gelene kadar temsili çizim + "temsili" notu.

## PİGES ONE (klasör: piges-one)
- Kategori: Windows masaüstü — kurumsal arşiv & arama. Satış ve indirme: noyansis.com (PayTR ile lisans). Windows 10/11 uyumlu.
- Tek cümle: Windows bilgisayardaki dağınık klasörleri, sektörel arşiv planlarını ve milyonlarca dosyayı saniyeler içinde tarayan, yerel çalışan masaüstü arama ve arşivleme programı.
- Özellikler: derin dosya adı ve sektörel arşiv planı taraması; salt okunur güvenli tarama (orijinal dosyalara dokunmaz); internetsiz ve yerel çalışır; PayTR ile tek tıkla lisans etkinleştirme.
- Ekran: yalnız site kartı (`web_kart.png`). Kullanıcının bilgisayarı yok; Windows arayüzü temsili çizilir + "temsili" notu. Google Play'e yönlendirilmez.

## Vadem (klasör: vadem)
- Kategori: Finans & vade. DURUM: paket com.noyansis.vadem, 1 Kasım 2026'da Google Play sayfası açılmıyor (404). Yayına alınana kadar videosu yapılmaz.
- Tek cümle: Çek, senet, kredi kartı ve kredi taksitlerini tek ekranda toplayan, şirket ve şahıs nakit akışını yöneten akıllı vade ve hatırlatma asistanı.
- Özellikler: alınan ve verilen çekler için ibraz süresi takibi; senetler için vade ve protesto süresi hatırlatıcısı; kredi kartı hesap kesim ve kredi taksit planları; firma bazlı tahsilat ve ödeme nakit akış takvimi.
- Ekran: yalnız site kartı ve simge. Gelene kadar temsili çizim + "temsili" notu.

## Golrunch (klasör: golrunch)
- Kategori: Futbol maç uygulaması. Google Play'de yayında: https://play.google.com/store/apps/details?id=com.macmercegi.mobile
- Bilgi az: ayrıntılı özellik yazılmaz; yalnız "futbol maçlarını takip" düzeyinde kal. Bahis/iddaa çağrışımı yapılmaz.
- Ekran: yok. Gelene kadar temsili çizim + "temsili" notu.
