
class TortugasNinja:
    #atributos/Propiedades
    def __init__(self,nombre,ataque,defensa,arma,vida,vidas):
        self.ataque=ataque
        self.defensa=defensa
        self.arma=arma
        self.vida=vida
        self.vidas=vidas
        self.nombre=nombre

    #Metodos
    def ataque(self):
        print("Ataque")
    
    def defensa(self):
        print("Defiendo")

donatello=TortugasNinja("donatello",100,250,"palo",200,3)
print(f'{donatello.nombre} tiene {donatello.ataque} puntos de ataque y su arma es un {donatello.arma}')

miguel=TortugasNinja("miguel",120,150,"ninshacos",150,3)
print(f'{miguel.nombre} tiene {miguel.ataque} puntos de ataque y su arma es un {miguel.arma}')

leo=TortugasNinja("leo",300,200,"espada",300,3)
print(f'{leo.nombre} tiene {leo.ataque} puntos de ataque y su arma es una {leo.arma}')

rafael=TortugasNinja("rafael",320,400,"sai",200,3)
print(f'{rafael.nombre} tiene {rafael.ataque} puntos de ataque y su arma es un {rafael.arma}')
print("donatello y leo se enfrentan")
if donatello.ataque>leo.ataque:
    print("Gana donatello")

else:
    print("Gana leo")