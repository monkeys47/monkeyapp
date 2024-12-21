# Leer el archivo original con los correos
with open("correos_pruebas.txt", "r") as archivo:
    lineas = archivo.readlines()

# Diccionario para almacenar los correos por dominio
dominios = {}

# Separar los correos por dominio
for linea in lineas:
    email, password = linea.strip().split(":")
    dominio = email.split("@")[-1]
    
    # Crear una lista para cada dominio
    if dominio not in dominios:
        dominios[dominio] = []
    dominios[dominio].append(f"{email}:{password}\n")

# Guardar los correos en archivos separados por dominio
for dominio, correos in dominios.items():
    nombre_archivo = f"{dominio}_pruebas.txt"
    with open(nombre_archivo, "w") as archivo_dominio:
        archivo_dominio.writelines(correos)

print("Los correos han sido agrupados por dominio en un único archivo.")