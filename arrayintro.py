lista=[5,5,6,9]
numero=5
decimal=65.1

print(type(numero))
print(type(decimal))
print(type(lista))

tipoTupla=(4,5,6,7,) #No se puede modificar
print(tipoTupla)
print(type(tipoTupla))

tipoLista=["julio",19,"aries",1.60]
tipoLista2=[9,14,3,1,15]
print(sorted(tipoLista2))

print(f'El nombre del usuario es {tipoLista[0]} tiene {tipoLista[1]} años, su signo es {tipoLista[2]} y mide {tipoLista[3]}')

tipoLista.append(input("Escribe tu nuevo signo"))
print(tipoLista)