from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Ruta al archivo ChromeDriver descargado
driver_path = "chromedriver.exe"
service = Service(driver_path)

# Credenciales para probar (reemplázalas con un correo y contraseña reales)
email = "eddyulerio05@gmail.com"
password = "07052004er"

# Inicia el navegador Chrome
driver = webdriver.Chrome(service=service)

try:
    # Abre la página de inicio de sesión de Gmail
    driver.get("https://accounts.google.com/")

    # Introducir el correo electrónico
    email_input = driver.find_element(By.ID, "identifierId")
    email_input.send_keys(email)  # Cambia por un correo válido
    email_input.send_keys(Keys.RETURN)

    time.sleep(2)  # Espera a que cargue la página de contraseña

    # Introducir la contraseña
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)  # Cambia por una contraseña válida
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)  # Espera para ver si el login es exitoso

    # Verificar si el inicio de sesión fue exitoso
    if "myaccount.google.com" in driver.current_url:
        print("Inicio de sesión exitoso.")
    else:
        print("Inicio de sesión fallido.")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Cierra el navegador
    driver.quit()