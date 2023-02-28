
def calculoPromedio(calificaciones):
    return(sum(calificaciones))/(len(calificaciones))

respuesta="si"
calificaciones=[]

while respuesta=="si":
    calificaciones.append(int(input("Escribe la calificacion del siguiente alumno :")))
    respuesta = input("Escriba si para seguir añadiendo numeros :")

    print(calificaciones)
promedio=calculoPromedio(calificaciones)
print(promedio)