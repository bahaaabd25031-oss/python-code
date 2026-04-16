import turtle 
t = turtle.Turtle() 
t.speed(7) 
for _ in range(2):
    for _ in range(4):
        for _ in range(4):
            t.forward(100)
            t.left(90)
        t.forward(100)
    t.right(180)
turtle.done