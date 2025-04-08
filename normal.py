import math
import tkinter as tk
from tkinter import messagebox
from scipy.stats import norm
from math import sqrt


# Función que calcula las probabilidades
def calcular_probabilidades():
    try:
        # Obtener los valores ingresados
        media = float(entrada_media.get())
        desviacion = float(entrada_desviacion.get())
        x = float(entrada_x.get()) # Valor fijo para el cálculo de P(X = 10)

        menor_que = float(entrada_menor_que.get()) 
        valor_a_entre = float(entrada_entre_a.get())
        valor_b_entre = float(entrada_entre_b.get())
        
        # Validación de datos
        if desviacion <= 0:
            messagebox.showerror("Error", "La desviación estándar debe ser mayor que cero.")
            return
        
        # Cálculos
        prob_exacta = (1 / (desviacion * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - media) / desviacion) ** 2)  # P(X = 10), aproximado a 0
        prob_menor_6 = norm.cdf(menor_que, media, desviacion)
        prob_entre_7_y_12 = norm.cdf(valor_a_entre, media, desviacion) - norm.cdf(valor_b_entre, media, desviacion)
        
        # Mostrar resultados
        mensaje = (
            f"Resultados del ejercicio con media = {media} y desviación = {desviacion}:\n\n"
            f"1. P(X = {x}) ≈ {prob_exacta:.4f} (≈ 0 en variables continuas)\n"
            f"2. P(X < {menor_que}) = {prob_menor_6:.4f}\n"
            f"3. P({valor_a_entre} < X < {valor_b_entre}) = {prob_entre_7_y_12:.4f}"
        )
        messagebox.showinfo("Resultados", mensaje)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos en los campos.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Distribución Normal - Variable Aleatoria Continua")
ventana.geometry("600x710")
ventana.config(bg="#e6f2ff")

# Título
titulo = tk.Label(ventana, text="VARIABLE ALEATORIA CONTINUA", font=("Arial", 16, "bold"), bg="#e6f2ff")
titulo.pack(pady=10)

# Explicación
explicacion = (
    "¿Qué es una Variable Aleatoria Continua?\n"
    "Es aquella que puede tomar infinitos valores dentro de un intervalo de números reales.\n"
    "Estas variables no se pueden contar, se miden."
)
lbl_explicacion = tk.Label(ventana, text=explicacion, font=("Arial", 11), bg="#e6f2ff", justify="left")
lbl_explicacion.pack(pady=5)

# Ejemplos
ejemplos = (
    "Ejemplos:\n"
    "• Tiempo de espera en una fila (5.2, 5.25, 5.3 minutos...)\n"
    "• Peso de una persona (70.1 kg, 70.15 kg...)\n"
    "• Temperatura en una ciudad (28.4°C, 28.45°C...)"
)
lbl_ejemplos = tk.Label(ventana, text=ejemplos, font=("Arial", 11), bg="#e6f2ff", justify="left")
lbl_ejemplos.pack(pady=5)

# Entrada para Media
lbl_media = tk.Label(ventana, text="Ingrese la Media (μ):", font=("Arial", 12), bg="#e6f2ff")
lbl_media.pack(pady=5)
entrada_media = tk.Entry(ventana, font=("Arial", 12))
entrada_media.pack(pady=5)

# Entrada para Desviación Estándar
lbl_desviacion = tk.Label(ventana, text="Ingrese la Desviación Estándar (σ):", font=("Arial", 12), bg="#e6f2ff")
lbl_desviacion.pack(pady=5)
entrada_desviacion = tk.Entry(ventana, font=("Arial", 12))
entrada_desviacion.pack(pady=5)

# Entrada para x
x_media = tk.Label(ventana, text="Ingrese el valor de x:", font=("Arial", 12), bg="#e6f2ff")
x_media.pack(pady=5)
entrada_x = tk.Entry(ventana, font=("Arial", 12))
entrada_x.pack(pady=5)

# Entrada para menor que
        # valor_a_entre = int(entrada_entre_a.get())
        # valor_b_entre = int(entrada_entre_b.get())
menor_que_media = tk.Label(ventana, text="Ingrese el valor de x:", font=("Arial", 12), bg="#e6f2ff")
menor_que_media.pack(pady=5)
entrada_menor_que = tk.Entry(ventana, font=("Arial", 12))
entrada_menor_que.pack(pady=5)

# Entrada para entre a y b
entrada_entre_a_media = tk.Label(ventana, text="Ingrese el de a:", font=("Arial", 12), bg="#e6f2ff")
entrada_entre_a_media.pack(pady=5)
entrada_entre_a = tk.Entry(ventana, font=("Arial", 12))
entrada_entre_a.pack(pady=5)

# Entrada para entre a y b
entrada_entre_b_media = tk.Label(ventana, text="Ingrese el de b:", font=("Arial", 12), bg="#e6f2ff")
entrada_entre_b_media.pack(pady=5)
entrada_entre_b = tk.Entry(ventana, font=("Arial", 12))
entrada_entre_b.pack(pady=5)


# Botón para calcular
btn_calcular = tk.Button(ventana, text="Calcular Probabilidades", font=("Arial", 12), bg="#0066cc", fg="white", command=calcular_probabilidades)
btn_calcular.pack(pady=20)

# Ejecutar ventana
ventana.mainloop()
