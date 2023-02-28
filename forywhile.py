'''
while:se ejecuta mientras la condicion sea verdadera (TRUE)


si quiero un while se comporte como un for
contador 

for: el numero de repeticiones es finita, la cantidad de repeticiones

break: romper el ciclo'''
import turtle
turtle.shape("turtle")
programa = input("Escribe si para graficar o no para no graficar")

while programa == "si":
    print('''selecciona la figura que quieres graficar
    1) para trinagulo
    2) para cuadrado 
    3) para pentagono''')
    opcion = int(input())
    print(f'la opcion elegida es {opcion}')
    if opcion == 1: #triangulo 
        grados = 360/3
        turtle.forward(100)
        turtle.right(grados)
        turtle.forward(100)
        turtle.right(grados)
        turtle.forward(100)
        turtle.right(grados)

    elif opcion == 2: #cuadrado
        grados = 360/4
        turtle.forward(100)
        turtle.right(grados)
        turtle.forward(100)
        turtle.right(grados)
        turtle.forward(100)
        turtle.right(grados)
        turtle.forward(100)
        turtle.right(grados)

    elif opcion == 3: #pentagono
        grados = 360/5
        turtle.forward(100)
        turtle.right(grados)
        turtle.forward(100)
        turtle.right(grados)
        turtle.forward(100)
        turtle.right(grados)
        turtle.forward(100)
        turtle.right(grados)
        turtle.forward(100)
        turtle.right(grados)

    else: 
        print("opcion invalidad")

    programa = input("Escribe si para graficar o no para no graficar")
    print("programa terminado")
turtle.exitonclick()