from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from utils.getDriver import getDriver

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/'
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = getDriver()
  
    def setUp(self) -> None:
        self.driver.get(URL_PAGE)

    def test(self) -> None:
        self.driver.find_element(By.TAG_NAME, 'h1')
        pass

    


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()