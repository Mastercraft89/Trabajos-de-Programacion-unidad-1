import turtle
turtle.shape("turtle")
programa = input("Escribe si para graficar o no para no graficar =")
longitud = 30
while programa == "si":
    lados = int(input("Escribe el numero de lados de la figura :"))
    if lados == 0:
        print("opcion invalidad")
    else:
        grados= 360/lados
    for i in range (0,lados):
        turtle.forward(longitud)
        turtle.right(grados)

    programa = input("Escribe si para graficar o no para no graficar =")

print("programa terminado")
turtle.exitonclick()