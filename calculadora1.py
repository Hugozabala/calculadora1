import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("600x800")

etiqueta = tk.Label(ventana, text="Escribe los números:")
etiqueta.pack(pady=5)

num1 = tk.Entry(ventana)
num1.pack(pady=5)

num2 = tk.Entry(ventana)
num2.pack(pady=5)

def sumar():
    numero1 = num1.get()
    numero2 = num2.get()
    etiqueta.config(text=f"Resultado: {numero1 + numero2}!")

def restar():
    numero1 = num1.get()
    numero2 = num2.get()
    etiqueta.config(text=f"Resultado: {numero1 - numero2}!")

def multiplicar():
    numero1 = num1.get()
    numero2 = num2.get()
    etiqueta.config(text=f"Resultado: {numero1 * numero2}!")

def dividir():
    numero1 = num1.get()
    numero2 = num2.get()
    if numero2 == 0:
        etiqueta.config(text=f"Resultado: No se puede dividir por zero!")
    else:
        etiqueta.config(text=f"Resultado: {numero1 / numero2}!")

def limpiar():
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    etiqueta.config(text="Escribe los números:")


boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(pady=5)

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()