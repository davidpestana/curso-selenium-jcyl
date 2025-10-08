from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/'
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)        


    def setUp(self) -> None:
        self.driver.get(URL_PAGE)

        self.selectorCoches = self.driver.find_element(By.NAME, "cars")
        self.coches = Select(self.selectorCoches)


    def testCochesEsMultiple(self) -> None:
        self.coches.assertFalse(self.coches.is_multiple)

        
    def testCochesNumeroOpciones(self) -> None:
        self.coches.assertEqual(len(self.coches.options), 4)


    def testSeVeLaOcionSeleccionadaAlSeleccionar(self) -> None:
        self.coches.select_by_value("audi")
        self.assertEqual(self.coches.first_selected_option.text, "Audi")
        self.coches.select_by_index(0)
        self.assertEqual(self.first_selected_option.text, "BMW")

    def testValueAlSeleccionar(self) -> None:
        self.coches.select_by_visible_text("Tesla")
        value = self.selectorCoches.get_attribute("value")
        self.assertEqual(value, "tesla")


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()