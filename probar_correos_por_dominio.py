import yagmail
import glob

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

# Procesar todos los archivos separados por dominio
archivos = glob.glob("*_pruebas.txt")  # Busca todos los archivos *_pruebas.txt

for archivo in archivos:
    print(f"Procesando: {archivo}")
    
    with open(archivo, "r") as archivo_dominio:
        lineas = archivo_dominio.readlines()

    # Archivo para guardar solo los correos funcionales
    nombre_funcionales = archivo.replace("_pruebas", "_funcionales")
    with open(nombre_funcionales, "w") as funcionales:
        for linea in lineas:
            try:
                # Separar el correo y la contraseña
                email, password = linea.strip().split(":")
                
                # Configurar el servidor SMTP según el proveedor
                servidor = configurar_servidor(email, password)
                
                # Probar la conexión (sin enviar un correo)
                servidor.login()
                print(f"Correo funcional: {email}")
                
                # Guardar el correo funcional en el archivo
                funcionales.write(f"{email}:{password}\n")
            
            except Exception as e:
                print(f"Error con la cuenta {email}: {e}")
    
    print(f"Archivo procesado: {nombre_funcionales}")

print("Proceso completado.")