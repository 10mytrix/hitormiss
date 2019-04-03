import turtle as tu
import random
erwin=tu.Turtle()
erwin.speed(0)
#tu.setup(width=.90, height=.90, startx=0, starty=0)
erwin.penup()
erwin.goto(-300,300)
erwin.ht()
erwin.pendown()
tu.colormode(255)
tu.tracer(100,0)
def gauche(step,long):
    if step!=0:
        erwin.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        erwin.right(90)
        droite(step-1,long)
        erwin.fd(long)
        erwin.left(90)
        gauche(step-1,long)
        erwin.fd(long)
        gauche(step-1,long)
        erwin.left(90)
        erwin.fd(long)
        droite(step-1,long)
        erwin.right(90)
def droite(step,long):
    if step!=0:
        erwin.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        erwin.left(90)
        gauche(step-1,long)
        erwin.fd(long)
        erwin.right(90)
        droite(step-1,long)
        erwin.fd(long)
        droite(step-1,long)
        erwin.right(90)
        erwin.fd(long)
        gauche(step-1,long)
        erwin.left(90)
gauche(8,2)
        
        
    

        
        