class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
d = Dog()
d.sound()



class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        super().show()
        print("Class B")
obj = B()
obj.show()



class A:
    def display(self):
        print("Class A")
class B(A):
    def display(self):
        print("Class B")
class C(B):
    def display(self):
        print("Class C")
obj = C()
obj.display()



class Vehicle:
    pass
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")
c = Car()
b = Bike()
c.wheels()
b.wheels()



class Employee:
    def salary(self):
        print("Salary = 30000")
class Manager(Employee):
    def salary(self):
        print("Salary = 30000 + Incentive")
e = Employee()
m = Manager()
e.salary()
m.salary()



class University:
    name = "ABC University"
    @classmethod
    def show(cls):
        print(cls.name)
class College(University):
    pass
print(College.name)
College.show()



class MathOps:
    @staticmethod
    def add(a, b):
        return a + b
class AdvancedOps(MathOps):
    pass
print(AdvancedOps.add(10, 20))



class Father:
    def skills(self):
        print("Father skills")
class Mother:
    def skills(self):
        print("Mother skills")
class Child(Father, Mother):
    pass
c = Child()
c.skills()


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")
r = Rectangle()
r.area()



class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
s = Student("Ravi", 101)
print(s.name)
print(s.roll)


