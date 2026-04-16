import turtle
import random as r
t = turtle.Turtle()
t.speed(0)
for _ in range(500):
    t.pendown()
    t.circle(r.randint(5,50))
    t.penup()
    t.goto(r.randint(-200,200),r.randint(-200,200))
turtle.done