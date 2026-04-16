import turtle
import random as r
t = turtle.Turtle()
t.speed(0)
for _ in range(50):
    t.penup()
    l = r.randint(10,100)
    x = r.randint(-200,200)
    y = r.randint(-200,200)
    t.goto(x,y)
    ang = r.randint(0,90)
    t.setheading(ang)
    t.pendown()
    for _ in range(4):
        t.forward(l)
        t.right(90)
turtle.done