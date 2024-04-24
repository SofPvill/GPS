import tkinter as tk
from tkinter import messagebox
import subprocess

def validar_ingreso():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    # Validar usuario y contraseña (aquí podrías agregar lógica de validación)
    if usuario == "admin" and contraseña == "123":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso!")
        ejecutar_archivo()
        root.destroy()  # Cerrar la ventana de inicio de sesión
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def ejecutar_archivo():
    try:
        subprocess.run(["python", "pruebaModelo.py"])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar el archivo: {e}")

# Crear la ventana de inicio de sesión
root = tk.Tk()
root.title("Inicio de Sesión")

# Configurar tamaño de la ventana de inicio de sesión
ancho_ventana = 400
alto_ventana = 200

# Obtener dimensiones de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# Calcular posición para centrar la ventana de inicio de sesión
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

# Establecer tamaño y posición de la ventana de inicio de sesión
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Crear un frame para contener los elementos de inicio de sesión
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta y campo de entrada para el usuario
label_usuario = tk.Label(frame, text="Usuario:")
label_usuario.grid(row=0, column=0, padx=5, pady=5)
entry_usuario = tk.Entry(frame)
entry_usuario.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo de entrada para la contraseña
label_contraseña = tk.Label(frame, text="Contraseña:")
label_contraseña.grid(row=1, column=0, padx=5, pady=5)
entry_contraseña = tk.Entry(frame, show="*")
entry_contraseña.grid(row=1, column=1, padx=5, pady=5)

# Botón para iniciar sesión
button_ingresar = tk.Button(frame, text="Ingresar", command=validar_ingreso)
button_ingresar.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()
