from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import unittest

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/async.html'
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()        
        cls.driver.get(URL_PAGE)
        cls.driver.find_element(By.CSS_SELECTOR, 'body > div > div > main > div > div > div > div > div > div > button').click()
        cls.wait = WebDriverWait(cls.driver, 6)
        # cls.wait = WebDriverWait(cls.driver, 6, poll_frequency=0.2, ignored_exceptions=[NoSuchElementException])

    def setUp(self) -> None:
        pass


    def testWaitImplicito(self) -> None:
        print("Esperando implícitamente 6 segundos...")
        self.driver.implicitly_wait(6)
        button = self.driver.find_element(By.ID, 'btn')
        print("Botón encontrado:", button)
        self.assertIsNotNone(button)

    def testWaitExplicito(self) -> None:
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#btn')))
        button = self.driver.find_element(By.CSS_SELECTOR, '#btn')
        self.assertIsNotNone(button)        

    def testFluentWait(self) -> None:
        self.wait.until(lambda s: s.find_element(By.CSS_SELECTOR, '#btn').is_displayed())
        button = self.driver.find_element(By.CSS_SELECTOR, '#btn')
        self.assertIsNotNone(button)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()