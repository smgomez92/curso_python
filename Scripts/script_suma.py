#-*- coding: utf-8 *-*
#suma de dos números 
import sys
import mi_paquete.mis_funciones as fun 

if len(sys.argv) == 3:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    resultado = fun.suma(num1,num2)
    #forma de presentar los datos ordenados 
    print("La suma de {} + {} es: {}".format(num1,num2,resultado))
        
else:
	print("No se le pasó argumentos")
	print("Ejemplo script_suma.py 2 3")








