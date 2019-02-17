import mi_paquete.mis_funciones as fun 


def calculadora():
    print("\t**** CALCULADORA DE DOS NUMEROS ****")
    num1=fun.validar()
    num2=fun.validar()
    while True:
      print("""¿Qué deseas hacer?\n
               1.- Sumar
               2.- Restar
               3.- Multriplicar
               4.- Dividir\n""")
      print("Ingresa una opción")
      opcion = input() 
      if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4' :
                     print(fun.operaciones(a=num1,b=num2,opcion=opcion),"\n")
                     print("""\n SEGUIR CALCULANDO?
                  1.- SI
                  2.- Salir\n""")
                     opcion = input()
                     if opcion == '1':
                        calculadora() 
                     else:
                        print("Saliendo.... ")
                        exit()                     
      else:
          print("Esa opción NO es válida ")

      



calculadora()




