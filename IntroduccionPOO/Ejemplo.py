class Ejemplo:
	def __init__(self, parametro1, parametro2):
		
		self.atributo1 = parametro1
		self.atributo2 = parametro2

#instanciar un objeto pasando argumentos al constructor
un_ejemplo=Ejemplo("un valor", "otro valor")

#imprimir valor de un atributo
print(un_ejemplo.atributo1)

# imprimir otro valor de un Atributo
print(un_ejemplo.atributo2)