from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack
import unittest

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/'

@ddt
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)        


    def setUp(self) -> None:
        self.driver.get(URL_PAGE)

    @data([2, 5, 10], [3, 10, 30], [1, 7, 7])
    @unpack
    def testProducto(self, num1, num2, res) -> None:
        resultado = num1 * num2
        print(resultado)
        self.assertEqual(resultado, res)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()