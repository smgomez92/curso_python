class Galleta():
	chocolate = False
	
	#el método init se ejecuta cuando se crea una instancia de la clase (parecido al metodo constructor en java)
	#la palabra reservada self hace referencia al mismo objeto, y sirve para diferenciar entre el ámbito de clase 
	#y el de un método (parecido a this en java)
	def __init__ (self,marca = None):
		self.marca = marca 
		print("galleta creada")

	#No hay necesidad de metodos get y set .. 
	def setChocolate(self,choco):
		self.chocolate = choco

	def setMarca(self,mar):
		self.marca = mar
	
#la función type nos indica el tipo de dato al que pertenece el parámetro que le pasemos 
#print(type(galleta1))
#print(galleta1.sabor)


"""galleta1 = Galleta("Oreo")
galleta2 = Galleta("Ducales")
galleta3 = Galleta()
galleta1.setChocolate(choco=True)
print(galleta1.chocolate,galleta1.marca)
print(galleta2.chocolate,galleta2.marca)
galleta2.setMarca("Universal")
print(galleta2.chocolate,galleta2.marca)
galleta1.marca = "Otra Marca sin set :v"

print(galleta1.chocolate,galleta1.marca)"""

class Persona:
	#constructor de la clase
	def __init__(self,nombre,apellido,ced):
		self.nombre = nombre
		self.apellido = apellido
		self.ced = ced 
		#METODOS ESPECIALES
	#metodo destructor de la clase sirve para borrar la instancia o escribir alguna sentencia antes de eliminar
    #la instancia
    def __del__(self):
     #   print("se borró a",self.nombre)"""
     #el metodo estring para mostrar el objeto en forma de string 
    def __str__(self):
    	#return "[nombre = {},apellido = {},ced = {},]".format(self.nombre,self.apellido,self.ced)
    def __len__(self):
    		return algo

        


persona1 = Persona("Santiago","Gómez",172167884) 

#Encapsulacion de atributos se utiliza la sintaxis __nombre_atributo q simula el modificador de acceso private

class Carros:
	__placa = "sssssssssssssss"

	def __metodo_privado(self):
		print("Método privado")

	def  placa(self):
		return self.__placa

	def getMetodo(self):
		self.__metodo_privado()
	
c = Carros()
placa = c.placa()
print(placa)
c.getMetodo()




