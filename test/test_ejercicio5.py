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
        row = self.table.find_element(By.XPATH,".//tr[last()]")
        cols = row.find_elements(By.TAG_NAME,"td")
        self.assertEqual(3,len(cols), "la ultima fila deberia tener 3 columnas")

    def testHasTwoRowsAfterFifth(self) -> None:
        rows = self.table.find_elements(By.XPATH, ".//tr")
        total = len(rows)
        self.assertGreaterEqual(total, 7, "Debería haber al menos dos filas después de la quinta")


    def testHasTwoRowsAfterFifth(self) -> None:
        # Find all sibling rows that come after the 5th
        following_rows = self.table.find_elements(By.XPATH, ".//tr[5]/following-sibling::tr")
        # Assert that there are exactly 2 rows after the 5th
        self.assertEqual(
            2,
            len(following_rows),
            f"Debería haber exactamente 2 filas después de la quinta, pero se encontraron {len(following_rows)}"
        )


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()