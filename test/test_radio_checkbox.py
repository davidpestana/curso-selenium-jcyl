from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest

URL_PAGE = 'https://psychic-space-giggle-6jv4rwv4crqwj-8080.app.github.dev/radio-checkbox.html'
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


    def testRadioButtons(self) -> None:
        working = self.driver.find_element(By.XPATH, "//input[@type='radio' and @name='working' and @value='Yes']")

        if not working.is_selected():
            working.click()
        self.assertTrue(working.is_selected())

    def testCheckboxes(self) -> None:
        cine = self.driver.find_element(By.XPATH, "//input[@id='cine']")
        if not cine.is_selected():
            cine.click()
        self.assertTrue(cine.is_selected())



    def testCheckboxes(self) -> None:
        hobbies = self.driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='hobbies']")

        self.assertEqual(hobbies.value, ['cine', 'musica', 'deporte'], "Los valores de los checkboxes no son correctos")

        for hobby in hobbies:
            if not hobby.is_selected():
                hobby.click()
            self.assertTrue(hobby.is_selected())
        

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()