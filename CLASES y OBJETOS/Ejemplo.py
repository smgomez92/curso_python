import math
class Punto:
	def __init__(self,x = None,y = None):
		if x is None and y is None:
			self.x = 0
			self.y = 0 
		else:
			self.x=x
			self.y=y
    
	def __str__(self):
		return "P({},{})".format(self.x,self.y)

	def __del__(self):
		print("se borró",self)

	def cuadrante(self):
		if self.x > 0 and self.y > 0:
			print("El punto",self,"está en el 1er cuadrante")
		elif self.x < 0 and self.y > 0:
			print("El punto",self,"está en el 2do cuadrante")
		elif self.x < 0 and self.y < 0:
			print("El punto",self,"está en el 3er cuadrante")
		elif self.x == 0 and self.y == 0:
			print("El punto",self,"está en el origen")
		else:
			print("El punto",self,"está en el 4to cuadrante")

	def vector(self,punto2):
		x1 = punto2.x - self.x
		y1 = punto2.y - self.y
		v = Punto(x1,y1)
		return v 

	def distancia(self,punto2):
		x1 = (punto2.x - self.x)**2
		y1 = (punto2.y - self.y)**2

		d = math.sqrt(x1+y1)
		return d 





class Rectangulo:
	def __init__(self, inicial = Punto(),final = Punto()):
		self.inicial = inicial
		self.final = final

	def base(self):
		self.base = abs(self.final.x - self.inicial.x)
		print("La base del Rectangulo es {}".format(self.base))

	def altura(self):
		self.altura = abs(self.final.y - self.inicial.y)
		print("La altura del Rectangulo es {}".format(self.altura))

	def area(self):
		self.base = abs(self.final.x - self.inicial.x)
		self.altura = abs(self.final.y - self.inicial.y)
		print("El area del Rectangulo es {}".format(self.base*self.altura))


A = Punto(2,3)
B = Punto(5,5)
R = Rectangulo(inicial=A,final=B)
R.base()
R.altura()
R.area()






"""punto1 = Punto()
punto2 = Punto(2,3)
punto3 = Punto(5,5)
print(punto1.cuadrante())
print(punto2.cuadrante())
print("Vector resultante",punto2.vector(punto2=punto3))
print("La distancia entre",punto3,"y",punto2,"es:",punto2.distancia(punto2=punto3))"""
#del(punto2)