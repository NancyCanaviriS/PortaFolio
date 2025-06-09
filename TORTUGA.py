import turtle

#creacion de las ventanas 
ventana=turtle.Screen()
ventana.title('Juego Snake')
ventana.bgcolor('black')
ventana.setup(width=600,height=600)

##cabeza snake
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.penup()
cabeza.shape('square')
cabeza.color('blue')
cabeza.goto(0,0)
ventana.mainloop()   
