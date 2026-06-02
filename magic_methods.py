class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def __str__(self):
        return f"{self.account_holder}: {self.balance}"
    def __add__(self, o2):
        return self.balance + o2.balance
    def __sub__(self, o2):
        return self.balance - o2.balance
    def __eq__(self, o2):
        return self.balance == o2.balance
    def __lt__(self, o2):
        return self.balance < o2.balance
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return super().__getattribute__(name)
    def __setattr__(self, name, value):
        if name == "balance" and value < 0:
            print("Negative balance not allowed")
        super().__setattr__(name, value)
a1 = BankAccount("Santhi", 5000)
a2 = BankAccount("Raji", 3000)
print(a1 + a2)
print(a1 - a2)
print(a1 == a2)
print(a1 < a2)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return f"{self.name}: {self.total_price()}"
    def __add__(self, o2):
        return self.total_price() + o2.total_price()
    def __mul__(self, o2):
        return self.total_price()* o2.total_price()
    def __gt__(self, o2):
        return self.total_price() > o2.total_price()
    def __eq__(self, o2):
        return self.price == o2.price
    def __getattr__(self, name):
        return "Attribute not found"
    def __setattr__(self, name, value):
        if name == "price" and value < 0:
            raise ValueError("Invalid price")
        super().__setattr__(name, value)
p1=Product("santhi",20,5)
p2=Product("Sri",30,5)
print(p1+p2)
print(p1*p2)
print(p1>p2)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def grade(self):
        return "Pass" if self.marks >= 40 else "Fail"
    def __str__(self):
        return f"{self.name}: {self.marks}"
    def __add__(self, other):
        return self.marks + other.marks
    def __truediv__(self,o2):
        return self.marks /o2.marks
    def __ge__(self, other):
        return self.marks >= other.marks
    def __lt__(self, other):
        return self.marks < other.marks
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "marks" and not (0 <= value <= 100):
            raise StopIteration
        print("Marks must be 0-100")
        super().__setattr__(name, value)
s1=Student("santhi",40)
s2=Student("Raji",90)
print(s1+s2)
print(s1/s2)
print(s1>=s2)
print(s1<s2)



class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def __str__(self):
        return str(self.area())
    def __add__(self, o2):
        return self.area() + o2.area()
    def __sub__(self, o2):
        return self.area() - o2.area()
    def __eq__(self, o2):
        return self.area() == o2.area()
    def __gt__(self, o2):
        return self.area() > o2.area()
    def __getattr__(self, name):
        return "Not found"
    def __setattr__(self, name, value):
        if value <= 0:
            raise ValueError("Must be positive")
        object.__setattr__(self, name, value)



class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def reading_time(self):
        return self.pages * 2
    def __str__(self):
        return self.title
    def __add__(self, other):
        return self.pages + other.pages
    def __floordiv__(self, days):
        return self.pages // days
    def __gt__(self, other):
        return self.pages > other.pages
    def __eq__(self, other):
        return self.title == other.title
    def __getattr__(self, name):
        return "Attribute missing"
    def __setattr__(self, name, value):
        if name == "title" and value == "":
            raise ValueError("Empty title")
        if name == "pages" and value <= 0:
            raise ValueError("Invalid pages")
        object.__setattr__(self, name, value)



class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
    def final_amount(self):
        return self.price * self.quantity
    def __str__(self):
        return self.item_name
    def __add__(self, o2):
        return self.final_amount() +self.final_amount()
    def __mod__(self, discount):
        return self.final_amount() % discount
    def __lt__(self, o2):
        return self.final_amount() < o2.final_amount()
    def __ge__(self, o2):
        return self.quantity >= o2.quantity
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "quantity" and value < 1:
            raise ValueError("Invalid quantity")
        object.__setattr__(self, name, value)


class TimeDuration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def total_minutes(self):
        return self.hours * 60 + self.minutes
    def __str__(self):
        return f"{self.hours}:{self.minutes}"
    def __add__(self, o2):
        return self.total_minutes() + o2.total_minutes()
    def __sub__(self, o2):
        return self.total_minutes() - o2.total_minutes()
    def __eq__(self, o2):
        return self.total_minutes() == o2.total_minutes()
    def __gt__(self, o2):
        return self.total_minutes() > o2.total_minutes()
    def __getattr__(self, name):
        return "Invalid attribute"
    def __setattr__(self, name, value):
        if name == "minutes" and not (0 <= value <= 59):
            raise ValueError("Minutes must be 0-59")
        object.__setattr__(self, name, value)


class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def upgrade_ram(self, extra_ram):
        self.ram += extra_ram
    def __str__(self):
        return self.brand
    def __add__(self, o2):
        return self.price + o2.price
    def __mul__(self, n):
        return self.price * n
    def __lt__(self, o2):
        return self.price < o2.price
    def __eq__(self, o2):
        return self.ram == o2.ram
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name in ["ram", "price"] and value <= 0:
            raise ValueError("Must be positive")
        object.__setattr__(self, name, value)


class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, enemy):
        enemy.health -= self.attack_power
    def __str__(self):
        return self.name
    def __add__(self, o2):
        return self.attack_power + o2.attack_power
    def __sub__(self, damage):
        self.health -= damage
    def __gt__(self, o2):
        return self.health > o2.health
    def __eq__(self, o2):
        return self.attack_power == o2.attack_power
    def __getattr__(self, name):
        return "Stat unavailable"
    def __setattr__(self, name, value):
        if name == "health" and value < 0:
            raise ValueError("Health cannot be negative")
        object._setattr_(self, name, value)