from selenium import webdriver

def get_selenium_browser_version():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # CI向け

    driver = webdriver.Chrome(options=options)
    caps = driver.capabilities
    driver.quit()

    return {
        "browserVersion": caps.get("browserVersion"),
        "chrome": caps.get("chrome", {})
    }

def test_selenium_version():
    info = get_selenium_browser_version()
    assert info["browserVersion"] is not None