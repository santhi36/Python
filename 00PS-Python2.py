class ShoppingCart:
    def __init__(self):
        self.__items = []   # private
    def add_item(self, item):
        self.__items.append(item)
    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
    def get_items(self):
        return self.__items.copy()   # safe copy
cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Mouse")
print(cart.get_items())



from abc import ABC, abstractmethod
class Sensor(ABC):
    def __init__(self):
        self.__raw_value = 100
        self.__factor = 1.0
    @abstractmethod
    def read_value(self):
        pass
    def calibrate(self):
        print("Calibration done successfully")
    def get_reading(self):
        return self.read_value()
class TemperatureSensor(Sensor):
    def read_value(self):
        return "Temperature: 25°C"
class PressureSensor(Sensor):
    def read_value(self):
        return "Pressure: 1013 hPa"
class HumiditySensor(Sensor):
    def read_value(self):
        return "Humidity: 60%"
t = TemperatureSensor()
print(t.get_reading())
t.calibrate()



class BS:
    def sort(self, data):
        return sorted(data)
class MS:
    def sort(self, data):
        return sorted(data)
class QS:
    def sort(self, data):
        return sorted(data)
class Sorter:
    def change(self, strategy):
        self.strategy = strategy
    def sort_data(self, data):
        return self.strategy.sort(data)
nums = [5, 2, 8, 1]
s = Sorter()
s.change(BS())
print(s.sort_data(nums))
s.change(QS())
print(s.sort_data(nums))



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
class Account(ABC):
    interest_rate = 5
    def __init__(self, balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    @abstractmethod
    def calculate_interest(self):
        pass
    @staticmethod
    def validate_amount(amount):
        return amount > 0
    @classmethod
    def update_interest(cls, rate):
        cls.interest_rate = rate
class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.05
class CurrentAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.02
class FixedDepositAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.08
acc = SavingsAccount(10000)
acc.deposit(2000)
print("Balance:", acc.balance)
print("Interest:", acc.calculate_interest())
Account.update_interest(6)
print("New Rate:", Account.interest_rate)








