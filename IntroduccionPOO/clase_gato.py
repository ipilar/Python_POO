###----------------------------------------
###Ejemplo: implementación de la clase Gato
###----------------------------------------

class Gato:

	#atributo de clase
	especie = "mamifero"

	def __init__(self, nombre, edad):
		self.nombre=nombre
		self.edad=edad
		self.alimentos=[] 

	def esAdulto(self):
		if self.edad > 1:
			print(self.nombre, "es adulto")
		else:
			print(self.nombre, "es cachorro")

	def esAlimentoFavorito(self,alimento):
		return alimento in self.alimentos


#Instanciar un objeto Gato   
miGato=Gato("Pelusa",1)

#Imprimir un atributo
print(miGato.nombre)