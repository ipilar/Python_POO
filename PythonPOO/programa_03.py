class VariablesGlobales:

	nombre= ""

	def __init__(self, nombre):
			self.nombre = nombre

	def getNombre(self):
		print(self.nombre)

objeto = VariablesGlobales("Isabel")
objeto.getNombre()


