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

#Cambiar un atributo e imprimir
miGato.nombre="Pelusita"
print(miGato.nombre)

#Agregar un atributo de forma dinámica e imprimirlo
miGato.raza="Siamés"
print(miGato.raza)

#Agregar elementos a una lista que es atributo de un objeto
miGato.alimentos.append("pescado")
miGato.alimentos.append("leche")
print(miGato.alimentos)

#Modificar la lista que es atributo de un objeto
miGato.alimentos=["leche", "galletas"]
print(miGato.alimentos)

#Invocar un método de un objeto
miGato.esAdulto()
miGato.edad=2
miGato.esAdulto()

#Instanciar otro objeto de la misma clase
otroGato=Gato("Cleo",3)

#Guardar una lista en un atributo
otroGato.alimentos=["pescado","pan"]

#Invocar al mismo método en distintos objetos
print(miGato.esAlimentoFavorito("leche"))
print(otroGato.esAlimentoFavorito("leche"))

#Acceder a atributo de clase de un objeto
print(miGato.especie)

#Acceder a atributo de clase sin instanciar objetos
print(Gato.especie)