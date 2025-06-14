import TORTUGA
import random
import time

partes=[]
cabeza=TORTUGA.cabeza
comida=TORTUGA.comida

while True:
    #actualizacion ventana
    TORTUGA.ventana.update()

    #choque de bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direccion='quieta'
        time.sleep(1)
    #colision comida
    if cabeza.distance(comida) < 20: 
        x=random.randint(-14,14)
        y=random.randint(-14,14)
        comida.goto(x*20,y*20)
        nueva_parte=TORTUGA.creacion_elemento('square','yellow')
        nueva_parte.direccion='quieta'
        partes.append(nueva_parte)

    #llamar al movimento
    TORTUGA.movimiento()
    #retardo
    time.sleep(0.05)
