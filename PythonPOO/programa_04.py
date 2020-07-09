class Coche:

	def __init__(self):
		print("Constructor de Coche")

	def acelerar(self):
		print("Acelerar")

	def frenar(self):
		print("Frenar")

class CocheRojo(Coche):

	def __init__(self):
		print("Constructor de CocheRojo")

objeto = Coche()
objeto.acelerar()
objeto.frenar()

objetoCocheRojo = CocheRojo()
objetoCocheRojo.acelerar()
objetoCocheRojo.frenar
