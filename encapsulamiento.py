class Vehiculos:
    #atributos
    #marca,modelo,año,color,numeerodeserie
    def __init__(self,marca,modelo,año,color,numerodeserie,tipomotor):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.color=color
        self.__numerodeserie=numerodeserie  #encapsular
        self.__tipomotor=tipomotor

    def __verificarTenencia(self):
        if self.año>=2010:
            return True
        else:
            return False

    def costoTenencia(self):
        if self.__verificarTenencia():
            return 1000*1.5
        else:
            return "no paga tenencia"

    def avanzar(self):
        print("Estoy avanzando")
    
    def frenando(self):
        print("Estoy frenando")

    def detenerse(Self):
        print("Estoy en un semaforo")
    
    def presentar(self):
        print(f"El carro {self.modelo} de la marca {self.marca}, del año {self.año}, es {self.color}, con numero de serie {self.__numerodeserie} y su tipo de motor es {self.__tipomotor}")

    def getnumerodeserie(self):
        print(self.__numerodeserie)

    def gettipomotor(self):
        print(self.__tipomotor)

caropips=Vehiculos("Toyota","Corolla",2021,"blanco","X0001","Gasolina")
caropips.presentar()
print("---------------------")
#caropips.__numerodeserie="x0003"
#print(caropips.__numerodeserie)
#caropips.getnumerodeserie()
#caropips.gettipomotor()
#print(caropips.verificarTenencia())
print(caropips.costoTenencia())
print("el costo de la tenecia es:" )

