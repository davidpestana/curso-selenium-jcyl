from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest


URL_PAGE = 'https://demoqa.com/droppable'
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # options = Options()
        # options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome()        
        cls.driver.get(URL_PAGE)


    def setUp(self) -> None:
        pass


    def testDragAndDrop(self) -> None:
        source = self.driver.find_element(By.ID, 'draggable')
        target = self.driver.find_element(By.ID, 'droppable')

        
        self.driver.save_screenshot("screenshots/before_screenshot.png") 

        ActionChains(self.driver).drag_and_drop(source, target).perform()
        self.assertEqual("Dropped!", target.text)          

        self.driver.save_screenshot("screenshots/after_screenshot.png") 

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()