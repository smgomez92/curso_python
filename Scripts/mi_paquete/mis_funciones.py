# -*- coding: utf-8 *-*
PI = 3.141516

def mi_funcion():
	print('esta es la funcion del paquete mi_paquete')


def suma(a,b):
	resultado = a + b
	return resultado


def buscar(elemento):
    i=0
    lista = [1,2,3,4,5,6,7,8,9,10]    
    for n in lista:
	    if n == elemento:
		    return True
	    else:
		    i += 1
		    if i == len(lista):			    
			    return False



def operaciones(a, b,opcion):
    d={
     '1':a + b,
     '2':a - b,
     '3':a * b,
     '4':a / b,
    }
    return d[opcion]

"""#parámetros arbitrarios
def params (a, *tupla,**keys):
	print (a) 

	for t in tupla:
		print (t)

	for key in keys:
		print(keys[key])

params(2,3,4,5,'hola',c='perro',d=2*2)

#desempaquetado de datos en una tupla
def suma2(a,b):
    print(a+b)

datos = [40,40]
suma2(*datos)

def multiplicacion(num1,num2):
	print(num1*num2)

#desempaquetado de datos en un diccionario 
datos1={'num1':2,'num2':4}
multiplicacion(**datos1)"""


