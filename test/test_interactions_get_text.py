from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
import time

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/ejercicio8.html'
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

    def testTexto1(self) -> None:
        input = self.driver.find_element(By.ID, 'message')
        input.clear()
        input.send_keys("nuevo comentario")
        print(input.get_attribute('value'))


    def testTexto2(self) -> None:
        textarea = self.driver.find_element(By.ID, 'comments')
        textarea.clear()
        textarea.send_keys("nuevo comentario")

        print(textarea.get_attribute('value'), textarea.text)

        # self.assertEqual("nuevo comentario", textarea.get_attribute('value'), "El texto del textarea no es correcto")   


    def testTexto3(self) -> None:
        p = self.driver.find_element(By.ID, 'parrafo')
        message = p.text
        print(message)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()