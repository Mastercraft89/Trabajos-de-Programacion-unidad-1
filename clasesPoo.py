class TortugasNinja:
    #atributos/Propiedades
    poderAtaque=100
    poderDefensa=90
    agilidad=100
    puntosVida=200
    vidas=3
    velocidad=300
    arma=""
    poderAtaqueM=80
    poderDefensaM=100
    agilidadM=150
    puntosVidaM=200
    vidas=3
    velocidadM=350
    armaM=""

    #Metodos
    def ataque(self):
        print("Ataque")
    
    def defensa(self):
        print("Defiendo")

#objeto
donatello=TortugasNinja()
donatello.arma="palo"
print(f'el poder de ataque de donatello es:{donatello.poderAtaque} y su arma es un {donatello.arma}')

enemigoCerca=input("¿esta destructor cerca?")
if enemigoCerca=="si":
    donatello.defensa()

#objeto
miguelangel=TortugasNinja()
miguelangel.armaM="ninshacos"
print(f'el poder de ataque de miguelangel es:{miguelangel.poderAtaqueM} y su arma es un {miguelangel.armaM}')

enemigoCerca=input("¿esta destructor cerca?")
if enemigoCerca=="si":
    miguelangel.defensa()