import math
import turtle

class Shape:
    def __init__(self, name, area=0):
        self.name = name
        self.__area__=area
    def __str__(self):
        return self.name
    def area(self):
        return self.__area__


class Rect(Shape):
    def __init__(self, name, length = 0, width = 0, x = 0, y = 0, color = "black"):
        super().__init__(name, length*width)
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.color = color
    
    def __str__(self):
        return "Rect: " + super().__str__() + "(" + str(self.__area__) + ")"
    
    def __mul__(self, k):
        t = Rect(self.name, self.length * k, self.width * k)
        return t
    
    def draw(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        for i in range(2):
            t.forward(self.length)
            t.right(90)
            t.forward(self.width)
            t.right(90)
    
    def shift(self, j, k):
        self.x += j
        self.y += k
        



class Circle(Shape):
    def __init__(self, name, radius = 0, x = 0, y = 0):
        super().__init__(name, math.pi*radius**2)
        self.radius = radius
        self.x = x
        self.y = y
    def __str__(self):
        return "Circle: " + super().__str__()
    
    def __mul__(self, k):
        t = Circle(self.name, self.radius * k)
        return t
    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x, self.y - self.radius)
        t.pendown()
        t.circle(self.radius)

        



r = Rect("field", 100, 50)
print(r)
r.draw()
r = r * 2
print(r.area())
r.shift(-100, 50)
r.color = "red"
r.draw()

c = Circle("roundabout", 50)
c.draw()
c = c * 5
print(c)
print(c.area())
turtle.done()

        


