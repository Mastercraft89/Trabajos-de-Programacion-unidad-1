import turtle
turtle.shape("turtle")

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
'''
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
'''
turtle.exitonclick()