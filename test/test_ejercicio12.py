import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class TestCrearCuentaWikipedia(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://es.wikipedia.org/w/index.php?title=Especial:Crear_una_cuenta")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 1️⃣ Comprobar que un elemento no está presente y mostrar mensaje
    def test_element_not_present_message(self):
        driver = self.driver
        try:
            driver.find_element(By.ID, "elemento_inexistente")
            print("❌ El elemento inesperado está presente.")
        except NoSuchElementException:
            print("✅ El elemento no está presente (correcto).")

    # 2️⃣ Comprobar que un elemento no está presente y mostrar excepción personalizada
    def test_element_not_present_custom_exception(self):
        driver = self.driver
        try:
            driver.find_element(By.NAME, "campo_que_no_existe")
            raise Exception("❌ Error: el elemento debería no existir, pero está presente.")
        except NoSuchElementException:
            print("✅ El elemento no existe, como esperábamos.")

    # 3️⃣ Comprobar que un elemento está presente y visible
    def test_element_present_and_displayed(self):
        driver = self.driver
        try:
            username_input = driver.find_element(By.ID, "wpName2")
            self.assertTrue(username_input.is_displayed(), "El campo de usuario no está visible.")
            print("✅ El campo de nombre de usuario está presente y visible.")
        except NoSuchElementException:
            self.fail("❌ No se encontró el campo de nombre de usuario.")

if __name__ == "__main__":
    unittest.main()
