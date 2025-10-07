from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import unittest

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/'
class BaseFirefox(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Firefox(options=options)        


    def setUp(self) -> None:
        self.driver.get(URL_PAGE)
        print("paso por aqui")


    def tutest1(self) -> None:
        pass

    def tutest2(self) -> None:
        pass    
    
    def tutest3(self) -> None:
        pass


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()