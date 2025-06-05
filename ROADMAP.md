# ROADMAP.md: Python ile Dosya Bütünlüğü ve Hash Doğrulama Aracı Geliştirme

## Giriş

Bu yol haritası, dosya bütünlüğünü kontrol etmeye yönelik geliştirilen açık kaynaklı bir Python aracı olan **FileHashCheck** projesinin geliştirme sürecini adım adım açıklamaktadır. Bu araç, hash algoritmalarını kullanarak dosya veya klasör bazlı bütünlük doğrulaması yapar. Ayrıca JSON dışa aktarım, karşılaştırma ve yeniden adlandırma gibi gelişmiş özellikler sunar.

**Not:** Bu proje yalnızca etik, yasal ve eğitim amaçlıdır. Başkalarının dosya sistemlerinde veya cihazlarında izinsiz işlem yapmak yasa dışıdır.

## Ön Koşullar

* **Python 3.x**: Geliştirme için temel dil
* **Kütüphaneler**:

  * `colorama`: Terminal çıktıları için renkli yazı desteği (`pip install colorama`)
* **Bilgi Gereksinimleri**:

  * Python temel programlama bilgisi
  * Komut satırı kullanımı (Windows/Linux)
  * Hash algoritmalarına genel aşinalık (MD5, SHA1, SHA256)

## Test Ortamını Kurma

Test ortamı oluşturmak ve uygulamayı doğru şekilde çalıştırmak için şu adımlar izlenmelidir:

1. **Python Kurulumu**: Python 3.7+ sistemde yüklü olmalıdır.
2. **Projenin İndirilmesi**:

   ```bash
   git clone https://github.com/emirsenler/FileHashCheck-project.git
   cd FileHashCheck-project
   ```
3. **Sanal Ortam ve Kurulum**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Temel Bileşenlerin Geliştirilmesi

### Hash Hesaplama

Python’un `hashlib` modülü kullanılarak SHA256, SHA1 ve MD5 algoritmaları ile dosya hash değerleri hesaplanır. Her dosya için otomatik olarak üç algoritma da çalıştırılır.

### Karşılaştırma ve Doğrulama

Kullanıcıdan alınan referans hash değeri ile hesaplanan değerler karşılaştırılır. Eşleşme varsa “UYUMLU”, yoksa “UYUŞMUYOR” mesajı verilir.

### JSON Çıktı

Her dosya sonucu; hash değerleri, boyutu, karşılaştırma sonuçları gibi detaylarla birlikte JSON formatında dışa aktarılabilir.

### Renkli Terminal Çıktısı

`colorama` kütüphanesi sayesinde başarı ve hata durumları yeşil/kırmızı renkte gösterilir.

### Klasör Tarama Desteği

`--dir` parametresi ile klasör içinde bulunan tüm dosyalar taranır, recursive olarak işlem yapılır.

### Dosya Yeniden Adlandırma

İsteğe bağlı olarak `--rename-by-hash` seçeneği kullanılarak dosya adı hash değeriyle değiştirilir.

### Loglama

Tüm sonuçlar `hashcheck.log` dosyasına JSON formatında kaydedilir.

## Gelişmiş Geliştirmeler

### Dinamik Algoritma Seçimi

Kullanıcı `--algos sha1 sha256` gibi komutlarla sadece seçtiği algoritmaları kullanabilir.

### Gelecekteki Geliştirmeler (Planlı)

* VirusTotal API entegrasyonu ile hash’lerin zararlı yazılımlarla eşleşip eşleşmediğini kontrol etme
* GUI (grafik arayüz) desteği
* HMAC destekli gelişmiş doğrulama

## Geliştirmelerin Test Edilmesi

1. **Tek Dosya Testi**

   ```bash
   python filehashcheck.py --filepath test.txt --sha256 abc123... --export sonuc.json
   ```

2. **Klasör Taraması**

   ```bash
   python filehashcheck.py --dir ./Belgeler --algos sha1 sha256 --export hepsi.json
   ```

3. **Yeniden Adlandırma**

   ```bash
   python filehashcheck.py --filepath belge.pdf --rename-by-hash sha256
   ```

4. **Log ve JSON Doğrulama**

   * `hashcheck.log` dosyasını ve oluşturulan JSON dosyalarını kontrol edin.

## Karşı Önlemler ve En İyi Uygulamalar

* **Referans hash’leri güvenli ortamda saklayın**
* **SHA256 kullanımı önerilir** (MD5/SHA1 artık güvenli sayılmaz)
* **Sonuçları log dosyasında tutarak izlenebilirlik sağlayın**

## Sonuç

`FileHashCheck`, Python ile geliştirilmiş hafif, modüler ve pratik bir dosya doğrulama aracıdır. Komut satırından kolayca kullanılabilir, otomasyon sistemlerine entegre edilebilir ve açık kaynak olarak geliştirilmeye açıktır.

Etik, açık ve sürdürülebilir yazılım geliştirme ilkeleriyle geliştirilmeye devam etmektedir.
