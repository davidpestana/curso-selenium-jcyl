from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest

URL_PAGE = 'http://www.w3schools.com/html/html_tables.asp'
class BaseChrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=options)        


    def setUp(self) -> None:
        self.driver.get(URL_PAGE)
        self.table = self.driver.find_element(By.XPATH,"(//table)[1]")


    def testTableExist(self) -> None:
        self.assertIsNotNone(self.table)
        pass
    
    def testNumberOfRows(self) -> None:
        rows = self.table.find_elements(By.TAG_NAME,"tr")
        self.assertEqual(7,len(rows), "la tabla deberia tener 7 filas")
        
    def testLastRowHasNumberOfCols(self) -> None:
        row = self.table.find_element(By.XPATH,"last(tr)")
        cols = row.find_elements(By.TAG_NAME,"td")
        self.assertEqual(3,len(cols), "la ultima fila deberia tener 3 columnas")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()