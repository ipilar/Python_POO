"""
POO con Python
1.- Paradigma de Programación
2.- Todo es un objeto
3.- Clases (Atributos o propiedades - Métodos)
4.- Objetos

Objeto: una entidad que se quiere representar pero no es suficiente con una variable de los tipos mas básicos (int, float, bool,..)
Por ejemeplo: un sistema de ventas podemos tener
objetos como el vendedor, un articulo, una venta
y objetos mas complejos y otros objetos pueden ser por ejemplo una ventana.

Atributos: caracterisitcas propias que lo definen
Métodos: acciones a realizar.

CLASE
-----
"Molde" para obtener objetos con la misma
estructura. Para obtener un objeto a partir de	una clase se le debe instanciar.

Objetos de la misma clase: tienen los mismos
metodos y atributos, pero los atributos pueden
tener distintos valores o estados.


class Gato:
	pass

mi_gato = Gato()

Representado por los atributos: nombre, edad,
alimentos favoritos.
Métodos: saber si es adulto, decir si un alimento es de sus favoritos

ATRIBUTOS
---------
Propiedades del objeto, representadas mediante
variables. 
Pueden ser de cualquier tipo de dato (incluso otros objetos).
"De Clase" o "de instancia", segun si el 
valor es el mismo para todos los objetos o no. 
Pueden crearse de forma dinamica durante la ejecucion.

Atributos de Clase: o atributos estaticos son compartidos para todos los objetos de una misma clase. Se pueden leer y utilizar sin necesidad de una instancia.

Atributos de Instancia:

METODOS
-------
Dan funcionalidad a los Objetos.
Necesitan de una clase para existir.
Similares a las funciones (con algoritmos, parametros y valor de retorno).
Puede invocarse desde el propio objeto que 
lo contiene o desde otro, con la sintaxis
objeto.metodo()

Constructor es un metodo especial: istancia objetos de una clase (se invoca automaticamente)
En el pueden inicializarse los atributos de un objeto.
No es obligatorio crealo ni inicializar todos los atributos.


"""

