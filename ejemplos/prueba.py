import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Menu, messagebox

# FUNCIONES
# ABRIR VENTANA SECUNDARIA
def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.config(width=300, height=200)
    # Crear un botón dentro de la ventana secundaria para cerrar la misma.
    boton_cerrar = ttk.Button(
        ventana_secundaria,
        text="Cerrar ventana", 
        command=ventana_secundaria.destroy
    )
    boton_cerrar.place(x=75, y=75)

# ABRIR SCRIPT → RESTO DE UNA FRACCIÓN
def abrir_script_resto():
    resto = tk.Tk()
    resto.title("Calculadora de Resto de División")
    resto.geometry("1200x800")
    
    # Funciona para calcular el resto
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

    # Crear y colocar los widgets
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

# Crear la ventana principal.
main = tk.Tk()
main.geometry("1200x800")
main.title("Ventana principal")

# Creación de la barra de menú
menubar = Menu(main) 
# Añadir opciones a la barra de menú
# ---------------------------------------------
file = Menu(menubar, tearoff = 0)
# FUNCIONES
# ................................................
def abrir_archivo():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            print(file.read())

# ................................................
#CINTA DE OPCIONES
menubar.add_cascade(label ='Participaciones', menu = file) 
file.add_command(label ='Resto de una fraccion', command = abrir_script_resto)
file.add_command(label ='Abrir...', command = abrir_archivo) 
file.add_separator() 
file.add_command(label ='Salir', command = main.destroy) 
# ---------------------------------------------
"""
Crear un botón dentro de la ventana principal
que al ejecutarse invoca a la función
abrir_ventana_secundaria().
"""
boton_abrir = ttk.Button(
    main,
    text="Abrir ventana secundaria",
    command=abrir_ventana_secundaria
)
boton_abrir.place(x=100, y=100)

main_frame = ttk.Frame(main, padding=10)
main_frame.grid()

#SISTEMA GRID DE TKINTER: https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/

ttk.Label(main_frame, text="Hola a todos!").grid(row=1, column=2)

ttk.Button(main_frame, text="Quit", command=main.destroy).grid(row=2, column=2)

main.config(menu = menubar) 
main.mainloop()