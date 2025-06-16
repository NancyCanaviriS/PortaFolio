import TORTUGA
import random
import time

partes=[]
cabeza=TORTUGA.cabeza
comida=TORTUGA.comida

texto=TORTUGA.texto 
#variables de puntaje
puntaje=0
mejor_puntaje=0

#funcion game over
def game_over():
    time.sleep(1)
    cabeza.goto(0,0)
    cabeza.direccion='quieta'
    for i in partes:
        i.hideturtle()
    partes.clear()


while True:
    #actualizacion ventana
    TORTUGA.ventana.update()

    #choque de bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 220 or cabeza.ycor() < -280:
        game_over()

    #colision comida
    if cabeza.distance(comida) < 20: 
        x=random.randint(-14,14)
        y=random.randint(-14,10)
        comida.goto(x*20,y*20)
        #colores
        if len(partes)%2 !=0:
            colores='blue'
        else:
            colores='yellow'
        nueva_parte=TORTUGA.creacion_elemento('square',colores)
        nueva_parte.direccion='quieta'
        partes.append(nueva_parte)

        #aumentar puntaje
        puntaje += 1
        if puntaje > mejor_puntaje:
            mejor_puntaje=puntaje
        texto.clear()
        texto.write('Puntaje: {}  Mejor puntaje:{}'.format(puntaje,mejor_puntaje),
                    align='center' , font=('Courier',20,'normal'))

    #mover partes
    partes_totales=len(partes)
    for i in range(partes_totales-1,0,-1):
        x=partes[i-1].xcor()
        y=partes[i-1].ycor()
        partes[i].goto(x,y)
    if partes_totales > 0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        partes[0].goto(x,y)

    #llamar al movimento
    TORTUGA.movimiento()

    #colision del cuerpo
    for i in partes:
        if i.distance(cabeza) < 20:
            game_over()
    #retardo
    time.sleep(0.05)
