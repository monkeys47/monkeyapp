import os

def unificar_funcionales(carpeta_funcionales, archivo_salida):
    # Conjunto para evitar duplicados
    correos_unificados = set()

    # Leer todos los archivos en la carpeta funcionales
    for archivo in os.listdir(carpeta_funcionales):
        archivo_path = os.path.join(carpeta_funcionales, archivo)
        if os.path.isfile(archivo_path):
            with open(archivo_path, "r") as f:
                for linea in f:
                    correo = linea.strip()
                    if correo:  # Evitar líneas vacías
                        correos_unificados.add(correo)

    # Escribir todos los correos unificados en el archivo de salida
    with open(archivo_salida, "w") as archivo_salida_f:
        for correo in sorted(correos_unificados):
            archivo_salida_f.write(correo + "\n")

    print(f"Todos los correos funcionales se han unificado en: {archivo_salida}")

# Ejecutar la función
if __name__ == "__main__":
    carpeta_funcionales = "funcionales"
    archivo_salida = "todos_funcionales.txt"
    unificar_funcionales(carpeta_funcionales, archivo_salida)