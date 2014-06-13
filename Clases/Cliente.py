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
        with open('veiculos.txt', mode='r',encoding ='utf-8') as veiculos:
            	for veiculo in veiculos:
                    print(veiculo)

                    veic=veiculo.split(";", 5)

                    for a in veic:
                        print(a)
                    cochet=Coche.coche(veic[0],veic[1],veic[2],veic[3],veic[4])
                    print(cochet.getDisponible(matricula))
                    if cochet.getDisponible(matricula)==str(True):
                       fecha_debolucion=input("que dia debolbera el beiculo?")
                       num=input("numero de dias")


                       tramite=Alquiler.alquiler(matricula,self.getNif(),datetime.datetime.now().strftime('%d/%m/%Y'),fecha_debolucion,cochet.getPrecio_dia(),False)
                       tramite.seif()
                       cochet.setDisponible("False")
                       cochet.seif()

    def SercarCochesDisponibles(self):
        with open('veiculos.txt', mode='r',encoding ='utf-8') as veiculos:
            print(veiculos)
            for veiculo in veiculos:
                veic=veiculo.split(";")

                cochet=Coche.coche.__init__(veic[0],veic[1],veic[2],veic[3],veic[4],veic[5])
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

                    cochet=Coche.coche.__init__(veic[0],veic[1],veic[2],veic[3],veic[4],veic[5])
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

#clien=cliente("jordi","luesma","47179315J")
#clien.seif()

#print(clien.getNombre())
#print(clien.getApellido())
#print(clien.getNif())

#print(clien.ToString())
#clien.Alquilar()
#clien.SercarCochesDisponibles()