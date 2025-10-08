from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest

URL_PAGE = 'https://es.wikipedia.org/w/index.php?title=Especial:Buscar&search=&fulltext=Buscar&profile=advanced'

class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)

    def setUp(self) -> None:
        self.driver.get(URL_PAGE)

    def testCheckboxCount(self) -> None:
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        self.assertEqual(
            37,
            len(checkboxes),
            f"Se esperaban 37 checkboxes, pero se encontraron {len(checkboxes)}"
        )

    def testSearchInputExists(self) -> None:
        # Campo de texto principal en búsqueda avanzada
        search_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="search"]')
        self.assertIsNotNone(search_input, "El campo de búsqueda no fue encontrado")

    def testSearchButtonExists(self) -> None:
        # Botón de búsqueda principal dentro del formulario de búsqueda avanzada
        search_button = self.driver.find_element(By.CSS_SELECTOR, '#powersearch button[type="submit"]')
        self.assertIsNotNone(search_button, "El botón de búsqueda no fue encontrado")

    def testSearchInputAndButtonExist(self) -> None:
        search_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="search"]')
        search_button = self.driver.find_element(By.CSS_SELECTOR, '#powersearch button[type="submit"]')
        self.assertIsNotNone(search_input, "Falta el campo de búsqueda")
        self.assertIsNotNone(search_button, "Falta el botón de búsqueda")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
