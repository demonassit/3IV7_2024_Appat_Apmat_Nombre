#derivado a que es necesario poder almacenar diferentes fuentes de datos
#en python se utiliza la variable diccionario
#un diccionario es capaz de poder almacenar diferentes tipos de dato en formato de lista
import tkinter as tk
from tkinter import messagebox, simpledialog

#el examen debe de tener almenos 8 elementos de la lista que deseen guardar el examen debe de posee elementos de dialogo y mensajes de salida con tkinter, la lista debe de implementar al menos 30 diferentes elementos y debe verse una interfaz mediante la cual los imprima en formato de lista

#primero vamos a crear una lista de alumnos
alumnos = []

#vamos a crear una funcion que se encargue de registrar un alumno

def registrar_alumno():
    boleta = simpledialog.askstring("Entrada","Ingresa la boleta del alumno: ")
    nombre = input("Ingresa el nombre del alumno: ")
    appat = input("Ingresa el apellido paterno del alumno: ")
    apmat = input("Ingresa el apellido materno del alumno: ")
    fecnac = input("Ingresa la fecha de nacimiento(dd/mm/aaaa) del alumno: ")

    calificaciones = []
    #vamos a solicitar 3 calificaciones
    for i in range(1,4):
        calificacionparcial = float(input("Ingrese la calificacion del parcial: "))
        calificaciones.append(calificacionparcial)

    #defino al alumno
    alumno = {
        "boleta" : boleta,
        "nombre" : nombre,
        "apellido_paterno" : appat,
        "apellido_materno" : apmat,
        "fecha_nacimiento" : fecnac,
        "calificaciones" : calificaciones
    }

    alumnos.append(alumno)
    messagebox.showinfo("Exito", "Alumno registrado exitosamente")

#funcion para poder consultar los datos del arreglo de alumnos(lista)
def consultar_alumnos() :
    if not alumnos :
        print("No hay registros solo juguito contigo")
    else :
        print("Lista de Alumnos: \n")
        for alumno in alumnos :
            print("Boleta: {alumno['boleta']}, Nombre: {alumno['nombre']}{alumno['apellido_paterno']}{alumno['apellido_materno']}, Fecha de Nacimiento: {alumno['fecha_nacimiento']}, Calificaciones: {alumno['calificaciones']} \n" )

#funcion para buscar y editar por la boleta
def editar_alumno() :
    boleta = input("Ingrese la boleta del alumnos que desea editar: ")
    for alumno in alumnos :
        if alumno['boleta'] == boleta :
            alumno['nombre'] = input("Ingresa el nuevo nombre o presiona Enter para mantener el actual:") or alumno['nombre']
            alumno['apellido_paterno'] = input("Ingresa el nuevo apellido paterno o presiona Enter para mantener el actual:") or alumno['apellido_paterno']
            alumno['apellido_materno'] = input("Ingresa el nuevo apellido materno o presiona Enter para mantener el actual:") or alumno['apellido_materno']
            alumno['fecha_nacimiento'] = input("Ingresa la nueva fecha de nacimiento o presiona Enter para mantener el actual:") or alumno['fecha_nacimiento']
            #editamos las calificaciones
            for i in range(3) :
                nueva_calificacion = input("Ingresa ela nueva calificacion o presiona Enter para mantener el actual:")
                if nueva_calificacion: 
                    alumno['calificaciones'][i] = float(nueva_calificacion)
    return
    print("No hay mas alumnos")

#eliminar alumno
def eliminar_alumno():
    print("esto es parte del examen")

#vamos a crear un menu
def main() :
    while True:
        print("Menu de Gestión de Proximos Extras")
        print("1.- Registrar Alumno")
        print("2.- Consultar lista de Alumnos")
        print("3.- Editar Alumno")
        print("4.- Eliminar Alumno")
        print("5.- Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1" :
            registrar_alumno()
        elif opcion == "2" :
            consultar_alumnos()
        elif opcion == "3" :
            editar_alumno()
        elif opcion == "4" :
            #ahi la crean
            eliminar_alumno()
        elif opcion == "5" :
            print("Ayos")
            break
        else : 
            print("opcion no valida")

main()