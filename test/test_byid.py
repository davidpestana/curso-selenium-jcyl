from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/'
class ColeccionEncontrarElementos(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)

    def setUp(self) -> None:
        self.driver.get(URL_PAGE)
        self.driver.find_element(By.CSS_SELECTOR, 'body > div > div > main > div > div > div > div > div > div > button').click()

    def testFindById(self) -> None:
        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')
        # username.text = 'mi_usuario'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()