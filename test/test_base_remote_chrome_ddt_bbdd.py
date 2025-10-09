from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack
import unittest
# from utils.loadBBDD import load_bbdd_data
from utils.loadCSV  import load_csv_data

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/'
URL_GRID = "http://localhost:4444/wd/hub"

@ddt
class BaseChrome(unittest.TestCase):


    # @classmethod
    # def setUpClass(cls) -> None:
    #     pass

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(
            command_executor=URL_GRID,
            options=options
        )
        self.driver = driver    
        self.addCleanup(self.driver.quit)


        self.driver.get(URL_PAGE)

    @data(*load_csv_data('test/data/ejemplo_ddt.csv'))
    @unpack
    def testProducto1(self, num1, num2, res) -> None:
        resultado = num1 * num2
        # print(resultado)
        self.assertEqual(resultado, res)

    # @data(*load_bbdd_data())
    # @unpack
    # def testProducto2(self, num1, num2, res) -> None:
    #     resultado = num1 * num2
    #     # print(resultado)
    #     self.assertEqual(resultado, res)


    def test(self) -> None:
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()