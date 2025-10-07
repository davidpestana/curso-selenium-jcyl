from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless=new")

# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)

driver.get("https://example.com")
print(driver.title)

driver.quit()