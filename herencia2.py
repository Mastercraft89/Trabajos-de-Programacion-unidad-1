class Persona:      #Clase padre
    def __init__(self,nombre,apellido):
        #atributos
        self.nombre=nombre
        self.apellido=apellido

        #metodos
    def saludar(self):
        return f'Soy {self.nombre} {self.apellido}'
    
class Profesor(Persona):
    #atributos
    def __init__(self,nombre,apellido,edad,carrera):
        super().__init__(nombre,apellido)
        self.edad=edad
        self.carrera=carrera
    #metodos
    def saludarProfe(self):
        return f'Soy el profe {self.nombre} {self.apellido} tengo {self.edad} y soy de la carrera de {self.carrera}'
        
class alumno(Profesor):
    #atributos
    def __init__(self,nombre,apellido,edad,carrera,numerodecontrol,sexo):
        super().__init__(nombre,apellido,edad,carrera)
        self.numerosdecontrol=numerodecontrol
        self.sexo=sexo
    #metodos
    def saludaralumno(self):
        return f'Soy el estudiante {self.nombre} {self.apellido} tengo {self.edad} y soy de la carrera de {self.carrera}, mi numero de control es {self.numerosdecontrol} y mi sexo es {self.sexo}'

julionavarro=Persona("Julio","Navarro")
print(julionavarro.saludar())
print("-------------------------------------------------")
profePips=Profesor("Pips","Vazquez", 30, "diseño digital")
print(profePips.saludarProfe())
print("----------------------------------------------------")
Alumno=alumno("julio","Navarro",19,"Ingeneria Electronica",21560165,"masculino")
print(Alumno.saludaralumno())

