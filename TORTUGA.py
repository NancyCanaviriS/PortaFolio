import turtle

#creacion de la ventana
ventana=turtle.Screen()
ventana.title('Juego Snake')
ventana.bgcolor('black')
ventana.setup(width=600,height=600)
#funcion creacion de elementos(tortuga)
def creacion_elemento(forma,color):
    elemento=turtle.Turtle()
    elemento.speed(0)
    elemento.penup()
    elemento.shape(forma)
    elemento.color(color)
    elemento.goto(0,0)
    return elemento
#creacion de elementos
cabeza=creacion_elemento('square','blue')
cabeza.direccion='quieta'
comida=creacion_elemento('circle','red')
comida.goto(0,90)
#creacion de texto(puntaje)
texto=creacion_elemento(None,'white')
texto.hideturtle()
texto.goto(0,260)
texto.write('Puntaje:0  Mejor puntaje:0',align='center' , font=('Courier',20,'normal'))
#funciones
def arriba():
    cabeza.direccion='arriba'
def abajo():
    cabeza.direccion='abajo'
def izquierda():
    cabeza.direccion='izquierda'
def derecha():
    cabeza.direccion='derecha'

#teclado
ventana.listen()
ventana.onkeypress(arriba,'Up')
ventana.onkeypress(abajo,'Down')
ventana.onkeypress(izquierda,'Left')
ventana.onkeypress(derecha,'Right')

#movimiento
def movimiento():
    #movimiento vertical
    if cabeza.direccion== 'arriba':
        y=cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direccion=='abajo':
        y=cabeza.ycor() 
        cabeza.sety(y-20)  
    #movimiento horizontal
    if cabeza.direccion== 'izquierda':
        x=cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direccion=='derecha':
        x=cabeza.xcor() 
        cabeza.setx(x+20) 

