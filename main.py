#IMPORTANDO LA CLASE
from Personaje import Personaje

#Utilizar una clase
#Para utilizar una clase CREO UN OBJETO
#UN OBJETO es una VARIABLE que HEREDA los atributos y metodos de la clase
personaje = Personaje("Batman","Negro","Heroe")

#ACCEDER A LOS ATRIBUTOS DE MI OBJETO
print(personaje.nombre)

#ACCEDER A LOS METODOS DE MI OBJETO
personaje.saludar()




