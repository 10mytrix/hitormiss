import turtle
import random
import time
from math import *
dessin=turtle.Turtle()
dessin.ht()
dessin.pensize(1)
turtle.colormode(255)
dessin.speed(0)
turtle.delay(0)

def dessinerEtoile(x,size):
    dessin.pd()
    for i in range(1,x+1):
        dessin.left(180-180/x)
        dessin.fd(size)

def branche(nb):
    for i in range(1,nb+1):
        dessin.pu()
        dessin.color(10+i,0,0)
        dessin.fd(2+i/6)
        dessin.pensize(i/6)
        
        dessin.pd()
        dessin.fd(1)
        dessin.bk(1)
        dessin.left(10/((i**(1/2))/4))
repet=6
for i in range(1,repet+1):
    dessin.pu()
    dessin.home()
    dessin.lt((360/repet)*i)
    dessin.fd(30)
    branche(200)
    
