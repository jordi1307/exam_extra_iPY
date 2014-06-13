__author__ = 'jor'
import datetime
import re
def main():
    #nif=input("Cliente Identifiquese ,con su nif")
    nif="47179315J"
    if nif=="":
        print("se creara un nuebo cliente:")

        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        nifcli=input("Nif: ")

        clien=cliente(nombre,apellido,nifcli)
        clien.seif()


    else:
        cli=""
        print(nif)
        with open('clientes.txt', mode='r',encoding ='utf-8') as clientes:

                aux2=clientes.read()
                aux=aux2.split(";")
                clien=cliente(aux[0],aux[1],aux[2])
               # print("buscan")
                #print(clien.getNif())
                #if clien.getNif() ==nif.strip():
                #    print("hola")
                cli=clien



        cli.Alquilar()


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

    def Alquilar(self):#1.2.1

        matricula=input("inserte matricula del coche a alquilar")
        with open('veiculos.txt', mode='r',encoding ='utf-8') as veiculos:
            	for veiculo in veiculos:
                    print(veiculo)

                    veic=veiculo.split(";", 5)

                    for a in veic:
                        print(a)
                    cochet=coche(veic[0],veic[1],veic[2],veic[3],veic[4])
                    print(cochet.getDisponible(matricula))
                    if cochet.getDisponible(matricula)==str(True):
                       fecha_debolucion=input("que dia debolbera el beiculo?")
                       num=input("numero de dias")


                       tramite=alquiler(matricula,self.getNif(),datetime.datetime.now().strftime('%d/%m/%Y'),fecha_debolucion,cochet.getPrecio_dia(),False)
                       tramite.seif()
                       cochet.setDisponible("False")
                       cochet.seif()

    def SercarCochesDisponibles(self):
          with open('veiculos.txt', mode='w',encoding ='utf-8') as veiculos:#1.2.2
            	for veiculo in veiculos:
                    veic=veiculo.split(";")

                    cochet=Coche.coche(veic[0],veic[1],veic[2],veic[3],veic[4],veic[5])
                    if cochet.getDisponible()==True:
                        print("Coche:\n"
                              "\tMatricula: % \n"
                              "\tMarca: %\n"
                              "\tModelo: %\n"
                              "\tPrecio por dia: %\n"
                              "\tDisponible: %\n"
                                % cochet.getMatricula(),
                                 cochet.getMarca(),
                                 cochet.getModelo(),
                                 cochet.getPrecio_dia())

    def SercarCochesEnLloger(self):#1.2.3
          with open('veiculos.txt', mode='w',encoding ='utf-8') as veiculos:
            	for veiculo in veiculos:
                    veic=veiculo.split(";")

                    cochet=Coche.coche(veic[0],veic[1],veic[2],veic[3],veic[4],veic[5])
                    if cochet.getDisponible()==False:
                        print("Coche:\n"
                              "\tMatricula: % \n"
                              "\tMarca: %\n"
                              "\tModelo: %\n"
                              "\tPrecio por dia: %\n"
                              "\tDisponible: %\n"
                                % cochet.getMatricula(),
                                 cochet.getMarca(),
                                 cochet.getModelo(),
                                 cochet.getPrecio_dia())
    def ToString(self):
        return self.getNombre()+";"+self.getApellido()+";"+self.getNif()
    def seif(self):
          with open('clientes.txt', mode='a',encoding ='utf-8') as clientes:
             clientes.write("\n"+self.ToString())
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
        print("seif alquiler")
        with open('alquiler.txt', mode='a',encoding ='utf-8') as f_alquiler:
             f_alquiler.write(self.ToString())






main()