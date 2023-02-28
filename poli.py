class Animales:
    def hablar(self):
        pass

class Perro(Animales):
    def hablar(self):
        print("\nEl perro dice Guau!")

class Leon(Animales):
    def hablar(self):
        print("El leon dice Raurr!")

class Vaca(Animales):
    def hablar(self):
        print("La vaca dice Muuu!")


for animal in Perro(),Leon(),Vaca():
    animal.hablar()


