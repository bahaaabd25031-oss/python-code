import turtle 
n = int(input('enter a number to print th n\'th ploygon: '))
t = turtle.Turtle() 
t.speed(0)  
for i in range(n):                             
    t.color('green') 
    t.forward(800/n) 
    t.right(360/n)                                
turtle.done()


x = {}
print(type(x))