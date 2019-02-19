#sirve para copiar objetos 
import copy

class Producto():
	def __init__(self,referencia,nombre,pvp,descripcion):
		self.referencia = referencia
		self.nombre = nombre
		self.pvp = pvp
		self.descripcion = descripcion

	def __str__(self):
		return """\
Referencia:\t {}
Nombre:\t\t {}
P.V.P.:\t\t {}
Descripción: {}
		""".format(self.referencia,self.nombre,self.pvp,self.descripcion)


#El argumento 'Producto' nos indica q estamos heredando de producto o q Adorno es 'hija' de producto 
class Adorno(Producto):
	pass

class Alimento(Producto):
	productor = ""
	distribuidor = ""
	def __str__(self):
		return """\
Referencia:\t  {}
Nombre:\t\t  {}
P.V.P.:\t\t  {}
Descripción:  {}
Productor:\t  {}
Distribuidor: {}
		""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)

class Libro(Producto):
	isbn = ""
	autor = ""

	def __str__(self):
		return """\
Referencia:\t  {}
Nombre:\t\t  {}
P.V.P.:\t\t  {}
Descripción:  {}
ISBN:\t\t  {}
Autor:\t\t  {}
		""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)

 

a = Adorno(201,"Adorno", 0.50, "Adorno para la sala")
al = Alimento(2010,"Aceite",1.00,"Aceite de oliva")
al.distribuidor = "SA"
al.productor = "pre"
li = Libro(202,"Libro",5.00,"Novela")
li.isbn = "1-00-123"
li.autor = "Don Juan"

productos = [a,al]
productos.append(li)

# isinstance nos ayuda a saber a que clase pertenece la instancia
for p in productos:
	if isinstance(p,Adorno):
		print(p.nombre,p.descripcion)
	elif isinstance(p,Alimento):
		print(p.nombre,p.distribuidor,p.productor)
	elif isinstance(p,Libro):
		print(p.nombre,p.isbn,p.autor)


print()
li_c = copy.copy(li)
li_c.autor = "don juancho"
#se utiliza el metodo copy del modulo copy ya que no se puede copiar los objetos asignandolos a otras variables 
#ya que al modificar su copia tmbn se modifica el original (paso de referencia como parametro )
print(li)
print(li_c)