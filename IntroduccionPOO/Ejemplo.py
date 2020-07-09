class Ejemplo:
	
    def __init__(self, parámetro1, parámetro2):
        self.atributo1=parámetro1
        self.atributo2=parámetro2

#instanciar un objeto pasando argumentos al constructor
un_ejemplo=Ejemplo("un valor", "otro valor")

#imprimir valor de un atributo
print(un_ejemplo.atributo1)
