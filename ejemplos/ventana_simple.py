from tkinter import *
from tkinter import ttk

# Root es la ventana principal
root = Tk()
#Titulo de la ventana
root.title("Hello World")
#Dimensiones de la ventana
root.geometry("600x400")
#Dimensiones minimas de la ventana
root.minsize(200, 200)
#Dimensiones maximas de la ventana
root.maxsize(400, 400)
#Iconoo de la ventana

#Background de la ventana
root.configure(bg = 'gray')

main_frame = ttk.Frame(root, padding=10)
main_frame.grid()

ttk.Label(main_frame, text="Hello World!").grid(column=0, row=0)

ttk.Button(main_frame, text="Quit", command=root.destroy).grid(column=1, row=1)

root.mainloop()