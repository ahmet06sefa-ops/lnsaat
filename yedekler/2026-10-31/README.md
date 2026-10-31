# İnce işler – kullanılmayan üretim yedekleri

31 Ekim 2026 tarihinde, çalışan web sitesinin kullanmadığı görsel orijinalleri ve üretim betikleri yedeklenmiştir. Bu klasör **çalışan web sitesi değildir**; sitede kullanılan sıkıştırılmış görseller site projesinde ayrıca bulunur.

- `ince_isler_assets/`: Önceki görsellerin PNG orijinalleri ve eski JPG kopyaları.
- `ince_isler_yeni_gorsel_orijinalleri/`: Görsel anlatımların PNG orijinalleri.
- `ince_isler_malzeme_orijinalleri/`: Malzeme çizimlerinin PNG orijinalleri. `malzeme-profil.png` yalnızca kavramsal taslaktır; hassas C/U profil ayrıntısı için kullanılmamalıdır.
- `uretici-betikleri/`: Daha önceki PDF/görsel üretim betiklerinin yedek kopyaları. Yerel yol ve bağımlılıkları bulunur; gerektiğinde uyarlanmalıdır.

Kullanıcının yüklediği PDF, çıkarılmış metni, şifreler, çalışan site projesi, bağımlılıklar, derleme çıktıları ve önbellekler bu yedeğe eklenmemiştir. `SHA256SUMS` dosyası içerik bütünlüğünü kontrol etmek içindir.

Yedeği indirdikten sonra (Linux/macOS):

```sh
cd yedekler/2026-10-31
sha256sum -c SHA256SUMS
# Gerekirse seçili klasörü çalışma alanına geri kopyala:
cp -a ince_isler_malzeme_orijinalleri ~/ 
```

Bu depo herkese açıksa içindeki tüm dosyalar da herkese açıktır. Bu veriler yedek amaçlıdır; teknik çizim veya üretici belgesi yerine geçmez.
