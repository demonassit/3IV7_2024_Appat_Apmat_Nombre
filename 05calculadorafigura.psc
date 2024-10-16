//vamos a crear un programa para calcular areas y perimetros
//pero con el uso de subprocesos

//vamos a crear el subproceso del rectangulo
SubProceso Rectangulo(base, altura)
	Definir area, perimetro Como Real
	area = base * altura
	perimetro = 2*(base+altura)
	Escribir "El area del rectangulo es: ", area
	Escribir "El perimetro del rectangulo es: ", perimetro
FinSubProceso

SubProceso Triangulo(base, altura, lado1, lado2, lado3)
	Definir area, perimetro Como Real
	area = (base * altura)/2
	perimetro = lado1 + lado2 + lado3
	Escribir "El area del triangulo es: ", area
	Escribir "El perimetro del triangulo es: ", perimetro
FinSubProceso

Algoritmo CalculadoradeFiguras
	Definir opcion Como Caracter
	Definir base, altura, lado1, lado2, lado3 Como Real
	//vamos a crear el menu
	Escribir "Selecciona una opcion: "
	Escribir "A Area y Perimetro del Rectangulo"
	Escribir "B Area y Perimetro del Triangulo"
	
	Leer opcion
	
	Segun opcion Hacer
			//para el caso 1
		Caso "A" :
			Escribir "Ingresa la base del rectangulo"
			Leer base
			Escribir "Ingresa la altura del rectangulo"
			Leer altura
			Rectangulo(base, altura)
		Caso "B" :
			Escribir "Ingresa la base del triangulo"
			Leer base
			Escribir "Ingresa la altura del triangulo"
			Leer altura
			Escribir "Ingresa lado 1"
			Leer lado1
			Escribir "Ingresa lado 2"
			Leer lado2
			Escribir "Ingresa lado 3"
			Leer lado3
			Triangulo(base, altura, lado1, lado2, lado3)
		De Otro Modo:
			Escribir "Opcion no valida"
	FinSegun
FinAlgoritmo


