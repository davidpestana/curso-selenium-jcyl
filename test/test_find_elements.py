from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/'
class ColeccionEncontrarElementos(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)        
        cls.driver.get(URL_PAGE)
        cls.driver.find_element(By.CSS_SELECTOR, 'body > div > div > main > div > div > div > div > div > div > button').click()


    def setUp(self) -> None:
        pass


    def testFindById(self) -> None:
        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')
        # username.text = 'mi_usuario'

    def testFindByName(self) -> None:
        username = self.driver.find_element(By.NAME, 'user')
        password = self.driver.find_element(By.NAME, 'pass')

    def testFindByClass(self) -> None:
        username = self.driver.find_element(By.CLASS_NAME, 'login-u')
        password = self.driver.find_element(By.CLASS_NAME, 'login-p')

    def testFindByTags(self) -> None:
        labels = self.driver.find_elements(By.TAG_NAME, 'label')
        for label in labels:
            pass
            # print(label.text)
    def testFindByLinkText(self) -> None:
        link = self.driver.find_element(By.LINK_TEXT, 'Logout')
        # print(link.get_attribute('href'))

    def testFindByPartialLinkText(self) -> None:
        link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'notificaciones sin leer')
        # print(link.get_attribute('href'))


    def testFindByXpath(self) -> None:
        submit_button = self.driver.find_element(By.XPATH, '/html/body/form/button')
        # print(submit_button.get_attribute('type'))
        # print(submit_button.text)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()