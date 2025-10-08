from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/dbl-click.html'
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)        
        cls.driver.get(URL_PAGE)
        cls.driver.find_element(By.CSS_SELECTOR, 'body > div > div > main > div > div > div > div > div > div > button').click()



    def setUp(self) -> None:
        pass


    def testDobleClick(self) -> None:
        box = self.driver.find_element(By.ID, 'caja-doble-click')

        self.assertEqual(box.value_of_css_property('background-color'), "rgba(0, 0, 255, 1)", " El color inicial no es azul")
        
        ActionChains(self.driver).double_click(box).perform
        
        self.assertEqual(box.value_of_css_property('background-color'), "rgba(255, 255, 0, 1)", " El color despues del doble click no es amarillo")
            
        title = self.driver.execute_script('return dblFunction(document.getElementById("caja-doble-click"))')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()