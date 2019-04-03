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
r=1.1
a=0.2
n=6
def dessinerEtoile(x,size):
    dessin.pd()
    for i in range(1,x+1):
        dessin.left(180-180/x)
        dessin.fd(size)

def branche(nb):
    for i in range(1,nb+1):
        dessin.pu()
        dessin.color(10+8*i,0,0)
        dessin.fd(2+i)
        #test=n+i*3
        #dessin.goto((r**test)*cos(a*test),(r**test)*sin(a*test))
        dessin.pd()
        dessinerEtoile(1+2*((i//10)+1),i)
        dessin.left(10/((i/2)**(1/10)))
    dessin.pu()
    dessin.fd(20)
    dessin.pensize(30)
    dessin.pd()
    dessin.fd(1)
    dessin.pensize(1)
    dessin.pu()
while False:
    dessin.penup()
    dessin.goto(random.randint(-200,200),random.randint(-200,200))
    dessinerEtoile(1+2*random.randint(1,10),40)
    
    time.sleep(0.5)
repet=6
for i in range(1,repet+1):
    dessin.pu()
    dessin.home()
    dessin.lt((360/repet)*i)
    dessin.fd(30)
    branche(30)
    
