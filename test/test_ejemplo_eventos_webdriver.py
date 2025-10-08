import unittest
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.common.action_chains import ActionChains
from listeners.trace_llisteners import TraceListener

class ColeccionSeleniumAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.event_driver = EventFiringWebDriver(cls.driver, TraceListener())

    def setUp(self) -> None:
        self.event_driver.get("https://todomvc.com/examples/javascript-es6/dist/")

    def testEventos(self) -> None:
        """Ejemplo de uso de eventos y listener."""
        driver = self.event_driver

        # Añadir tareas
        input_box = driver.find_element(By.CSS_SELECTOR, "input.new-todo")
        input_box.send_keys("Hacer la compra" + Keys.ENTER)
        input_box.send_keys("Ir al gimnasio" + Keys.ENTER)

        # Pausa breve para que las tareas aparezcan
        time.sleep(1)

        # Provocar excepción intencionada (el listener tomará screenshot)
        driver.find_element(By.ID, "no-existe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.event_driver.quit()
