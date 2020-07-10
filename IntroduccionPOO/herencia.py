###-----------------------------
###Ejemplo: herencia de clases
###-----------------------------

class Empleado:

  def __init__(self, nombre, edad, registro, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.registro = registro
        self.sueldoBase = sueldo
    
  def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase - descuentos + bonos

class AgenteVentas(Empleado):
#Reimplementación de método __init__ en la subclase
	def __init__(self, mostrador):
		self.numeroMostrador = mostrador

#Instanciar objeto de subclase
pedro = AgenteVentas(4)
print(pedro.numeroMostrador)

#Atributo de superclase no existe
print(pedro.nombre)

