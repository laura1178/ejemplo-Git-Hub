import tkinter as tk
from tkinter import messagebox

expresion='' 
def press(num):
    global expresion 
    expresion+=str(num)
    screen_text.set(expresion)
def limpiar():
    global expresion
    screen_text.set('')
    expresion = ''
def limpiar2():
    global expresion
    expresion = expresion [:-1]
    screen_text.set(expresion)

def igual():
    try: 
        global expresion
        result=str(eval(expresion))
        screen_text.set(result)
        expresion = result
    except Exception as e:
        messagebox.showerror('Error', 'Entrada no valida')
        screen_text.set('')
        expresion = ''
ventana = tk.Tk()
ventana.title ("Calculadora")
ventana.geometry("360x500")
ventana.resizable(False, False)
ventana.iconbitmap ("calcu.ico")

colorTexto = "#FFFFFF"
colorBoton = "#000000"
colorBotonIgual = "#FF0008"
colorBotonLimpiar = "#34A9BA"
colorBotonLimpiar2 = "#B08B8B"

screen_text = tk.StringVar()
screenLabel = tk.Label(ventana,textvariable = screen_text, font = ('Arial', 24), bg = '#ffffff', 
fg = "#000000", anchor = 'e', padx = 10, bd = 3, relief = "sunken")

screenLabel.grid (row = 0, column = 0, columnspan = 4, sticky = 'we')

botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3),
]

for (texto, fila, columna) in botones:
    button = tk.Button(ventana, text = texto, width = 5, height = 2, font = ("Arial", 18), bg = colorBoton, 
    fg = colorTexto, command=lambda t=texto: press(t))#está creando una función anónima (usando lambda) que, cuando se ejecute, va a llamar a la función press() pasando el valor de texto como argumento
    button.grid(row=fila, column=columna, padx=5, pady=5,sticky='nsew')

buttonIgual = tk.Button (ventana, text = "=", width = 5, height = 2, font = ("Arial", 18), 
bg = colorBotonIgual, fg = '#ffffff', command = igual)
buttonIgual.grid (row = 4, column = 2, padx = 5, pady = 5, sticky = 'nsew')

buttonLimpiar = tk.Button (ventana, text = "C", width = 5, height = 2, font = ("Arial", 30),
bg = colorBotonLimpiar, fg = '#ffffff', command = limpiar)
buttonLimpiar.grid (row = 5, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = 'nsew')

buttonLimpiar = tk.Button (ventana, text = "©", width = 5, height = 2, font = ("Arial", 30),
bg = colorBotonLimpiar, fg = '#ffffff', command = limpiar2)
buttonLimpiar.grid (row = 5, column = 2, columnspan = 2, padx = 5, pady = 5, sticky = 'nsew')

ventana.mainloop()







