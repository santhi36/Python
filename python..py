class Animal:
    def sound(self):
        print("Animal make sound")
class Dog (Animal):
    def sound(self):
        print("Dog barks")
d=Dog()
d.sound()



class A:
    def show(self):
        print("class A")
class B(A):
    def show(self):
        super().show()
        print("class B")
obj =B()
obj.show()

class A:
    def display(self):
        print("class A")
class B(A):
    def display(self):
        print("class B")
class C(B):
    def display(self):
        print("class C")
obj=C()
obj.display()

class Vehical:
    pass
class Car(Vehical):
    def wheels(self):
        print("Car has 4 wheels")
class Bike(Vehical):
    def wheels(self):
        print("Bike has 2 wheels")
c = Car()
b = Bike()
c.wheels()
b.wheels()


class Employee:
    def salary(self):
        print("Salary=30000")
class Manager(Employee):
    
