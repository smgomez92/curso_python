#-*- coding: utf-8 *-*
#para ingresar un número decimal por teclado se lo hace de la siguiente 

#decimal = float(input("Ingrese un número")) 
#se lo hace asi ya que input() recive solo cadenas de texto asi que hay q transformarlas 

#para introducir x numero de de valores en una lista

valores = []
#aki se le pedrà al usuario q ingrese el numero de valores que quiere ingresar 
x = int(input("El número de valores a ingresar ")) 

for v in range(x):
	valores.append(input("Introduce un valor"))

for val in valores:
	print(val)

#Entrada de datos en un script 
#archivos que se crean en el disco duro y se ejecutan en el S.O