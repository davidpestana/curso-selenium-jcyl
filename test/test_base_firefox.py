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


    def test1(self) -> None:
        print(self.driver.title)
        

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()