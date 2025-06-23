import pygame 
from pygame.locals import*
import random

winHori=800
winVert=600
fps=60
white=(255,255,255)
negro=(0,0,0)
class pelotaP:
  def _init_(self, fichero_imagen):
        self.imagen=pygame.image.load(fichero_imagen).convert_alpha()
        self.ancho,self,alto=self.imagen.get_size()
        self.x=winHori/2-self.ancho/2
        self.y=winVert/2-self.alto/2
        self.dir_x=random.choice([-5,5])
        self.dir_y=random.choice([-5,5])
        self.puntuacion=0
        self.puntuacion_maqui=0
  def movimiento(self):
        self.x+=self.dir_x
        self.y+=self.dir_y
  def reiniciar(self):
       self.x=winHori/2-self.ancho/2
       self.y=winVert/2-self.alto/2
       self.dir_x=-self.dir_x
       self.dir_y=random.choice([-5,5])
  def rebotar(self):
       if self.x<=-self.ancho:
            self.reiniciar()
            self.puntuacion_maqui+=1
       if self.x>=winHori:
            self.reiniciar()
            self.puntuacion+=1
       if self.y<=0:
            self.dir_y=-self.dir_y
       if self.y+self.alto>=winVert:
            self.dir_y=self.dir_y
class raqueta:
     def __init__(self):
          self.imagen=pygame.image.load('raqueta.png').convert_alpha()
          self.ancho,self.alto=self.imagen.get_size()
          self.x=0
          self.y=winVert/2-self.alto/2
          self.dir_y=0
     def movimiento(self): 
          self.y+=self.dir_y
          if self.y<=0:
               self.y=0
          if self.y+self.alto>=winVert:
             self.y=winVert-self.alto
     def movimiento_maqui(self):
          if self.p>pelota.y:
               self.dir_y=-3
          elif self.y<pelota.y:
               self.dir_y=+3
          else :
               self.dir_y=0
          self.y+=self.dir_y
     def  golpear(self,pelota):
         if (
              pelota.x<self.x+self.ancho
              and pelota.x>self.x
              and pelota.y+pelota.alto>self.y
              and pelota.y<self.y+self.alto
          ):
              