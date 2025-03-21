import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# https://www.datacamp.com/es/tutorial/poisson-distribution
# https://aprendeconalf.es/docencia/python/manual/matplotlib/
# https://www.statology.org/poisson-distribution-python/

def calcular_poisson():
    try:
        # Definiendo los valores de lambda y k
        lam_da = float(entrada_lambda.get())
        k = int(entrada_k.get())
        
        # Calcular la probabilidad de que ocurran exactamente k eventos
        poison_calculo = poisson.pmf(k, lam_da)
        # El resultado con 6 decimales
        label_resultado.config(text=f"P(X = {k}) = {poison_calculo:.6f}")
        # Para mostrar el resultado en porcentaje
        porcentaje = poison_calculo * 100
        resultado_porcenaje = round(porcentaje, 2)
        label_resultado_probabilidad.config(text=f"La probabilidad de que ocurran exactamente {k} eventos es: {resultado_porcenaje}%")

        # Generando el grafico de Barras
        k_values = np.arange(0, 21)  # Valores de k de 0 a 20
        probabilities = poisson.pmf(k_values, lam_da)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Gráfico de barras
        ax1.bar(k_values, probabilities, color='#b1fa07', alpha=0.7)
        ax1.set_title('Distribución de Poisson')
        ax1.set_xlabel('Número de eventos (k)')
        ax1.set_ylabel('Probabilidad P(X=k)')
        ax1.set_xticks(k_values)
        ax1.grid()
        ax1.axvline(x=k, color='red', linestyle='--', label=f'k = {k}')
        ax1.legend()

        # Generando el grafico circular
        k_resaltar = k
        prob_resto = 1 - poison_calculo

        # Configuración del gráfico circular
        etiquetas = [f'P(X = {k_resaltar})\nλ = {lam_da}', 'Otras probabilidades']
        # Determinando los colores hexadecimal → https://htmlcolorcodes.com/es/
        colores = ['#FFC300', '#2466a7']
        explode = (0.1, 0)  # Separación del sector resaltado

        ax2.pie([poison_calculo, prob_resto],
                labels=etiquetas,
                colors=colores,
                explode=explode,
                autopct='%1.1f%%',
                startangle=90,
                shadow=True,
                textprops={'fontsize': 10}
            )

        ax2.set_title(f'Distribución de Poisson: Probabilidad P(X={k})\n', fontsize=14)
        ax2.axis('equal')  # Gráfico perfectamente circular

        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Ingresa valores válidos, los cuales son números enteros.")

# Crear la ventana principal
ventana_poison = tk.Tk()
ventana_poison.title("Calculadora de Distribución de Poisson")
ventana_poison.geometry("800x400")

# Imagen de Poisson
imagen_poisson = tk.PhotoImage(file="imagenes/poison.png")
# Insertarla en una etiqueta.
label = tk.Label(image=imagen_poisson)
label.pack()

# Crear y colocar los widgets
label_lambda = tk.Label(ventana_poison, text="Valor de λ (lambda):")
label_lambda.pack()

entrada_lambda = tk.Entry(ventana_poison)
entrada_lambda.pack()

label_k = tk.Label(ventana_poison, text="Número de eventos (k):")
label_k.pack()

entrada_k = tk.Entry(ventana_poison)
entrada_k.pack()

boton_calcular = tk.Button(ventana_poison, text="Calcular Probabilidad", command=calcular_poisson)
boton_calcular.pack()

label_resultado = tk.Label(ventana_poison, text="")
label_resultado.pack()

label_resultado_probabilidad = tk.Label(ventana_poison, text="")
label_resultado_probabilidad.pack()

# Iniciar el bucle principal de la interfaz
ventana_poison.mainloop()