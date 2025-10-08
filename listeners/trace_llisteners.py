import os
import datetime
from selenium.webdriver.support.events import AbstractEventListener

class TraceListener(AbstractEventListener):
    """Listener para registrar eventos y capturar screenshots en caso de error."""

    def on_exception(self, exception, driver):
        """Se ejecuta automáticamente cuando ocurre una excepción en Selenium."""
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshots/{timestamp}_exception.png"
        driver.save_screenshot(filename)
        print(f"⚠️ Excepción detectada. Screenshot guardado en: {filename}")

    def before_click(self, element, driver):
        print("🖱️ Before click")

    def before_change_value_of(self, element, driver):
        print("✏️ Before change value")

    def before_find(self, by, value, driver):
        print(f"🔍 Before find: {by} = {value}")

    def before_navigate_to(self, url, driver):
        print(f"🌍 Before navigate to: {url}")

    def after_navigate_to(self, url, driver):
        print(f"✅ After navigate to: {url}")