'''
CALCULADORA
'''

#importamos tkinker y messagebox para ventanas emergentes de error
import tkinter as tk
from tkinter import messagebox

#creamos la ventana principal de la aplicacion
ventana = tk.Tk()                    #instanciamos una ventana principal
ventana.title("calculadora basica") #le damos un titulo a la ventana
ventana.geometry("600x700")          #establecemos el tamanno

#creamos una caja de texto para que el usuario ingrese el primer numero 
entrada1 = tk.Entry(ventana)    #entrada de texto
entrada1.pack(pady=5)           #la colocamos en la ventana con espacio vertical

#segunda entrada para el siguiente numero
entrada2 = tk.Entry(ventana)       #entrada de texto(segundo numero)
entrada2.pack(pady=5)

#etiqueta donde se mostrara el resultado
resultado_label = tk.Label(ventana, text="resultado:")  #creamos una etiqueta
resultado_label.pack(pady=10)                           #la colocamos con algo de espacio

#lista para almacenar el historial de operaciones
historial = []

#funcion que realiza la operacion matematica
def calcular(op):
    try:
        #obtenemos los numeros desde las entradas y los convertimos a float
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        
        #evaluamos la operacion segun el boton que se haya presionado
        if op == "+":
            resultado = num1 + num2
        elif op == "-":
            resultado = num1 - num2
        elif op == "*":
            resultado = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError  #lanzamos un error si se intenta dividir por cero
            resultado = num1 / num2
        
        #creamos el texto del resultado con la operacion completa    
        resultado_texto = f"{num1} {op} {num2} = {resultado}"
        #mostramos el resultado en la etiqueta 
        resultado_label.config(text=resultado_texto)
        #guardamos la operacion en el historial
        historial.append(resultado_texto)
        #actualizamos la caja de historial para meter la nueva operacion
        actualizar_historial()
        
    except ValueError:
        #si el usuario no ingreso un numero valido, mostramos error
        messagebox.showerror("error", "ingresa solo numeros.")
    except ZeroDivisionError:
        #si intenta dividir por cero, mostramos error
        messagebox.showerror("error", "no se puede dividir por cero.")

#botones para cada una de las operaciones
#cada boton llama a la funcion 'calcular' con el simbolo correspondiente
tk.Button(ventana, text="+", command=lambda: calcular("+")).pack(fill="x")
tk.Button(ventana, text="-", command=lambda: calcular("-")).pack(fill="x")
tk.Button(ventana, text="*", command=lambda: calcular("*")).pack(fill="x")
tk.Button(ventana, text="/", command=lambda: calcular("/")).pack(fill="x")

#etiqueta que indica que abajo esta el historial
tk.Label(ventana, text="historial:").pack()

#caja de texto donde se mostrara el historial (solo lectura)
historial_texto = tk.Text(ventana, height=8)
historial_texto.pack()

#funcion para actualizar la caja del historial
def actualizar_historial():
    historial_texto.delete("1.0", tk.END)
    for operacion in historial[-5:]: #muestra las ultimas 5
        historial_texto.insert(tk.END, operacion + "\n")

#iniciamos el bucle principal de la interfaz (esto mantiene la ventana abierta)        
ventana.mainloop()
        