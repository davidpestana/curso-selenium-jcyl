/**
 * E2E test con Selenium WebDriver integrado con Jest.
 * Requiere tener corriendo la app Angular (ng serve o servidor HTTP)
 * y Chrome disponible localmente o en un Selenium Grid.
 */

import { Builder, By, until, WebDriver } from 'selenium-webdriver';
import chrome from 'selenium-webdriver/chrome';

let driver: WebDriver;

describe('AppComponent - Selenium E2E', () => {
//   const APP_URL = 'http://localhost:4200'; // Ajusta según tu entorno

  beforeAll(async () => {
    const options = new chrome.Options()
      .addArguments('--no-sandbox')
      .addArguments('--disable-dev-shm-usage')
      .addArguments('--headless=new');

    driver = await new Builder()
      .forBrowser('chrome')
      .setChromeOptions(options)
      // Para Selenium Grid:
      // .usingServer('http://localhost:4444/wd/hub')
      .build();
  }, 30000);

  afterAll(async () => {
    if (driver) {
      try {
        await driver.quit();
      } catch {
        // el framework maneja errores residuales de cierre
      }
    }
  });

  test('debería multiplicar correctamente dos números', async () => {
    await driver.get(APP_URL);

    const num1 = await driver.wait(until.elementLocated(By.id('num1')), 5000);
    const num2 = await driver.findElement(By.id('num2'));
    const boton = await driver.findElement(By.id('btn'));

    await num1.sendKeys('7');
    await num2.sendKeys('6');
    await boton.click();

    const resultado = await driver.wait(until.elementLocated(By.id('resultado')), 5000);
    const texto = await resultado.getText();

    expect(texto).toContain('42');
  }, 20000);
});
