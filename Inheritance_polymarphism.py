class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    def info(self):
        super().info()
        print(f"Doors: {self.doors}")
class ElectricCar(Car):
    def __init__(self, make, model, year, doors, battery_range):
        super().__init__(make, model, year, doors)
        self.battery_range = battery_range
    def info(self):
        super().info()
        print(f"Battery Range: {self.battery_range} km")
v = Vehicle("Honda", "Activa", 2022)
c = Car("Hyundai", "i20", 2023, 4)
e = ElectricCar("Tesla", "Model 3", 2025, 4, 500)
print("Vehicle:")
v.info()
print("\nCar:")
c.info()
print("\nElectric Car:")
e.info()




class Printable:
    def print_info(self):
        print("Printing document...")
class Saveable:
    def save(self):
        print("Saving document...")
class Document(Printable, Saveable):
    pass
doc = Document()
doc.print_info()
doc.save()
print("\nMRO:")
for cls in Document.__mro__:
    print(cls.__name__)



class A:
    def hello(self):
        return "A"
class B(A):
    def hello(self):
        return "B"
class C(A):
    def hello(self):
        return "C"
class D(B, C):
    pass
d = D()
print("hello() result:", d.hello())
print("\nMRO:")
for cls in D.__mro__:
    print(cls.__name__)


class A:
    def hello(self):
        return "A"
class B(A):
    pass
class C(A):
    def hello(self):
        return "C"
class D(B, C):
    pass
d = D()
print("hello() result:", d.hello())
print("\nMRO:")
for cls in D.__mro__:
    print(cls.__name__)




class School:
    def __init__(self, school_name):
        self.school_name = school_name
        print("School initialized")
class Department(School):
    def __init__(self, school_name, department_name):
        super().__init__(school_name)
        self.department_name = department_name
        print("Department initialized")
class Course(Department):
    def __init__(self, school_name, department_name, course_name):
        super().__init__(school_name, department_name)
        self.course_name = course_name
        print("Course initialized")
c = Course("ABC School", "Computer Science", "Python")
print("\nDetails:")
print("School:", c.school_name)
print("Department:", c.department_name)
print("Course:", c.course_name)




class Payment:
    def __init__(self, amount):
        self.amount = amount
    def process(self):
        print(f"Processing payment of ₹{self.amount}")
class CreditCard(Payment):
    def process(self):
        print(f"Paid ₹{self.amount} using Credit Card")
class UPI(Payment):
    def process(self):
        print(f"Paid ₹{self.amount} using UPI")
class NetBanking(Payment):
    def process(self):
        print(f"Paid ₹{self.amount} using Net Banking")
def checkout(payment):
    payment.process()
payments = [CreditCard(1000),UPI(500),NetBanking(2000)]
for p in payments:
    checkout(p)


class PDFReport:
    def send(self):
        print("PDF Report Sent")
class ExcelSheet:
    def send(self):
        print("Excel Sheet Sent")
class EmailMessage:
    def send(self):
        print("Email Message Sent")
def dispatch(item):
    item.send()
dispatch(PDFReport())
dispatch(ExcelSheet())
dispatch(EmailMessage())

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Hexagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total
shapes = [Circle(5),Rectangle(4, 6),Triangle(10, 8),Hexagon(3)]
print("Total Area =", total_area(shapes))




class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
d = Dog()
d.speak()
class Calculator:
    def add(self, *args):
        return sum(args)
c = Calculator()
print(c.add(10, 20))
print(c.add(10, 20, 30))
print(c.add(10, 20, 30, 40))