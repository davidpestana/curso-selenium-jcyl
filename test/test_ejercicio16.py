from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack
import unittest

URL_PAGE = 'https://demoqa.com/automation-practice-form'

@ddt
class BaseChrome(unittest.TestCase):

    data_set = [
        {'first_name': 'Juan', 'last_name': 'Pérez', 'email': 'juan@example.com', 'phone': '1234567890', 'address': 'Calle Falsa 123'},
        {'first_name': 'María', 'last_name': 'Gómez', 'email': 'maria@example.com', 'phone': '0987654321', 'address': 'Avenida Siempre Viva 742'},
        {'first_name': 'Jhon&Smith', 'last_name': 'Gómez', 'email': 'maria@example.com', 'phone': '0987654321', 'address': 'Avenida Siempre Viva 742'}
    ]

    

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)        


    def setUp(self) -> None:
        self.driver.get(URL_PAGE)

    @data(*data_set)
    @unpack
    def test_fill_first_name(self, **kwargs) -> None:
        first_name=kwargs['first_name']
        first_name_input = self.driver.find_element(By.ID, 'firstName')
        first_name_input.clear()
        first_name_input.send_keys(first_name)
        self.assertEqual(first_name_input.get_attribute('value'), first_name, f"El nombre ingresado debería ser {first_name}")

    @data(*data_set)
    def test_fill_lastName(self, data) -> None:
        last_name_input = self.driver.find_element(By.ID, 'lastName')
        last_name_input.clear()
        last_name_input.send_keys(data['last_name'])
        self.assertEqual(last_name_input.get_attribute('value'), data['last_name'], f"El apellido ingresado debería ser {data['last_name']}")


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()