class Personaje:

    #Constructor de la clase
    #Inicializa los atributos y metodos de mi clase
    def __init__(self,nombre,colorTraje,tipo):

        #ATRIBUTOS=DATOS=VARIABLES
        self.nombre = nombre
        self.colortraje = colorTraje
        self.tipo = tipo
    
    #METODOS=ACCIONES=FUNCIONES
    def saludar(self):
        print('Hola...')
