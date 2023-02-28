class Animales:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print(f'\nAnimal Salvaje')

class Perro(Animales):
    def tipo_animal(self):
        print(f'\nanimal domestico\n')

nuevo_animal=Leon('Mufasa')
nuevo_animal.tipo_animal()

nuevo_animal=Perro('solovino')
nuevo_animal.tipo_animal()