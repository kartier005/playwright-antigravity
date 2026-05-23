# GÖRSEL PROGRAMLAMA FİNAL ÖDEVİ

Bu proje, Görsel Programlama dersi final ödevi kapsamında hazırlanmıştır. Ödevin gereksinimleri doğrultusunda **Google Antigravity** kullanılarak araştırma yapılmış ve **Playwright** ile bir web scraping (veri çekme) otomasyon projesi geliştirilmiştir.

---

## ADIM 1: Google Antigravity Nedir ve Özellikleri Nelerdir?

**Google Antigravity**, Google DeepMind tarafından geliştirilen "Advanced Agentic Coding" (İleri Düzey Ajan Tabanlı Kodlama) tabanlı, yapay zeka destekli otonom bir yazılım asistanıdır. Geleneksel yapay zekalardan en büyük farkı, sadece kod veya metin üretmekle kalmayıp, kullanıcının bilgisayarında **aktif bir geliştirici gibi çalışabilmesidir.**

**Temel Özellikleri:**
- **Otonom Terminal Kullanımı:** Kullanıcının bilgisayarındaki komut satırına (PowerShell/Bash) erişerek komutlar çalıştırabilir, kütüphaneler kurabilir, sunucuları ayağa kaldırabilir.
- **Dosya Sistemi Erişimi:** Proje dizinlerini tarayabilir, yeni dosyalar oluşturabilir, kodları analiz edip düzenleyebilir ve hataları (bug) çözebilir.
- **Microservice ve Mimari Anlayışı:** Docker, RabbitMQ, Redis, React, FastAPI gibi modern yazılım mimarilerinde uçtan uca sistemler kurabilir.
- **Gerçek Zamanlı İletişim:** Verilen direktifleri uygularken bir yandan da arka planda çalışan görevlerin (logların) çıktılarını anlık olarak okur ve hataları kendi kendine düzeltir.

*(Bu proje, bizzat Google Antigravity tarafından planlanmış, Playwright kütüphaneleri kurulmuş ve kodlanmıştır.)*

---

## ADIM 2: Playwright Nedir ve Özellikleri Nelerdir?

**Playwright**, Microsoft tarafından açık kaynak kodlu olarak geliştirilen, modern web uygulamaları için bir **Uçtan Uca (End-to-End) Test ve Otomasyon** kütüphanesidir. Selenium gibi eski nesil araçların yerini alması amacıyla modern web teknolojilerine uygun tasarlanmıştır.

**Temel Özellikleri:**
- **Çoklu Tarayıcı Desteği:** Tek bir API ile Chromium (Chrome/Edge), WebKit (Safari) ve Firefox tarayıcılarını aynı anda kontrol edebilir.
- **Auto-Wait (Otomatik Bekleme):** Elementlerin yüklenmesini, tıklanabilir hale gelmesini veya animasyonların bitmesini otomatik bekler. Manuel `sleep` koymaya gerek bırakmaz (Flaky testleri engeller).
- **Headless & Headed Mod:** Tarayıcıyı hem arka planda gizli (headless=True) hem de ekranda görünür (headless=False) şekilde çalıştırabilir.
- **Ağ Kontrolü (Network Interception):** Web isteklerini (API çağrılarını, resimleri) yakalayabilir, değiştirebilir veya engelleyebilir.
- **Hızlı ve Asenkron:** Modern Python asenkron (asyncio) yapısını destekler, paralel işlemler yapabilir.

---

## ADIM 3: Örnek Proje (Quotes Scraper Bot)

Bu projede Playwright kütüphanesi kullanılarak bir veri çekme (Web Scraping) otomasyonu yapılmıştır.
Python kullanılarak yazılan `main.py` dosyası çalıştırıldığında şu işlemleri yapar:

1. Ekranda Chromium tabanlı bir tarayıcı açar.
2. `http://quotes.toscrape.com/` (Test amaçlı ünlü sözler sitesi) adresine gider.
3. Sayfadaki tüm sözleri ve o sözü söyleyen yazarları tespit eder.
4. Çektiği verileri ekrana yazdırır.
5. İşlem bitince tarayıcıyı kapatır ve Pandas kütüphanesi ile verileri **`unlu_sozler.xlsx`** adında bir Excel dosyasına kaydeder.

### Projeyi Çalıştırmak İçin
Terminalde veya CMD'de şu komutu çalıştırmanız yeterlidir:
```bash
python main.py
```
