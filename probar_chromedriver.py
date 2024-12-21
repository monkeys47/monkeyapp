from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Ruta al archivo ChromeDriver descargado
driver_path = "chromedriver.exe"  # Ruta del chromedriver en la misma carpeta

# Crear el servicio de ChromeDriver
service = Service(driver_path)

# Inicia el navegador Chrome
driver = webdriver.Chrome(service=service)

# Abre Google
driver.get("https://www.google.com")
print("¡ChromeDriver está funcionando correctamente!")

time.sleep(5)  # Espera para observar el navegador

# Cierra el navegador
driver.quit()