###-----------------------------
###Ejemplo: herencia de clases
###-----------------------------

class Empleado:

  def __init__(self, nombre, edad, registro, sueldo):
        self.nombre=nombre
        self.edad=edad
        self.registro=registro
        self.sueldoBase=sueldo
    
  def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase - descuentos + bonos

#Reimplementación de método __init__ llamando al de la superclase
class AgenteVentas(Empleado):
  def __init__(self, nombre, edad, registro, sueldo, mostrador):
        self.numeroMostrador = mostrador
        super().__init__(nombre, edad, registro, sueldo)

#Instanciar objeto de subclase
pedro=AgenteVentas("Pedro Martinez", 32, "A120", 55000, 4)

#Atributo heredado de la superclase
print(pedro.nombre)

#Método heredado de la superclase
print(pedro.calcularSueldo(100, 3000))
