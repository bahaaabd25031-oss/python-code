import turtle
l = [['F',75],['L',110],['F',150],['R',110],['F',100]]
t = turtle.Turtle()
t.speed(1)
for i in l:
    if i[0] == 'F': t.forward(i[1])
    elif i[0] == 'L': t.left(i[1])
    elif i[0] == 'R': t.right(i[1])
turtle.done

