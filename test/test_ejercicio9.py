from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest

URL_PAGE = "https://es.wikipedia.org/wiki/Especial:Contribuciones"

class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)

    def setUp(self) -> None:
        self.driver.get(URL_PAGE)

    def testSelectIsNotMultiple(self) -> None:
        select_element = self.driver.find_element(By.NAME, "namespace")
        selectDriver = Select(select_element)
        self.assertFalse(selectDriver.is_multiple(), "El select no debería ser múltiple")

    def testSelectHasCorrectNumberOfOptions(self) -> None:
        selectDriver = Select(self.driver.find_element(By.NAME, "namespace"))
        options = selectDriver.options
        self.assertEqual(
            len(options),
            22,  # <-- número actual en 2025 (puede cambiar)
            f"Se esperaban 22 opciones, pero se encontraron {len(options)}"
        )

    def testSelectAndCheckUsuario(self) -> None:
        select = Select(self.driver.find_element(By.NAME, "namespace"))
        select.select_by_visible_text("Usuario")
        selected = select.first_selected_option.text
        self.assertEqual(selected, "Usuario")

    def testSelectAndCheckMediaWiki(self) -> None:
        select = Select(self.driver.find_element(By.NAME, "namespace"))
        select.select_by_visible_text("MediaWiki")
        selected = select.first_selected_option.text
        self.assertEqual(selected, "MediaWiki")

    def testSelectAndCheckAyuda(self) -> None:
        select = Select(self.driver.find_element(By.NAME, "namespace"))
        select.select_by_visible_text("Ayuda")
        selected = select.first_selected_option.text
        self.assertEqual(selected, "Ayuda")

    def testSelectOptionsAreExpected(self) -> None:
        select = Select(self.driver.find_element(By.NAME, "namespace"))
        option_texts = [opt.text for opt in select.options]

        expected_options = [
            "(todas)", "Artículo", "Usuario", "Wikipedia", "Archivo", "MediaWiki",
            "Plantilla", "Ayuda", "Categoría", "Recurso educativo", "Wikiversidad",
            "Módulo", "Tema", "Accesorio", "Gadget definition", "Especial", "Media",
            "Resumen", "Propiedad", "Elemento", "Consulta SPARQL", "Lexema"
        ]

        self.assertEqual(option_texts, expected_options, "Las opciones del select no coinciden")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
