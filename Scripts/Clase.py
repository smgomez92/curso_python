nombre = ""
apellido = ""

def setApellido(ape):
	apellido = ape
	print(apellido)

def setNombre(nom):
	nombre = nom
	#print(nombre)

def factorial(n):
	if n==0 :
		return 1 
	else:
		return n*factorial(n-1)


def calculo_area(b=None,h=None):
	if b == None or h == None:
		print("No se han ingresado valores")
	else:
		return (b*h)/2







