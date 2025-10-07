from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest

URL_PAGE = 'https://es.wikipedia.org/wiki/Wikipedia:Portada'
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)        


    def setUp(self) -> None:
        self.driver.get(URL_PAGE)


    def testByXpathRelative(self) -> None:
        listElements = self.driver.find_elements(By.XPATH,'//*[@id="p-navigation"]/div[2]/ul/li')
        for element in listElements:
            title = element.find_element(By.TAG_NAME, 'a').get_attribute('title')
            print(title)

            # print(element.findElement(By.TAG_NAME, 'a').title)


    def testByXpathAbsolute(self) -> None:
        listElements = self.driver.find_elements(By.XPATH,'/html/body/div[1]/header/div[1]/nav/div/div/div/div/div[2]/div[2]/ul/li')
        for element in listElements:
            title = element.find_element(By.TAG_NAME, 'a').get_attribute('title')
            print(title)



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()