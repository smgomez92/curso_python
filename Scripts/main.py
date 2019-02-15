import funcion.funciones as f
import Clase as per
"""a1 = 2
b1 = 3

if f.comparar(a1,b1) > 0:
	print("El número {} es mas grande que el numero {}".format(a1,b1))
else:
	print("El número {} es mas grande que el numero {}".format(b1,a1))


a = "HOLA"
b = "HOLA"

if f.cadenas_iguales(a,b):
	print("la cadena {} es igual a la cadena {}".format(a,b))
else:
	print("la cadena {} NO es igual a la cadena {}".format(a,b))


[s,r,m,d,b]=f.operaciones(1,2)

print(s,r,m,d,b)

lista=f.lista()

print(f.lista()[1:4])"""

"""#paso de valores por referencia, dice que: si pasamos una lista coleccion conjunto o diccionario como 
#paramatero de una funcion si los valores de esa lista cambian tmbn cambiarán externamente esto nos 
#perjudicaria si queremos mantener los valores de la lista para futuros calculos 

def doblar_valor (lista):
	
	for i,n in enumerate(lista):
		lista[i] *=2
    
   
	
#afecta externamente a la lista pese a q le pasamos como parámetro		
lista1 = f.lista()
print(lista1)
doblar_valor(lista1)
print(lista1)

#para solucionar esto se puede realizar esto
lista1 = f.lista()
print(lista1)
doblar_valor(lista1[:])
print(lista1)"""

"""
a=1000
b = 0.5
d = {'hola':2*2,'m':2/1,'d':a/b}

for x in d:
	print(x,d[x])
	pass"""

print(per.calculo_area(h=10,b=15))