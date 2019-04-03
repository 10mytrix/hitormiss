from datetime import datetime
import turtle
turtle.delay(0)
petit= turtle.Turtle()
petit.ht()
petit.pensize(6)
petit.color("red")
grand= turtle.Turtle()
grand.ht()
grand.pensize(3)
point= turtle.Turtle()
point.ht()
dessin= turtle.Turtle()
rayon=200
point.speed(0)
petit.speed(0)
grand.speed(0)
dessin.speed(0)
h,m,s=0,0,0
msave,ssave=0,0
def cadran():
    dessin.ht()
    global rayon
    for i in range(61):
        dessin.penup()
        dessin.home()
        dessin.setheading(90-6*i)
        dessin.pensize(1)
        if i%15==0:
            dessin.fd(rayon-10)
            dessin.pensize(2)
            dessin.pendown()
            dessin.fd(10)
            dessin.pu()
            dessin.fd(20)
        elif i%5==0:
            dessin.fd(rayon-7)
            dessin.pendown()
            dessin.fd(7)
        else:
            dessin.fd(rayon-3)
            dessin.pendown()
            dessin.fd(3)
    dessin.penup()
    dessin.home()
    dessin.setheading(-3)
    dessin.fd(rayon+10)
    dessin.write("3",move=False, align="center", font=("Arial", 15, "bold"))
    dessin.home()
    dessin.setheading(-90)
    dessin.fd(rayon+20)
    dessin.write("6",move=False, align="center", font=("Arial", 15, "bold"))
    dessin.home()
    dessin.setheading(-177)
    dessin.fd(rayon+10)
    dessin.write("9",move=False, align="center", font=("Arial", 15, "bold"))
    dessin.home()
    dessin.setheading(-270)
    dessin.fd(rayon)
    dessin.write("12",move=False, align="center", font=("Arial", 15, "bold"))
    dessin.home()
        
        
def printtime():
    global h,m,s,msave,ssave
    if datetime.now().second!=s:
        s=datetime.now().second
        printsecond(s)
    if datetime.now().hour!=h or msave-m!=0:
        msave=m
        h=datetime.now().hour
        printhour(h,msave)
    if datetime.now().minute!=m or ssave-s!=0:
        ssave=s
        m=datetime.now().minute
        printminute(m,ssave)
        
def printhour(t,t2):
    global rayon
    petit.clear()
    petit.home()
    petit.seth((-30*(t%12)-t2/2)+90)
    petit.pd()
    petit.fd(rayon/3)
    petit.pu()
def printminute(t,t2):
    grand.clear()
    grand.home()
    grand.seth((-6*t-t2/10)+90)
    grand.pd()
    grand.fd(2*rayon/3)
    grand.pu()
def printsecond(t):
    point.clear()
    point.home()
    point.seth(-6*t+90)
    point.pd()
    point.fd(3*rayon/4)
    point.pu()       
def init():
    global h,m,s
    h=datetime.now().hour
    print(h)
    m=datetime.now().minute
    s=datetime.now().second
    printhour(h,m)
    printminute(m,s)
    printsecond(s)
    
cadran()
init()
while s!=-1:
    printtime()


