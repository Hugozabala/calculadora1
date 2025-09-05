import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Escribe tu nombre:")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

def saludar():
    nombre = entrada.get()
    etiqueta.config(text=f"Hola, {nombre}!")

def limpiar():
    entrada.delete(0, tk.END)
    etiqueta.config(text="Escribe tu nombre:")

boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()