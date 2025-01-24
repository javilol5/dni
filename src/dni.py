#from tablaAsignacion import TablaAsignacion
#from class_bcolors_enum import Colors
import random

class Dni:

    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.letraSana = False
        # Composición (agregación) "Has - a" / "Tiene - un"
        #self.tabla = TablaAsignacion()

    def get_numero(self):

        return int(self.dni[:-1])
    
    def get_letra(self):

        return str(self.dni[-1])
    
    def asignar_letra(self):

        resto = int(self.dni) % 23
        letra = 'TRWAGMYFPDXBNJZSQVHLCKE'[resto]
        return self.dni + letra
    
    def comprobar_letra(self):

        if self.dni[-1] == 'TRWAGMYFPDXBNJZSQVHLCKE'[(int(self.dni[:-1]) % 23)]:
            return True
        else:
            return False
        
    def creacion_dni(self):
        numero = random.randint(1, 99999999)
        numero = str(numero)
        while len(numero) < 8:
            numero = '0' + numero
        numero = numero + 'TRWAGMYFPDXBNJZSQVHLCKE'[(int(numero) % 23)]
        return numero

       