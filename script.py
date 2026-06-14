from abc import ABC,abstractmethod
class Pm(ABC):
    def __init__(self,b):
        self.__b=b
    @staticmethod
    def pay(self):
        pass
    @abstractmethod
    def validate(self):
        pass
    @property
    def bal(self):
        return self.__b
    @ bal.setter
    def bal(self,n):
        self.__b=n
    def  __add__(self, o2):
        return (self.pay()+o2.pay())/2
class card(Pm):
    def pay(self):
        return 500
    def valid(self,am):
        return am>=0
class wallet(Pm):
    def pay(self):
        return 10
    def valid(self,am):
        return am>=0
def checkout(l):
    k=int(input("Final bill:"))
    print("choose the options:")
p1= Pm(610)
c1=card(610)
w1=wallet(610)
print(c1+w1)
print(c1+w1)