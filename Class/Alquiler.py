__author__ = 'jor'

class alquiler:
    matricula=""
    nif=""
    fecha_alquiler=""
    fecha_debolucion=""
    importe=""
    completada=False
    def __init__(self,matricula,nif, fecha_alquiler,fecha_debolucion,importe,completada):
        self.matricula=matricula
        self.nif=nif
        self.fecha_alquiler=fecha_alquiler
        self.fecha_debolucion=fecha_debolucion
        self.importe=importe
        self.completada=completada



    def getMatricula(self):
        return self.matricula

    def getNif(self):
        return self.nif

    def getFecha_alquiler(self):
        return self.fecha_alquiler

    def getFecha_debolucion(self):
        return self.fecha_debolucion

    def getImporte(self):
        return self.importe

    def getCompletada(self):
        return self.completada



