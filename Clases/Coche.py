__author__ = 'jor'
import re
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
    def getDisponible(self,matricula):
        if matricula==self.matricula:
            return self.disponible




    def setDisponible(self,disponible):
        self.disponible=disponible
        self.seif()
    def setPrecio_dia(self,precio_dia):
        self.precio_dia=precio_dia
        self.seif()
    def ToString(self):
        return str(self.matricula)+";"+str(self.marca)+";"+str(self.modelo)+";"+str(self.precio_dia)+";"+str(self.disponible)

    def seif(self):

        with open('alquiler.txt', mode='r+',encoding ='utf-8') as f_alquiler:
             if re.search(f_alquiler.read(),self.matricula):
                 f_alquiler.write(self.ToString())
    def addCocha(self):#1.2.4
        with open('alquiler.txt', mode='a',encoding ='utf-8') as f_alquiler:
             if re.search(f_alquiler.read(),self.matricula):
                 f_alquiler.write("\n"+self.ToString())
