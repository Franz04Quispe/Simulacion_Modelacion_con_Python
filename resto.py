import tkinter as tk
from tkinter import messagebox

def calcular_resto():
    try:
        numerador = int(entry_numerador.get())
        denominador = int(entry_denominador.get())
        if denominador == 0:
            messagebox.showerror("Error", "El denominador no puede ser cero.")
            return
        resto = numerador % denominador
        label_resultado.config(text=f"El resto de {numerador} dividido por {denominador} es: {resto}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Resto de División")
# Dimensiones de la ventana
ventana.geometry("1200x800")
# Dimensiones minimas de la ventana
ventana.minsize(1180, 800)
# Dimensiones maximas de la ventana
ventana.maxsize(1200, 800)

# Crear y colocar los widgets
label_numerador = tk.Label(ventana, text="Numerador:")
label_numerador.pack()

entry_numerador = tk.Entry(ventana)
entry_numerador.pack()

label_denominador = tk.Label(ventana, text="Denominador:")
label_denominador.pack()

entry_denominador = tk.Entry(ventana)
entry_denominador.pack()

boton_calcular = tk.Button(ventana, text="Calcular Resto", command=calcular_resto)
boton_calcular.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()