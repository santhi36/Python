class BankAccount:
    def __init__(self, balance=0):
        self.__balance = 0
        self.balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance = self.balance - amount
acc = BankAccount(100)
acc.deposit(50)
print("After deposit:", acc.balance)
acc.withdraw(30)
print("After withdrawal:", acc.balance)



import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self.__radius = value
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
c = Circle(5)
print("Radius:", c.radius)
print("Area:", c.area)
print("Circumference:", c.circumference)
c.radius = 10
print("\nAfter changing radius:")
print("Radius:", c.radius)
print("Area:", c.area)
print("Circumference:", c.circumference)



class Config:
    def __init__(self):
        self.app_name = "MyApp"
        self._settings = {"theme": "dark"}
        self.__secret_key = "ABC123"
    def get_setting(self, key):
        return self._settings.get(key)
    def get_secret_key(self):
        return self.__secret_key
cfg = Config()
print("App Name:", cfg.app_name)
print("Settings:", cfg._settings)
print("Secret Key:", cfg._Config__secret_key)
print("Secret Key (safe):", cfg.get_secret_key())
print("Theme:", cfg.get_setting("theme"))



class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    @full_name.setter
    def full_name(self, value):
        parts = value.split(" ", 1)
        if len(parts) != 2:
            raise ValueError("Enter first and last name")
        self.first_name, self.last_name = parts
p = Person("santhi", "akana")
print("Full Name:", p.full_name)
p.full_name = "santhi akana"
print("First Name:", p.first_name)
print("Last Name:", p.last_name)
print("Full Name:", p.full_name)
