__author__ = 'jor'
import
class cliente:
    nombre=""
    apellido=""
    nif=""
    def __init__(self,nombre,apellido,nif):
        self.nombre=nombre
        self.apellido=apellido
        self.nif=nif


    def getNif(self):
        return self.nif
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def Alquilar(self):

        matricula=input("inserte matricula del coche a alquilar")

