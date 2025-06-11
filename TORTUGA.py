import turtle

#creacion de las ventanas 
ventana=turtle.Screen()
ventana.title('Juego Snake')
ventana.bgcolor('black')
ventana.setup(width=600,height=600)

##cabeza snake
def creacion_elemento(forma,color):
    elemento=turtle.Turtle()
    elemento.speed(0)
    elemento.penup()
    elemento.shape(forma)
    elemento.color(color)
    elemento.goto(0,0)
    return elemento
cabeza=creacion_elemento('square','blue')
comida=creacion_elemento('circle','red')
comida.goto(0,90)
ventana.mainloop()   
