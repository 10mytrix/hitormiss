import turtle
import random

t=turtle.Turtle()
t.penup()
t.left(90)
t.speed(0)
t.hideturtle()
turtle.tracer(100,0)
turtle.colormode(255)
def draw(long,angl):
    if long>1:
        t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        t.forward(long*0.2)
        t.left(75)
        draw(long*0.4,angl)
        t.right(150)
        draw(long*0.4,angl)
        t.left(75)
        t.forward(long*0.2)
        t.right(angl)
        draw(long*0.8,angl)
        t.left(angl)
        t.forward(long*-0.4)
t.pendown()
draw(200,15)