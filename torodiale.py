import turtle as tu
import random
erwin=tu.Turtle()
erwin.speed(0)
tu.setup(width=.90, height=.90, startx=0, starty=0)
tu.colormode(255)
def cerclage(rep, rayon, decentration):
    erwin.penup()
    erwin.forward(decentration)
    erwin.right(90)
    erwin.pendown()
    erwin.stamp()
    while rep!=0:
        for i in range(1,rep+1):
            erwin.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            erwin.circle(rayon)
            erwin.right(360/rep)
            erwin.forward((3.1415*2*decentration)/rep)
        erwin.clear()

de=int(tu.numinput("DIS","decentration"))
ra=int(tu.numinput("DIS","rayon"))
re=int(tu.numinput("DIS","REP"))
cerclage(re,ra,de)
    
