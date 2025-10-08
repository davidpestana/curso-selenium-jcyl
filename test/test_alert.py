from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/alert.html'
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)        
        cls.driver.get(URL_PAGE)
        cls.driver.find_element(By.CSS_SELECTOR, 'body > div > div > main > div > div > div > div > div > div > button').click()



    def setUp(self) -> None:
        pass

    def testAlert(self) -> None:
        btn = self.driver.find_element(By.ID,'show-alert')
        btn.click()
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, 'Has pulsado el botón...')
        alert.accept()
        alert.dismiss()
        alert.text = 'nuevo texto'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()