###-----------------------------
###Ejemplo: ocultamiento de la implementación
###-----------------------------

class Carrera:
	def __init__(self, nombre):
			self.nombre = nombre
			self.materias = {}


#Ocultar la implementación de una colección implementando un método propio para agregar elementos
	def agregarMateria(self, materia, codigo):
			self.materias[codigo] = materia


class Materia:
  def __init__(self, nombre, profesor):
      self.nombre = nombre
      self.profesor = profesor

# instanciar objeto Carrera
ing = Carrera("Ingeniería")

# instanciar un objeto Materia
algebra=Materia("Álgebra", "Ricardo Quinteros")
fisica=Materia("Física", "Margarita Gomez")
quimica=Materia("Química", "Lorena Ríos")

# para agregar materias a una tupla []
#print(ing.materias.append((134, algebra)) )
#print(ing.materias.append((412, fisica)) )

print( ing.materias)

#Ejemplo donde agregar elemento implica conocer la implementación de la colección
ing.materias[134]=algebra
ing.materias[412]=fisica

#Ejemplo donde se oculta la implementación de la colección
ing.agregarMateria(algebra, 134)
ing.agregarMateria(fisica, 412)

ing.agregarMateria(algebra, 134)