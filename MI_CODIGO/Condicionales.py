#-*- coding: utf-8 *-*
#Importando el modulo mis_funciones del paquete mi_paquete y dándole un alias fun
import mi_paquete.mis_funciones as fun 

"""a = 3>4
b = 3<5

print (a,b)


if not a : 
	print(True)
else: 
	print(False)

if  b and a:
	print(True)
else:
	print(False)


print(not (a<b))"""

"""n=1
while n <= 10:
	
	if (n % 2) == 0:
		print(n,' Número par')
	else:
		print(n,' Número impar')

	n +=1"""


"""print('\nNUMERO MAGICO \n')
teclado = '6'
num1 = int(teclado) 
numM = 12345679
num1 *= 9
numM *= num1 
print(numM)"""

"""#PROGRAMA PARA OPERAR DOS NUMEROS, sin control de excepciones 
a=1000
b=2
diccionario = {'Suma':1,'Resta':2,'Multiplicación':3, 'División':4 }
opcion='Suma'
if diccionario[opcion]==1:
	resultado = a + b
	print('La suma de ',a,' + ',b,' es: ',resultado)
elif diccionario[opcion]==2:
	resultado = a - b
	print('La ',opcion, ' de',a,' - ',b,' es: ',resultado)
elif diccionario[opcion]==3:
	resultado = a * b
	print('La ',opcion, ' de',a,' * ',b,' es: ',resultado)

elif diccionario[opcion]==4:
	resultado = a / b
	print('La ',opcion, ' de',a,' / ',b,' es: ',resultado)
else: 
	print('No existe esa opción',opcion)
"""

"""#Otra calculadora de otra forma usando el diccionario ..:v 

a=2**2
b=1
d={
 'Suma':a + b,
 'Resta':a - b,
 'Multiplicacion':a * b,
 'Division':a / b,
}
opcion = 'Suma'
print(d[opcion])"""

"""#el bucle while, tambien se le puede poner un else :O en python ... 
c = 0
while c < 10:
	c += 1
	print('c vale ',c)
else:
	print('el último valor de c es: ',c)"""



"""bandera = True
c=0 
while True:
	if c < 10:
		c +=1
		print(c)		
	else:
		print('break')
		break"""

"""#metodo para buscar un elemento en la lista 
lista = [1,2,3,4,5,6,7,8,9]
i = 0
elemento=3
while True:
	if i<len(lista):
		if lista[i]==elemento:
			print("elemento ",lista[i], "Encontrado")
			break 
		else:
			i += 1
	else:
		print('Elemento',elemento,'no encontrado')
		break
"""

#Otra manera

"""lista = [1,2,3,4,5,6,7,8,9]
i = 0
elemento=1

while i < len(lista):
	if lista[i]==elemento:
		print("elemento ",lista[i], "Encontrado")
		break
	i += 1
		
else:
	print('Elemento',elemento,'no encontrado')"""



#ciclo for, parecido al for each de java 
"""i=0
lista = [1,2,3,4,5,6,7,8,9,10]
elemento = 10
for n in lista:
	if n == elemento:
		print("elemento ",n, "encontrado")
		break
	else:
		i += 1
		if i == len(lista):
			print('Elemento',elemento,'no encontrado')"""
			


"""# otro forma 		
lista = [1,2,3,4,5,6,7,8,9,10]
elemento = 11
for i,numero in enumerate(lista):
	if elemento == numero:
		print("elemento ",numero, "encontrado")
	else:
		
		if i==len(lista) - 1 :
			print('Elemento',elemento,'no encontrado')
	


print(list(enumerate(lista)))

print(list(range(2,4)))"""


"""usu=12

while True:
	if not (usu % 2) == 0:
		print('Ingreso correcto')
		break
	else:
		print('Ingrese de nuevo')
		usu=1
"""

# promedio de n números 

"""usu = 6

lista_n=list(range(1,usu+1))
print(lista_n)
for i,n in enumerate(lista_n):
	lista_n[i]*=len(lista_n)
print(lista_n)
print(sum(lista_n)/5)

print(12 in lista_n)"""

#la funcion lista.append(elemento) arega un elemento en la lista 

"""print(fun.PI)
fun.mi_funcion()
r = fun.suma(2,4)
print(r)"""

