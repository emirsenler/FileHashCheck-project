<div align="center">
  <img src="https://img.shields.io/github/languages/count/emirsenler/FileHashCheck-project?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/emirsenler/FileHashCheck-project?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/emirsenler/FileHashCheck-project?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/emirsenler/FileHashCheck-project?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# Project Name
FileHashCheck-project

A brief, engaging description of your project.  
FileHashCheck, dosyaların dijital parmak izlerini (hash değerlerini) hesaplayarak bütünlüklerini denetleyen, karşılaştırma yapabilen ve sonuçları dışa aktarabilen gelişmiş bir Python aracıdır.
Siber güvenlikten sistem yönetimine kadar birçok alanda kullanılabilir; özellikle dosya manipülasyonu, veri güvenliği ve yazılım dağıtımı süreçlerinde hızlı ve güvenilir kontroller sağlar.

---

## Features / *Özellikler*

- **Multi-Algorithm Hash Calculation:** Calculates MD5, SHA1, and SHA256 hashes for files or folders.  
  *Çoklu Algoritma Desteği: Dosyalar için MD5, SHA1 ve SHA256 hash değerlerini hesaplar.*

- **Recursive Folder Scanning:** Automatically scans all files within a directory, including subfolders.  
  *Klasör Taraması: Belirtilen klasördeki tüm dosyaları (alt klasörler dahil) otomatik olarak tarar.*

- **Hash Comparison Capability:** Compares calculated hashes with provided reference hashes to check file integrity.  
  *Hash Karşılaştırması: Hesaplanan değerleri referans hash’lerle karşılaştırarak dosya bütünlüğünü doğrular.*

- **Hash-Based File Renaming:** Optionally renames files using their hash values to ensure uniqueness.  
  *Hash'e Göre Yeniden Adlandırma: Dosyaları isteğe bağlı olarak hash değerleriyle yeniden adlandırır.*

- **Colored CLI Output:** Displays comparison results in color-coded format for easy readability.  
  *Renkli Terminal Çıktısı: Sonuçları anlaşılır renklerle terminalde gösterir.*

- **JSON Result Exporting:** Allows exporting of results in structured JSON format for reporting or logging.  
  *JSON Dışa Aktarım: Sonuçları JSON formatında dışa aktararak raporlama ve arşivleme yapmanızı sağlar.*

- **Logging Support:** Automatically logs hash operations to a local log file (`hashcheck.log`).  
  *Loglama Desteği: Tüm işlemleri `hashcheck.log` dosyasına kaydeder.*

- **Command-Line Friendly:** Lightweight and fast, designed to be used in automated scripts or CI pipelines.  
  *Komut Satırı Dostu: Hafif, hızlı ve otomasyon sistemlerine entegre edilebilir yapıdadır.*


---

## Team / *Ekip*

- **2320191043** - Emir Şenler:
  *Emir Şenler: Proje Sahibi*

---

## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*                   | Link                                                  | Description / *Açıklama*                                              |
|------------------------------------|-------------------------------------------------------|------------------------------------------------------------------------|
| Hash Algoritmaları Karşılaştırması | [researchs/hash-algorithms.md](researchs/hash-algorithms.md) | Overview of MD5, SHA1, and SHA256 algorithms and their use cases. / *MD5, SHA1 ve SHA256 algoritmalarının karşılaştırılması ve kullanım alanları.* |
| Dosya Bütünlüğü ve Güvenlik       | [researchs/file-integrity.md](researchs/file-integrity.md) | Importance of file integrity in cybersecurity. / *Siber güvenlikte dosya bütünlüğünün önemi.* |
| CLI Tabanlı Araçların Önemi        | [researchs/cli-tools.md](researchs/cli-tools.md)       | Advantages of using command-line tools in automation and scripting. / *Komut satırı araçlarının otomasyon ve betiklerdeki avantajları.* |
| Adli Bilişimde Hash Kullanımı      | [researchs/digital-forensics.md](researchs/digital-forensics.md) | How hash values are used to verify digital evidence. / *Dijital delillerin doğrulanmasında hash kullanımının rolü.* |
| Add More Research                  | *Link to your other research files*                   | *Description of the research / Araştırmanın açıklaması*                |

---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/emirsenler/FileHashCheck-project.git
   cd FileHashCheck-project
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python filehashcheck.py --filepath dosya.pdf --sha256 1e3d863a... --export sonuc.json
```

**Steps**:  
1. Prepare input data (The input should be an existing file or a folder path containing files to check.).  
2. Run the script with arguments (Use --filepath for a single file or --dir for a directory. You can also use --algos, --export, or --rename-by-hash optionally.).
3. Check output (Results are printed to the terminal and optionally saved in a JSON file. Logs are written to hashcheck.log.)

**Adımlar**:  
1. Giriş verilerini hazırlayın (Girdi olarak bir dosya ya da klasör yolu belirtin.)
2. Betiği argümanlarla çalıştırın (Tek dosya için --filepath, klasör taramak için --dir kullanın. --algos, --export veya --rename-by-hash gibi seçenekler opsiyoneldir.) 
3. Çıktıyı kontrol edin (Sonuçlar terminalde gösterilir, --export ile JSON dosyasına yazılır. İşlem geçmişi hashcheck.log dosyasına kaydedilir.)

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:emirsenler/FileHashCheck-project.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  

*Topluluk katkilerini memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler*

Thanks to:  
- Keyvan Arasteh (keyvan.arasteh@istinye.edu.tr)
- Istinye University

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim*

Project Maintainer: [Emir Şenler/Istinye University] - [emirsenler1907@gmail.com]
Found a bug? Open an issue.

Proje Sorumlusu: [Emir Şenler/Istinye University] - [emirsenler1907@gmail.com]. Hata bulursanız bir sorun bildirin.

---
