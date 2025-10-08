## 🧩 Uso de **Xvfb** en pipelines Selenium

Cuando ejecutamos pruebas Selenium en **pipelines CI/CD (como GitHub Actions, GitLab CI, Jenkins o contenedores Docker)**, no hay entorno gráfico disponible.
Chrome y otros navegadores necesitan una “pantalla” para procesar eventos de ratón y teclado, incluso cuando usamos `--headless`.

Ahí es donde entra en juego **Xvfb**.

---

### 🧠 ¿Qué es Xvfb?

**Xvfb (X Virtual Framebuffer)** es un servidor gráfico *virtual* para sistemas Linux.
Emula una pantalla (framebuffer) en memoria, permitiendo que las aplicaciones que requieren entorno gráfico —como **Google Chrome**, **Firefox**, o **Selenium**— se ejecuten como si tuvieran una interfaz visual, **aunque el sistema no tenga ninguna**.

En otras palabras:

> Xvfb crea un “display” falso donde el navegador puede renderizar y mover el ratón, aunque no haya una ventana real.

---

### 🚀 ¿Por qué usarlo en pipelines?

Incluso con `--headless`, hay acciones en Selenium que **no funcionan correctamente**:

* `ActionChains.drag_and_drop()`
* `ActionChains.double_click()`
* `ActionChains.move_to_element()`
* `ActionChains.context_click()`

Esto ocurre porque el modo headless **no procesa todos los eventos físicos del ratón**.
Si ejecutamos las pruebas dentro de **Xvfb**, Chrome cree que hay un entorno gráfico real, y esas acciones **sí se ejecutan correctamente**.

---

### ⚙️ Cómo usarlo

En Linux, basta con ejecutar tus pruebas con el comando:

```bash
xvfb-run -a python -m unittest discover -s test/
```

Explicación:

* `xvfb-run` → inicia el servidor X virtual.
* `-a` → asigna automáticamente un número de display disponible (por ejemplo `:99`).
* Lo que sigue (`python -m unittest ...`) se ejecuta dentro de ese entorno gráfico simulado.

---

### 📦 Ejemplo en GitHub Actions

```yaml
name: Selenium Tests

on: [push, pull_request]

jobs:
  selenium:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y xvfb
          pip install selenium

      - name: Run Selenium tests inside Xvfb
        run: |
          xvfb-run -a python -m unittest discover -s test/
```

---

### ✅ Ventajas de usar Xvfb

| Ventaja                               | Descripción                                                                |
| ------------------------------------- | -------------------------------------------------------------------------- |
| 🖥️ Emula un entorno gráfico completo | Chrome puede comportarse igual que en local                                |
| 🧩 Compatible con `ActionChains`      | Permite usar `drag_and_drop`, `double_click`, etc. sin modificar el código |
| ⚙️ Fácil de integrar                  | Solo requiere añadir `xvfb-run` antes del comando de test                  |
| 🪶 Ligero                             | No consume GPU ni memoria significativa                                    |
| 🔄 Transparente                       | Tu código Selenium no necesita ningún cambio                               |

---

### ⚠️ Cuándo **no** es necesario

* Si tu código **ya usa `--headless`** y **no dependes de acciones complejas** (solo clicks, inputs, navegación, etc.).
* Si ejecutas en un **Codespace** sin privilegios `sudo`, ya que no podrás instalar `xvfb`.

En esos casos, sigue siendo más práctico usar la técnica de **simulación con JavaScript (`execute_script()`)**.

---

### 🧩 Conclusión

* `Xvfb` permite que **Chrome o Firefox crean que tienen una pantalla real**, incluso en servidores CI.
* Es la forma **más sencilla y estable** de ejecutar tests Selenium **con `ActionChains` reales** dentro de pipelines.
* Si no puedes instalarlo, la alternativa es **inyectar eventos con JavaScript**.