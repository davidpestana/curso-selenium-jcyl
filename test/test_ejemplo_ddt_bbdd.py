from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack
import unittest
from utils.loadBBDD import load_bbdd_data

# URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/'





@ddt
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()        


    # def setUp(self) -> None:
    #     # self.driver.get(URL_PAGE)

    @data(*load_bbdd_data())
    @unpack
    def testProducto(self, num1, num2, res) -> None:
        resultado = num1 * num2
        # print(resultado)
        self.assertEqual(resultado, res)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()