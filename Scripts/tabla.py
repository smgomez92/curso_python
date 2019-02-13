import sys 
if len(sys.argv) == 3:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    if arg1 > 0 and arg1 < 10 and arg2 > 0 and arg2 < 10:
    	for i in range(arg1):
    		for j in range(arg2):
    			print("* ",end="")

    		print("")
    else:
    	print("los números ingresados deben estar dentro del rango 1-9")
else:
    print("No se ingresaron parámetros")
    print("Ejemplo tabla.py 3 4")    		
       	   
	