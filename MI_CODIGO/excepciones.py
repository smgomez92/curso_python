#las excepcines se escriben asi 
"""try:
	pass
except Exception as e:
	print( type(e).__name__ )
	rise //para invocar un error, parecido al throw exception para luego capturarlo 

else:
	pass
finally:
	pass"""
a = 2
b = 0
"""try:
    c = a/b
except Exception as e:
    print( type(e).__name__ )"""
			
		
def division(a,b):
	if b == 0:
		raise ZeroDivisionError()
	else:
		print(a/b)

try:
	division(a,b)
except ZeroDivisionError:
	print("No se puede dividir para cero")
	



		
	

 














	



