import sys 
if len(sys.argv) == 3:
	num1 = int(sys.args[1])
	num2 = int(sys.args[2])
	longitud = num2 - num1
	p = 0
	p1 = 0
	for x in range(longitud):
		if (x % 2) == 0:
			p += 1
		else:
			p1 += 1

    print("Hay {} números entre {} y {}".format(longitud,num1,num2))  
    print("De los cuales {} son pares y {} son impares {}".format(p,p1))
else:
	print("Error - Argumentos incorrectos")
    print("Ejemplo: numeros.py [1 - 9999]")
    



