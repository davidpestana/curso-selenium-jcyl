# curso-selenium-jcyl



## ✅ Instalar entorno Selenium + Chrome en Ubuntu (Codespace)

---

### 🧩 Paso 1 – Instalar Google Chrome (sin snap)

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
```

✅ Verifica que Chrome está disponible:

```bash
google-chrome --version
# → Google Chrome 117.x.x.x (o similar)
```

---

### 🐍 Paso 2 – Crear y activar entorno virtual

```bash
python3 -m venv env-curso-selenium
source env-curso-selenium/bin/activate
```

---

### 📦 Paso 3 – Instalar dependencias

```bash
pip install selenium webdriver-manager
```

---

## ✅ Listo

Ya puedes ejecutar tu script Python con Selenium + Chrome en modo headless.

---

### 📄 Ejemplo de `requirements.txt` (opcional)

```txt
selenium==4.16.0
webdriver-manager==4.0.1
```

Instalación en futuros entornos:

```bash
pip install -r requirements.txt
```