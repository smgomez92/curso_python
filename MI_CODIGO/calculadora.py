import mi_paquete.mis_funciones as fun 

print("\t**** CALCULADORA DE DOS NUMEROS ****")
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))

while True:
    print("""¿Qué deseas hacer?
             1.- Sumar
             2.- Restar
             3.- Multriplicar
             4.- Dividir\n""")
    print("Ingresa una opci�n")
    opcion = input() 
    if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4' :
                   res = fun.operaciones(a=num1,b=num2,opcion=opcion)
                   print ('El resultado es: ',res)
                   break
    else:
        print("Esa opción NO es válida ")