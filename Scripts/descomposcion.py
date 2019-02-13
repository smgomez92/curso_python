import sys 
if len(sys.argv) == 2:
	numero = int(sys.argv[1])
	if numero < 0 or numero > 10000:
		print("Error - el argumento es incorrecto")
		print("Ejemplo: descomposicio.py [1 - 9999]")
	else:
		cadena = str(numero)
		longitud = len (cadena)

		for i in range(longitud):
			print("{:04d}".format(int(cadena[longitud - 1 - i]) * 10 ** i))
else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: descomposicio.py [1 - 9999]")
		