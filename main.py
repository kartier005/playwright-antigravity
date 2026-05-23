from playwright.sync_api import sync_playwright
import pandas as pd
import time

def scrape_quotes():
    print("[1] Playwright baslatiliyor...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("[2] quotes.toscrape.com adresine gidiliyor...")
        page.goto("http://quotes.toscrape.com/")
    
        time.sleep(2)
        
        print("[3] Sayfadaki sozler ve yazarlar cekiliyor...")
        quotes_data = []
        quote_elements = page.query_selector_all(".quote")
        
        for quote in quote_elements:
            text = quote.query_selector(".text").inner_text()
            author = quote.query_selector(".author").inner_text()
            
            quotes_data.append({
                "Yazar": author,
                "Söz": text
            })
            print(f"Cekildi: {author} - {text[:30]}...")
            
        print(f"\nToplam {len(quotes_data)} soz basariyla cekildi!")
        
        time.sleep(2)
        browser.close()
        
        print("[4] Veriler Excel dosyasina kaydediliyor...")
        df = pd.DataFrame(quotes_data)
        df.to_excel("unlu_sozler.xlsx", index=False)
        print("[5] Islem tamamlandi! 'unlu_sozler.xlsx' dosyasini kontrol edebilirsiniz.")

if __name__ == "__main__":
    scrape_quotes()
