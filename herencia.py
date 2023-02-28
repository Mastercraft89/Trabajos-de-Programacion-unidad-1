
class Cazador:
    #atributos /propiedades
    def __init__(self,nombre,rango,espada):
        self.nombre=nombre
        self.rango=rango
        self.espada=espada

    #metodos
    def presenatar(self):
        print(f'Mi nombre es {self.nombre}, tengo el rango de {self.rango}, mi espada es {self.espada}')

class Pilar(Cazador):
    def __init__(self,nombre,rango,espada,respiracion,posturas,):
        super().__init__(nombre,rango,espada)
        self.respiracion = respiracion
        self.posturas = posturas

RangoBajo=Cazador("Tanjiro", "Mizumoto","Negra")
RangoBajo.presenatar()
print("--------------------------------------------------------------------------------")
himejima=Pilar("himejima","Pilar","Bola de picos y hacha","respiracion de la roca",5)
himejima.presenatar()
print(f'Mi respiracion es la {himejima.respiracion} y su numero de posturas es {himejima.posturas}')
