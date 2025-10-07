import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Tests(unittest.TestCase):


    @classmethod
    def setUpClass(self) -> None:
        options = Options()
        options.add_argument("--headless=new")

        # service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=options)

    def setUp(self) -> None:
        self.driver.get("https://www.google.com")
        

    def test1(self) -> None:
        self.assertEqual(1, 1, "no son iguales")
        pass

    def test2(self) -> None:
        # Código del test 2
        pass

    def tearDown(self) -> None:
        # Se ejecuta una vez después de cada prueba
        pass

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()