import os

# Función para agrupar los correos por dominio
def agrupar_correos_por_dominio(archivo_entrada, archivo_salida):
    # Diccionario para almacenar los correos agrupados por dominio
    dominios = {}

    with open(archivo_entrada, "r") as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            correo = linea.strip().split(":")[0]
            dominio = correo.split("@")[-1]
            if dominio not in dominios:
                dominios[dominio] = []
            dominios[dominio].append(linea.strip())

    # Escribir los correos agrupados en el archivo de salida
    with open(archivo_salida, "w") as archivo_salida:
        for dominio, correos in sorted(dominios.items()):
            archivo_salida.write(f"===== {dominio.upper()} =====\n")
            for correo in correos:
                archivo_salida.write(f"{correo}\n")
            archivo_salida.write("\n")

    print(f"Archivo agrupado por dominios creado: {archivo_salida.name}")

# Función principal
def main():
    archivo_entrada = "funcionales/todos_funcionales.txt"
    archivo_salida = "funcionales/agrupados_por_dominio.txt"

    print("Agrupando correos por dominio...")
    agrupar_correos_por_dominio(archivo_entrada, archivo_salida)

    print("Proceso completado.")

# Punto de entrada al programa
if __name__ == "__main__":
    main()