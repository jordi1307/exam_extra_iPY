__author__ = 'jor'
import Coche
import Alquiler
import datetime
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
        with open('veiculos.txt', mode='w',encoding ='utf-8') as veiculos:
            	for veiculo in veiculos:
                    veic=veiculo.split(";")
    #matricula=""
    #marca=""
    #modelo=""
    #precio_dia=""
    #disponible = False
                    Coche.coche.__init__(veic[0],veic[1],veic[2],veic[3],veic[4],veic[5])
                    if Coche.coche.getDisponible(matricula)==True:
                        fecha_debolucion=input("que dia debolbera el beiculo?")
                        num=input("numero de dias")
                        importe=num*Coche.coche.getPrecio_dia()
    #matricula=""
    #nif=""
    #fecha_alquiler=""
    #fecha_debolucion=""
    #importe=""
    #completada=False
                        Alquiler.alquiler.__init__(matricula,self.getNif(),datetime.datetime.now().strftime('%d/%m/%Y'),fecha_debolucion,importe,False)
                        Alquiler.alquiler.seif()
                        Coche.coche.setDisponible(False)
                        Coche.coche.seif()
    def SercarCochesDisponibles(self):
          with open('veiculos.txt', mode='w',encoding ='utf-8') as veiculos:#1.2.2
            	for veiculo in veiculos:
                    veic=veiculo.split(";")

                    Coche.coche.__init__(veic[0],veic[1],veic[2],veic[3],veic[4],veic[5])
                    if Coche.coche.getDisponible()==True:
                        print("Coche:\n"
                              "\tMatricula: % \n"
                              "\tMarca: %\n"
                              "\tModelo: %\n"
                              "\tPrecio por dia: %\n"
                              "\tDisponible: %\n"
                                % Coche.coche.getMatricula(),
                                 Coche.coche.getMarca(),
                                 Coche.coche.getModelo(),
                                 Coche.coche.getPrecio_dia())

    def SercarCochesEnLloger(self):#1.2.3
          with open('veiculos.txt', mode='w',encoding ='utf-8') as veiculos:
            	for veiculo in veiculos:
                    veic=veiculo.split(";")

                    Coche.coche.__init__(veic[0],veic[1],veic[2],veic[3],veic[4],veic[5])
                    if Coche.coche.getDisponible()==False:
                        print("Coche:\n"
                              "\tMatricula: % \n"
                              "\tMarca: %\n"
                              "\tModelo: %\n"
                              "\tPrecio por dia: %\n"
                              "\tDisponible: %\n"
                                % Coche.coche.getMatricula(),
                                 Coche.coche.getMarca(),
                                 Coche.coche.getModelo(),
                                 Coche.coche.getPrecio_dia())
    def ToString(self):
        return self.getNombre()+";"+self.getApellido()+";"+self.getNif()
    def seif(self):
          with open('clientes.txt', mode='a',encoding ='utf-8') as clientes:
             clientes.write("\n"+self.ToString())


