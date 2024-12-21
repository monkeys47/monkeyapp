import tkinter as tk
from tkinter import filedialog, messagebox
import threading

# Función para seleccionar un archivo
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo de correos", filetypes=(("Archivos de texto", ".txt"), ("Todos los archivos", ".*")))
    if archivo:
        ruta_archivo.set(archivo)

# Función para iniciar el proceso
def iniciar_proceso():
    if not ruta_archivo.get():
        messagebox.showerror("Error", "Por favor, selecciona un archivo antes de continuar.")
        return

    # Crear un hilo para ejecutar el proceso
    threading.Thread(target=procesar_archivo).start()

# Simular el procesamiento (esta función será reemplazada con el proceso real)
def procesar_archivo():
    boton_iniciar.config(state=tk.DISABLED)
    etiqueta_progreso.config(text="Procesando...")
    ventana.update()

    # Aquí se incluirá la lógica de procesamiento real
    # Simulando un proceso de 5 segundos
    import time
    time.sleep(5)

    etiqueta_progreso.config(text="Proceso completado.")
    messagebox.showinfo("Éxito", "El proceso se ha completado correctamente.")
    boton_iniciar.config(state=tk.NORMAL)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificador de Correos")
ventana.geometry("500x300")

ruta_archivo = tk.StringVar()

# Elementos de la interfaz
etiqueta_archivo = tk.Label(ventana, text="Archivo de correos:")
etiqueta_archivo.pack(pady=10)

entrada_archivo = tk.Entry(ventana, textvariable=ruta_archivo, width=50, state="readonly")
entrada_archivo.pack(pady=5)

boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack(pady=5)

boton_iniciar = tk.Button(ventana, text="Iniciar proceso", command=iniciar_proceso)
boton_iniciar.pack(pady=20)

etiqueta_progreso = tk.Label(ventana, text="")
etiqueta_progreso.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()