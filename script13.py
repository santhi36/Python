class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,o2):
        return self.x+o2

class B:
    def __init__(self,x):
        self.x=x
    def __add__(self,o2):
        if isinstance(o2,int):
            return self.x+o2
        if isinstance(o2,B):
            return self.x+o2.x
        else:
            print("wrong class")
            return 0
b1=B(30)
b2=B(35)
print(b1+b2)
print(b1+45)

##
class C:
    def __int__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,o2):
        if isinstance(o2,str):
            return self.x+o2
        elif isinstance(o2,int):
            return self.y+o2
        else:
            return self.z+o2.z
print(c1+"Hello")
print(c1+75)
print(c1+c2)
##
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class Cart:
    def __init__(self):
        self.l=[]
    def __add__(self, o2):
        self.l.append(o2)
    def __sub__(self, o2):
        if o2 in self.l:
            self.l.remove(o2)
    def total_price(self):
        s=0
        for i in self.l:
            s+=(i.price*i.quantity)
        return s
    def __str__(self):
        for i in self.l:
            print(i)
        print(f"total pr")

greater than in relation open""
class E:
    def __init__(self,a):
        self.a=a
    def __gt__(self, o2):
        return self.a>o2.a
e1=E(25)
e2=E(35)
e1>e2