"""#llamando a la función buscar(parametro) para buscar un valor dado un parámtro
usu = 9 
#res = fun.buscar(usu)
if fun.buscar(usu):
	print('Elemento',usu,'encontrado')
else:
	print('Elemento',usu,'no encontrado')"""


                   
                      


def encontrar (a,lista):
    for l in lista:
	    if l == a:
		    print("elemento encontrado")
		    break 
		

lista = [1,2,3,4]
a = 2
encontrar(a,lista)


# para saber la posición de un elemento en la tupla se utiliza el metodo .index(), o para contar cuantas veces se repite un 
# elemento en la tupla se utiliza el metodo .count()

"""mi_tupla = (1,1,2,'Hola',False,5,'Ciudad')
elemento = mi_tupla.index('Ciudad')
print (elemento) 
veces = mi_tupla.count(1)
print(veces)"""

#conjuntos: son colecciones desordenadas q se inicializan con el metodo .set(), y se agregan elemento con el 
#método .add()
"""conjunto = set()
conjunto = {1,2,3,'a','B'}
print(conjunto)
conjunto.add(0)
conjunto.add(2.5)
conjunto.add('A')
print(conjunto)"""
#se usa el metodo discard() para eliminar un elemento del conjunto 
#los conjuntos no admiten valores reptidos, ademas se puede puede buscar el elemento en el conjunto 
# elemento in conjunto

"""con = {'Santy','Michu',1,2,'Luis'}

print('Santy' in con)
print('michu' in con)

con1 = {1,1,1,1,1,1,}
print(con1)

#el metodo set() ayuda a crear un conjunto a partir de una lista 

lis = [33,11,22,11,33,44,44]
print(lis)
#casteo para transformar la lista en conjunto con el metodo set(), asi ya no habrá elementos duplicados

c1 = set(lis)
print(c1)

#de manera inversa se utiliza el metodo list() para transformar el conjunto a una lista

lis = list(c1)
print(lis)

s = "Al pan pan y al vino vino"
l=list(set(s))
print(l)"""

#diccionarios para 
"""lis = [1,2,3]
dic = {1:'uno','amarillo':'yellow',2:'tres',0:'False'}
d = 5
#para saber a que clase pertenece la variable se usa type()

print(type(dic), type(lis), type(d))

print(dic)
dic[2]='dos'
print(dic)
#se usa el metodo del() para borrar un elemento en un diccionario y de una lista tmbn 
del(dic[0])
print(dic)

print(lis)
del(lis[0])
print(lis)

#recorriendo el diccionario 
for d in dic:
	print(d,dic[d])


#otra forma de recorrer el diccionario utilizando el metodo .items()

for clave, valor in dic.items():
	print(clave,valor)


#Utilizando listas se puede guardar diccionarios en ellas 

lenguajes = []

l = {'Nombre':'Java', 'IDE':'NETBEANS', 'Año':1998}
lenguajes.append(l)

l = {'Nombre':'TRANSACSQL', 'IDE':'SQLServer', 'Año':2000}
lenguajes.append(l)

l = {'Nombre':'JavaScript', 'IDE':'VCode', 'Año':1998}
lenguajes.append(l)

print(lenguajes)

for l1 in lenguajes:
	print(l1['Nombre'],l1['IDE'],l1['Año'])



for l2 in lenguajes:
	for c,v in l2.items():
		print(c,v)"""
		



#PILAS Y COLAS 

pila = []

#rellenamos la lista con el .append()

pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)

print(pila)

#para sacar el ultimo elemento de la pila usamos el metodo .pop()

n = pila.pop()
print(pila,n)
n = pila.pop()
print(pila,n)
n = pila.pop()
print(pila,n)
n = pila.pop()
print(pila,n)

#COLAS
#primero se importa el modulo (o libreria) deque del paquete collections

from collections import deque  

mi_cola = deque()
print(mi_cola)

#para añadir elementos a la cola se utiliza el metodo append()

mi_cola.append('Santy')
mi_cola.append('Michu')
mi_cola.append('Luis')
mi_cola.append('gomez')

print(mi_cola)

#para sacar un elemento de la cola se utiliza el metodo popleft()

n=mi_cola.popleft()
print(mi_cola,n)
n=mi_cola.popleft()
print(mi_cola,n)
n=mi_cola.popleft()
print(mi_cola,n)
