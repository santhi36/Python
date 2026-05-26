class E:
    def __init__(self,a):
        self.a=a
    def __gt__(self, o2):
        return self.a>o2.a
    def __le__(self, o2):
        return self.a<o2.a
e1=E(25)
e2=E(35)
print(e1>e2)
print(e1<e2)
print(e1>=e2)
print(e2<=e1)
print(e1==e2)

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def td(self):
        return (self.x**2+self.y**2)**(1/2)
    def __add__(self, o2):
        return Vector(self.x+o2.x,self.y+o2.y)
    def __sub__(self, o2):
        return Vector(self.x-o2.x,self.y-o2.y)
    def __gt__(self,o2):
        return self.td()>o2.td()
    def __lt__(self,o2):
        return self.td()<o2.td()
    def __ge__(self,o2):
        return self.td()>=o2.td()
    def __le__(self,o2):
        return self.td()>=o2.td()
    def __eq__(self,o2):
        return self.td()==o2.td()
    def __str__(self):
        print(f"vector({self.x},{self.y})")
        return f"total_distance:{self.td()}"
v1=Vector(40,50)
v2=Vector(50,60)
v3=Vector(10,20)
print(v1+v2+v3)
print(v1+v2-v3)