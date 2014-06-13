__author__ = 'jor'
class coche:
    matricula=""
    marca=""
    modelo=""
    precio_dia=""
    disponible = False

    def __init__(self,matricula,marca,modelo,precio_dia,disponible):
            self.matricula=matricula
            self.marca=marca
            self.modelo=modelo
            self.precio_dia=precio_dia
            self.disponible = disponible

    def getMatricula(self):
        return self.matricula
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getPrecio_dia(self):
        return self.precio_dia
    def getDisponible(self):
        return self.disponible



    def setDisponible(self,disponible):
        self.disponible=disponible
    def setPrecio_dia(self,precio_dia):
        self.precio_dia=precio_dia

