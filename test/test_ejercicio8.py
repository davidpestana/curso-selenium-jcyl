from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys  

import unittest


URL_PAGE = 'https://es.wikipedia.org/wiki/Wikipedia:Portada'

class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)

    def setUp(self) -> None:
        self.driver.get(URL_PAGE)

    def testInputExists(self) -> None:
        search_input = self.driver.find_element(By.NAME, "search")
        self.assertIsNotNone(search_input)

    def testPlaceholderIsCorrect(self) -> None:
        search_input = self.driver.find_element(By.NAME, "search")
        placeholder = search_input.get_attribute("placeholder")
        self.assertEqual(
            placeholder,
            "Buscar en Wikipedia",
            f"El placeholder debería ser 'Buscar en Wikipedia', pero fue '{placeholder}'"
        )

    def testFontSizeIsCorrect(self) -> None:
        search_input = self.driver.find_element(By.NAME, "search")
        font_size = search_input.value_of_css_property("font-size")
        print("Font size:", font_size)
        self.assertEqual(
            font_size,
            "13.3333px",
            f"El tamaño de fuente debería ser '13.3333px', pero fue '{font_size}'"
        )

    def testSearchForSelenium(self) -> None:
        search_input = self.driver.find_element(By.NAME, "search")
        search_input.clear()
        search_input.send_keys("Selenium")
        
        # Simula un usuario pulsando Enter
        search_input.send_keys("Selenium", keys.ENTER)

        # Envia directamente el formulario que contiene el input  (solo funciona si el input está dentro de un form)
        search_input.send_keys("Selenium")
        search_input.submit()

        # Esperamos a que cargue nueva URL
        self.driver.implicitly_wait(3)

        # Comprobamos que la URL contiene "/Selenium"
        current_url = self.driver.current_url
        self.assertIn(
            "Selenium", current_url,
            f"La URL actual debería contener 'Selenium', pero es '{current_url}'"
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
