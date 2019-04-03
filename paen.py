import turtle as tu
import random
tu.setup(width=.90, height=.90, startx=0, starty=0)
t=tu.Turtle()
tu.colormode(255)
def dessiner(cotes, repetition, long):
    global color_list
    for l in range(1, repetition+1):
        t.begin_fill()
        t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for i in range(1,cotes+1):
            t.forward(long)
            t.left(360/cotes)
        t.end_fill()
        t.right(360/repetition)

t.speed(0)

c=int(tu.numinput("DIS","COTES"))
l=int(tu.numinput("DIS","LONG"))
r=int(tu.numinput("DIS","REP"))
dessiner(c,r,l)
