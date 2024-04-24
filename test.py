import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

etiqueta = tkinter.Label(ventana, text = "Hola mundo")
etiqueta.pack()

ventana.mainloop()