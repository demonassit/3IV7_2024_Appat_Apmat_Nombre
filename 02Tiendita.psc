Algoritmo tiendita
	
	Definir producto como Texto
	Definir codigoproducto, cantidad como Entero
	Definir precio como Real
	
	//tengo que crear un menu de seleccion
	Mientras opcion <> 5  Hacer
		Escribir "1.- Ingresar un nuevo Producto"
		Escribir "2.- Actualiza un Producto"
		Escribir "3.- Consulta el Inventario"
		Escribir "4.- Generar Reporte"
		Escribir "5.- Salir"
		
		Leer opcion
		
		Segun opcion Hacer
			Caso 1:
				Escribir "Ingresa el nombre del producto"
				Leer producto
				Escribir "Ingresa el codigo del producto"
				Leer codigoproducto
				Escribir "Ingresa la cantidad"
				Leer cantidad
				Escribir "Ingresa el Precio"
				Leer precio
			Caso 2:
				Escribir "Ingresa el codigo del producto a actualizar"
				Leer codigoproducto
				Escribir "Ingresa la nueva cantidad"
				Leer cantidad
			Caso 3:
				Escribir "Consultar Inventario"
				Escribir "nombre del producto ", producto
				Escribir "codigo del producto ", codigoproducto
				Escribir "precio del producto ", precio
				Escribir "cantidad del producto ", cantidad
			Caso 4:
				Escribir "Habia una vez un patito que decia miau miau"
			
		Fin Segun
		
		
	Fin Mientras
	
	
	
	
FinAlgoritmo
