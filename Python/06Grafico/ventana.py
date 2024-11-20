import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#boton para una funcion de saludar
def mostrar_saludo():
    nombre = entrada_nombre.get()
    saludo = f"Hola {nombre}"
    etiqueta_saludo.config(text=saludo)

#funcion para mostrar el estado de la casilla de verificacion
def mostrar_estado_casilla():
    estado = "Seleccionado" if casilla_var.get() else "No seleccionado"
    etiqueta_casilla.config(text=f"Estado de la casilla : {estado}")

#funcion para un radio button
def mostrar_opcion():
    etiqueta_opcion.config(text=f"Opcion seleccionada: {opcion_var.get()}")

#una barra de progreso
def incrementar_progreso():
    progreso.step(10)

#vamos a crear la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Interfaz en Python")
ventana.geometry("800x600")

#etiquetas 
etiqueta_bienvenida = tk.Label(ventana, text= "Bienvenido a tu primera interfaz", font=("Arial", 24))
etiqueta_bienvenida.pack(pady=10)

#boton para mostrar el saludo
boton_saludo = tk.Button(ventana, text= "Saludar, ", command=mostrar_saludo)
boton_saludo.pack(pady=5)

#etiqueta del saludo
etiqueta_saludo = tk.Label(ventana, text="")
etiqueta_saludo.pack()



ventana.mainloop()
