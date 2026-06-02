class Animal:
    def make_sound(self):
        print("Animal sound")
class Dog(Animal):
    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
class Cow(Animal):
    def make_sound(self):
        print("Moo")
animals = [Dog(), Cat(), Cow()]
for a in animals:
    a.make_sound()



class Car:
    def start(self):
        print("Car started")
class Computer:
    def start(self):
        print("Computer started")
class WashingMachine:
    def start(self):
        print("Washing Machine started")
def operate(device):
    device.start()
operate(Car())
operate(Computer())
operate(WashingMachine())


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def show(self):
        print(self.x, self.y)
v1 = Vector(2, 3)
v2 = Vector(1, 4)
v3 = v1 + v2
v3.show()
print(v1 == v2)



class Transport:
    def move(self):
        print("Transport is moving")
class Bus(Transport):
    def move(self):
        super().move()
        print("Bus moves on road")
class Bike(Transport):
    def move(self):
        super().move()
        print("Bike moves fast")
b = Bus()
b.move()
bk = Bike()
bk.move()



from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self):
        print("Email sent")
class SMSNotification(Notification):
    def send(self):
        print("SMS sent")
class PushNotification(Notification):
    def send(self):
        print("Push notification sent")
msgs = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]
for m in msgs:
    m.send()



class Payment:
    def process(self, amount):
        print("Amount:", amount)
class CreditCardPayment(Payment):
    def process(self, amount, card_type):
        print("Amount:", amount)
        print("Card Type:", card_type)
p = Payment()
p.process(1000)
c = CreditCardPayment()
c.process(2000, "Visa")



class BS:
    def logic(self):
        print("Bubble Sort")
class MS:
    def logic(self):
        print("Merge Sort")
class QS:
    def logic(self):
        print("Quick Sort")
class Sorter:
    def change(self, strategy):
        strategy.logic()
s = Sorter()
s.change(BS())
s.change(MS())
s.change(QS())



class Account:
    def withdraw(self):
        print("Withdraw from Account")
class SavingsAccount(Account):
    def withdraw(self):
        print("Withdraw from Savings Account")
class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self):
        super().withdraw()
        print("Extra benefits in Premium Account")
p = PremiumSavingsAccount()
p.withdraw()



class Circle:
    def draw(self):
        print("Drawing Circle")
class Square:
    def draw(self):
        print("Drawing Square")
class Rectangle:
    def draw(self):
        print("Drawing Rectangle")
class Car:
    def draw(self):
        print("Drawing Car")
def draw(shape):
    shape.draw()
draw(Circle())
draw(Square())
draw(Rectangle())
draw(Car())


class UPI:
    def pay(self):
        print("UPI Payment")
class Card:
    def pay(self):
        print("Card Payment")
class Cash:
    def pay(self):
        print("Cash Payment")
payments = [UPI(), Card(), Cash()]
for p in payments:
    p.pay()
class UPI:
    def pay(self):
        print("UPI Payment")
class Card:
    def pay(self):
        print("Card Payment")
class Cash:
    def pay(self):
        print("Cash Payment")
def payment_method(obj):
    if isinstance(obj, UPI):
        obj.pay()
    elif isinstance(obj, Card):
        obj.pay()
    elif isinstance(obj, Cash):
        obj.pay()
payment_method(UPI())
payment_method(Card())
payment_method(Cash())

