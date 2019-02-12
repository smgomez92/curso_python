# -*- coding: utf-8 *-*
#hoasldads

"""nota1 = 10
nota2 = 20

promedio = (nota1 +  nota2)/2

print(promedio%2)

mensaje = "La fuerza es: "

masa = 90
aceleracion = 9.8

fuerza = masa * aceleracion

print(mensaje)
print(fuerza)
print("Instituto Nacional \"Mejía\" ")
print("hola q hace\n con salto de linea ")
print(r"hola q hace\n como le va (crudo) ")


#Una impresion de varias lineas 
#print("""#hola q hace 

	#como le va""")

#concatenar Strings se puede lograr con el operador + pero solo entre el mismo tipo de dato 
"""print(mensaje+mensaje)
s = "hola" "q" "ase"
print(s*10) # :O 

p="python"
print(p[3])

palabra = "Santiago"
print(palabra[1:3])
#las cadena de texto son inmutables pero las listas si 
lista = [1,2,3,'Santiago']
print(lista[2])
print(lista[3])
lista[3]='Mauricio'
print(lista[3])

#tuplas no son innmutables
mi_tupla = ('a','c','5')
#mi_tupla[0]='b'
print(mi_tupla[0])

print(mi_tupla[-1])
print(mi_tupla[1:3])

#diccionarios

mi_diccionario = {'a':'Santiago', 'b': 6, 'c': 7 }
print(mi_diccionario['a'])
#borrar elementos del diccionario y reasignar valores 
print(mi_diccionario)
del(mi_diccionario['c'])
mi_diccionario['a']='Mauricio'
print(mi_diccionario)

print('Santiago Gómez')

#Asignacion multiple

a, b, c = 8, 'Santiago', False
print(a)
print(b)
print(c)
#Asignacion con una tupla 
a, b, c = mi_tupla
print(a)
print(b)
print(c)
#asignacion con una lista 
d, e, f, h = lista
print(d)
print(e)
print(f)
print(h)

#Condcionales 
f_1 = 5==7 or 3>1
print(f_1)



#Estructuras de control

num_1 = 10
num_2 = 2
num_3 = 300
if num_1>num_2:
	print('Numero 1 mayor')
elif num_2>num_3:
	print('Numero 2 mayor')
else:
	if num_1>num_3:
	   print('Numero 2 mayor')	
	else:
	   print('Numero 3 mayor')"""



#lectura por teclado

"""num_1 = int(input("Ingrese el número 1: "))
num_2 = input("Ingrese el número 2: ")
num_1=float(num_2)
num_3 = input("Ingrese el número 3: ")
num_1=int(num_3)"""
num_1 = 30
num_2 = 210
num_3 = 90


"""if num_1 > num_2 and num_1 > num_3:
  print(num_1, ' es mayor')
elif num_2 > num_1 and num_2 > num_3:
  print(num_2, ' es mayor ')
else: 
  print(num_3,' es mayor ')



#formas de imprimir distintos tipos de datos 
print(num_3,num_2)
print('los números son: ', num_1, num_2, num_3)

#otra forma solo pa strings
print('hola '+'perro')"""

"""n=0
while n < 10:
	if (n % 2) == 0:
		print(n, ' es un número par')
	else:
		print(n, ' es un número impar')
    
    n = n + 1"""


d = [10,11]


"""matriz = [ [1,2,3,4],
           [2,3,4,5],
           [2,41,44,1],
           [1,2,3,4]
]

print('matriz original ', matriz)

l_1 = matriz[0]
l_2 = matriz[1]
l_3= matriz[2]
l_4 = matriz[3]

l_1[-1]=sum(l_1[:3])
l_2[-1]=sum(l_2[:3])
l_3[-1]=sum(l_3[:3])
l_4[-1]=sum(l_4[:3])



matriz[0] = l_1
matriz[1] = l_2
matriz[2] = l_3
matriz[3] = l_4

print('matriz modificada', matriz)"""

#otra forma 
#con un for talvez 
"""matriz = [ [1,2,3,4],
           [2,3,4,5],
           [2,41,44,1],
           [1,2,3,4]
]

#matriz[i][-1] = suma(matriz[i][:-1]) #para referirnos al ultimo elemento de la fila i """

# para invertir una cadena 

"""cadena = "Hola mundo"
print(cadena)
#cadena = cadena[::-1]
print(cadena)
otra = 'odnum aloH'
print(otra[::-1])

print('Un programador dice: \"',cadena[:4],cadena[4:],'\" en su primer programa ..:v ')"""

a = input("Ingrese una cadena")
print(a==5)
