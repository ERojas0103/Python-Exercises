import tkinter as tk


def obtener_codigo_estudiante():
    codigo = codigo_entry.get()
    # Aquí puedes agregar el código para procesar el dato ingresado
    # Puedes imprimirlo en la consola o realizar alguna otra acción

    print("El código de estudiante ingresado es:", codigo)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("REGISTRO DE PRÉSTAMOS DE IMPLEMENTOS UFPS")

# Ajustar el tamaño de la ventana
ventana.geometry("400x300")

# Crear el título de bienvenida
titulo_label = tk.Label(
    ventana, text="Bienvenido al programa\nREGISTRO DE PRÉSTAMOS DE IMPLEMENTOS UFPS", font=("Arial", 18))
titulo_label.pack(pady=20)

# Crear la etiqueta y la casilla para el código de estudiante
codigo_label = tk.Label(
    ventana, text="Código de estudiante:", font=("Arial", 14))
codigo_label.pack()

codigo_entry = tk.Entry(ventana, font=("Arial", 14))
codigo_entry.pack(pady=10)

# Crear el botón para obtener el código de estudiante
obtener_codigo_button = tk.Button(ventana, text="Obtener código", font=(
    "Arial", 14), command=obtener_codigo_estudiante)
obtener_codigo_button.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
