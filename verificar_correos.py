import os
import time

# Función para dividir los correos por dominio
def dividir_correos_por_dominio(archivo_entrada, carpeta_salida):
    with open(archivo_entrada, "r") as archivo:
        lineas = archivo.readlines()

    dominios = {}
    for linea in lineas:
        correo = linea.strip().split(":")[0]
        dominio = correo.split("@")[-1]
        if dominio not in dominios:
            dominios[dominio] = []
        dominios[dominio].append(linea)

    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    for dominio, correos in dominios.items():
        nombre_archivo = os.path.join(carpeta_salida, f"{dominio.replace('.', '_')}_pruebas.txt")
        with open(nombre_archivo, "w") as archivo_salida:
            archivo_salida.writelines(correos)

# Función para verificar correos por dominio
def verificar_correos_por_dominio(carpeta_entrada, carpeta_funcionales):
    archivos = [f for f in os.listdir(carpeta_entrada) if f.endswith("_pruebas.txt")]

    if not os.path.exists(carpeta_funcionales):
        os.makedirs(carpeta_funcionales)

    for archivo in archivos:
        dominio = archivo.replace("pruebas.txt", "").replace("", ".")
        archivo_entrada = os.path.join(carpeta_entrada, archivo)
        archivo_funcionales = os.path.join(carpeta_funcionales, f"{dominio}_funcionales.txt")

        print(f"Procesando: {archivo}")
        with open(archivo_entrada, "r") as archivo_correos, open(archivo_funcionales, "w") as archivo_func:
            for linea in archivo_correos:
                try:
                    correo, contrasena = linea.strip().split(":")
                    # Aquí iría la lógica de conexión específica según el dominio
                    time.sleep(0.1)  # Simula la conexión
                    print(f"Correo funcional: {correo}")
                    archivo_func.write(f"{correo}:{contrasena}\n")
                except Exception as e:
                    print(f"Error con la cuenta {correo}: {e}")

    print(f"Todos los correos funcionales se guardaron en la carpeta: {carpeta_funcionales}")

# Función principal
def main():
    archivo_entrada = "correos_pruebas.txt"
    carpeta_salida = "dominios"
    carpeta_funcionales = "funcionales"

    print("Dividiendo correos por dominio...")
    dividir_correos_por_dominio(archivo_entrada, carpeta_salida)

    print("Verificando correos por dominio...")
    verificar_correos_por_dominio(carpeta_salida, carpeta_funcionales)

    print("Proceso completado.")

# Punto de entrada al programa
if __name__ == "__main__":
    main()