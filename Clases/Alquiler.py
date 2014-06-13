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





    def setMatricula(self,matricula):
         self.matricula=matricula

    def setNif(self,nif):
         self.nif=nif

    def setFecha_alquiler(self,fecha_alquiler):
         self.fecha_alquiler=fecha_alquiler

    def setFecha_debolucion(self,fecha_debolucion):
         self.fecha_debolucion=fecha_debolucion

    def setImporte(self,importe):
         self.importe=importe

    def setCompletada(self,completada):
         self.completada=completada
    def ToString(self):
        return str(self.matricula)+";"+str(self.nif)+";"+str(self.fecha_alquiler)+";"+str(self.fecha_debolucion)+";"+str(self.importe)+";"+str(self.completada)
        
    def seif(self):
         with open('alquiler.txt', mode='a',encoding ='utf-8') as f_alquiler:
             f_alquiler.write(self.ToString())





