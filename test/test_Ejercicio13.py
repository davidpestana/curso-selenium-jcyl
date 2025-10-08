import unittest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL_PAGE = "http://es.wikipedia.org/w/index.php?title=Especial:Buscar&search=&fulltext=Buscar&profile=advanced"

class TestCheckboxWikipedia(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(URL_PAGE)

        # Crear carpeta de capturas si no existe
        os.makedirs("screenshots", exist_ok=True)

    def take_screenshot(self, name):
        """Guarda una captura con timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(path)
        print(f"📸 Screenshot guardado: {path}")

    def test_checkboxes(self) -> None:
        driver = self.driver

        # 1️⃣ Obtener el checkbox principal y comprobar que está seleccionado
        main_checkbox = driver.find_element(By.ID, "mw-search-toggle-all")
        self.assertTrue(main_checkbox.is_selected(), "❌ El checkbox principal no está seleccionado")
        print("✅ El checkbox principal está seleccionado.")

        # 2️⃣ Obtener todos los checkboxes
        all_checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        print(f"✅ Se encontraron {len(all_checkboxes)} checkboxes en la página.")

        # 3️⃣ Capturar pantalla inicial
        self.take_screenshot("checkboxes_inicial")

        # 4️⃣ Seleccionar todos los checkboxes que no lo estén
        for checkbox in all_checkboxes:
            if not checkbox.is_selected():
                driver.execute_script("arguments[0].click();", checkbox)

        # 5️⃣ Capturar pantalla final
        self.take_screenshot("checkboxes_final")

        # Validar que todos quedaron seleccionados
        for checkbox in all_checkboxes:
            self.assertTrue(checkbox.is_selected(), "❌ Hay checkboxes sin seleccionar")

        print("✅ Todos los checkboxes están seleccionados.")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
