from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def test_chrome_navigation():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # ヘッドレスモードでブラウザ起動
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.google.com")
        title = driver.title
        print(f"Page title: {title}")
        assert "Google" in title
    finally:
        driver.quit()

if __name__ == "__main__":
    test_chrome_navigation()
