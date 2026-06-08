import math
class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
class Square:
    def __init__(self,s):
        self.s=s
class Circle:
    def __init__(self,r):
        self.r=r
class Triangle:
    def __init__(self,b,h):
        self.b=b
        self.h=h
class Shape:
    def area(self,a):
        if isinstance(a,Rectangle):
            print(f"Area of Rectangle: {a.l*a.b}")
        elif isinstance(a,Square):
            print(f"Area of Square: {a.s**2}")
        elif isinstance(a,Circle):
            print(f"Area of Circle: {math.pi*a.r*a.r}")
        elif isinstance(a,Triangle):
            print(f"Area of Triangle: {0.5*a.b*a.h}")
r=Rectangle(13,20)
s=Square(12)
c=Circle(22)
t=Triangle(16,8)
a=Shape()
a.area(r)
a.area(s)
a.area(c)
a.area(t)































