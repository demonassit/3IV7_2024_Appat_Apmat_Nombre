#vamos a crear una funcion que se encargue de sumar dos arreglos

def sumar_arreglos(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        print("Error: Los arreglos deben de tener la misma longitud")
        return None
    else:
        suma = []
        for i in range(len(arreglo1)):
            suma.append(arreglo1[i]+arreglo2[i])
        return suma
#programa principal

#primero definimos los arreglos
arreglo1 = []
arreglo2 = []

n = int(input("Introduce el tamaño de los arreglos"))

print("Introduce los elementos del primer arreglo")
for i in range(n):
    num = float(input("Ingresa el elemento :" ))
    arreglo1.append(num)

print("Introduce los elementos del segundo arreglo")
for i in range(n):
    num = float(input("Ingresa el elemento {i+1}: "))
    arreglo2.append(num)

resultado = sumar_arreglos(arreglo1, arreglo2)

#mostramos el resultado
if resultado is not None:
    print("La suma de los dos arreglos es: ", resultado)