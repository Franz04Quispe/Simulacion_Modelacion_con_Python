import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Menu, messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# https://www.datacamp.com/es/tutorial/poisson-distribution
# https://aprendeconalf.es/docencia/python/manual/matplotlib/
# https://www.statology.org/poisson-distribution-python/

# FUNCIONES
def abrir_ventana_secundaria():
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.config(width=300, height=200)
    boton_cerrar = ttk.Button(
        ventana_secundaria,
        text="Cerrar ventana", 
        command=ventana_secundaria.destroy
    )
    boton_cerrar.place(x=75, y=75)

def abrir_script_resto():
    resto = tk.Tk()
    resto.title("Hallar el resto de una división sin usar MODULO")
    resto.geometry("800x400")
    
    def calcular_resto():
        try:
            numerador = int(entry_numerador.get())
            denominador = int(entry_denominador.get())
            if denominador == 0:
                messagebox.showwarning("Advertencia", "El denominador no puede ser cero.")
                return
            cociente = numerador // denominador
            resto = numerador - (cociente * denominador)
            label_resultado.config(text=f"El resto de {numerador} dividido por {denominador} es: {resto}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")

    label_numerador = tk.Label(resto, text="Numerador:")
    label_numerador.pack()

    entry_numerador = tk.Entry(resto)
    entry_numerador.pack()

    label_denominador = tk.Label(resto, text="Denominador:")
    label_denominador.pack()

    entry_denominador = tk.Entry(resto)
    entry_denominador.pack()

    boton_calcular = tk.Button(resto, text="Calcular Resto", command=calcular_resto)
    boton_calcular.pack()

    label_resultado = tk.Label(resto, text="")
    label_resultado.pack()
    
    resto.mainloop()

def abrir_script_poisson():
    ventana_poison = tk.Tk()
    ventana_poison.title("CAlculo de Poisson")
    ventana_poison.geometry("800x400")
    
    def calcular_poisson():
        try:
            lam_da = float(entrada_lambda.get())
            k = int(entrada_k.get())
            
            poison_calculo = poisson.pmf(k, lam_da)
            label_resultado.config(text=f"P(X = {k}) = {poison_calculo:.6f}")
            porcentaje = poison_calculo * 100
            resultado_porcenaje = round(porcentaje, 2)
            label_resultado_probabilidad.config(text=f"La probabilidad de que ocurran exactamente {k} eventos es: {resultado_porcenaje}%")

            k_values = np.arange(0, 21)
            probabilities = poisson.pmf(k_values, lam_da)

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

            ax1.bar(k_values, probabilities, color='#b1fa07', alpha=0.7)
            ax1.set_title('Distribución de Poisson')
            ax1.set_xlabel(f'Número de eventos (k) = {k} y λ = {lam_da}')
            ax1.set_ylabel('Probabilidad P(X=k)')
            ax1.set_xticks(k_values)
            ax1.grid()
            ax1.axvline(x=k, color='red', linestyle='--', label=f'k = {k}')
            ax1.legend()

            k_resaltar = k
            prob_resto = 1 - poison_calculo

            etiquetas = [f'P(X = {k_resaltar})\nλ = {lam_da}', 'Otras probabilidades']
            colores = ['#FFC300', '#2466a7']
            explode = (0.1, 0) # Separación del sector resaltado
            # Para que la primera porción del gráfico circular se separará un 10% del centro del gráfico

            ax2.pie([poison_calculo, prob_resto],
                    labels=etiquetas,
                    colors=colores,
                    explode=explode,
                    autopct='%1.2f%%',
                    #significa que el porcentaje se mostrará con una cifra antes del punto decimal y una cifra después del punto decimal.
                    startangle=90,
                    shadow=True,
                    textprops={'fontsize': 10}
                )

            ax2.set_title(f'Distribución de Poisson: Probabilidad P(X={k})\n', fontsize=14)
            ax2.axis('equal')

            plt.tight_layout()
            plt.show()
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos, los cuales son números enteros.")

    imagen_poisson = tk.PhotoImage(file="imagenes/poison.png")
    label = tk.Label(image=imagen_poisson)
    label.pack()
    
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

    ventana_poison.mainloop()

# VENTANA PRINCIPAL
main = tk.Tk()
main.geometry("1200x800")
main.title("Simulación y Modelación | I-2025 | Franz Joel Quispe Mamani")
main.minsize(1000, 700)
main.maxsize(1200, 800)
main.configure(bg='azure')

icono = tk.PhotoImage(file="imagenes/bolivia.png")
main.iconphoto(True, icono)

menubar = Menu(main)
file = Menu(menubar, tearoff = 0)

def abrir_archivo():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            print(file.read())

menubar.add_cascade(label ='Participaciones', menu = file)
file.add_command(label ='Resto de una fraccion', command = abrir_script_resto)
file.add_command(label ='Poisson', command = abrir_script_poisson)
file.add_command(label ='Abrir...', command = abrir_archivo)
file.add_separator()
file.add_command(label ='Salir', command = main.destroy)

boton_abrir = ttk.Button(
    main,
    text="Abrir ventana secundaria",
    command=abrir_ventana_secundaria
)
boton_abrir.pack()

main.config(menu = menubar)
main.mainloop()