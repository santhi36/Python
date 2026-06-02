class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
b = BankAccount(101, 5000)
b.deposit(1000)
b.withdraw(2000)
print("Balance:", b.get_balance())
b.__balance = 100000
print(b.__balance)
print(b.get_balance())


class Student:
    def __init__(self):
        self.__marks = 0
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")
    def get_marks(self):
        return self.__marks
s = Student()
s.set_marks(85)
print(s.get_marks())
s.__marks = 200
print(s.__marks)
print(s.get_marks())


class SecureFile:
    def __init__(self, content, password):
        self.__content = content
        self.__password = password
        self.__logs = []
    def read(self, password):
        if password == self.__password:
            return self.__content
        else:
            self.__logs.append("Unauthorized attempt")
            return "Access Denied"
f = SecureFile("Secret Data", "1234")
print(f.read("1111"))
print(f.read("1234"))



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def get_salary(self):
        print("Salary accessed")
        return self.__salary
    def update_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("Salary updated")
        else:
            print("New salary must be higher")
e = Employee("John", 50000)
print(e.get_salary())
e.update_salary(60000)
e.update_salary(40000)


class Product:
    def __init__(self, price, discount):
        self.__price = price
        self.__discount = discount
    def get_final_price(self):
        if self.__price < 0:
            return "Invalid price"
        if self.__discount > 70:
            return "Discount too high"
        final = self.__price - (self.__price * self.__discount / 100)
        return final
p = Product(1000, 20)
print("Final Price:", p.get_final_price)


class Character:
    def __init__(self, health, max_health):
        self.__health = health
        self.__max_health = max_health
    def damage(self, points):
        self.__health -= points
        if self.__health < 0:
            self.__health = 0
    def heal(self, points):
        self.__health += points
        if self.__health > self.__max_health:
            self.__health = self.__max_health
    @property
    def health(self):
        return self.__health
c = Character(80, 100)
c.damage(30)
print(c.health)
c.heal(50)
print(c.health)


class Engine:
    def __init__(self):
        self.__temperature = 90
    def cool(self):
        self.__temperature -= 10
        print("Engine cooled")
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.__engine = Engine()
    def start_car(self):
        self.__engine.start()
    def cool_engine(self):
        self.__engine.cool()
car = Car()
car.start_car()
car.cool_engine()


class ShoppingCart:
    def __init__(self):
        self.__items = []
    def add_item(self, item):
        self.__items.append(item)
    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
    def get_items(self):
        return self.__items.copy()
cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Mouse")
items = cart.get_items()
items.append("Keyboard")
print(cart.get_items())


class Attendance:
    def __init__(self):
        self.attendance = []
a = Attendance()
a.attendance.append("John")
a.attendance.append("Fake Entry")
print(a.attendance)
class Attendance:
    def __init__(self):
        self.__attendance = []
    def mark_attendance(self, name):
        self.__attendance.append(name)
    def show(self):
        return self.__attendance
a = Attendance()
a.mark_attendance("John")
print(a.show())


class Person:
    def __init__(self):
        self._age = 0
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Invalid age")
p = Person()
p.age = 25
print(p.age)
p._age = -10
print(p.age)

from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r
    def perimeter(self):
        return 2 * math.pi * self.r
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
    def perimeter(self):
        return 2 * (self.l + self.b)
c = Circle(5)
print(c.area())



class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self):
        pass
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
class UPIPayment(PaymentGateway):
    def authenticate(self):
        print("UPI Authenticated")
    def pay(self, amount):
        print("Paid", amount)
    def refund(self, amount):
        print("Refunded", amount)
u = UPIPayment()
u.authenticate()
u.pay(500)


class VehicleControl(ABC):
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def brake(self):
        pass
    @abstractmethod
    def steer(self):
        pass
class CarControl(VehicleControl):
    def accelerate(self):
        print("Car Accelerating")
    def brake(self):
        print("Car Braking")
    def steer(self):
        print("Car Steering")
c = CarControl()
c.accelerate()
c.brake()
c.steer()


class DatabaseDriver(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def execute(self, query):
        pass
    @abstractmethod
    def close(self):
        pass
class MySQLDriver(DatabaseDriver):
    def connect(self):
        print("MySQL Connected")
    def execute(self, query):
        print("Executing:", query)
    def close(self):
        print("Connection Closed")
db = MySQLDriver()
db.connect()
db.execute("SELECT * FROM users")
db.close()


class ReportGenerator(ABC):
    @abstractmethod
    def load_data(self):
        pass
    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def export(self):
        pass
class PDFReport(ReportGenerator):
    def load_data(self):
        print("Loading PDF data")
    def process(self):
        print("Processing PDF")
    def export(self):
        print("Exporting PDF")
r = PDFReport()
r.load_data()
r.process()
r.export()


class RobotCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass
class MoveCommand(RobotCommand):
    def execute(self):
        print("Robot moved")
    def undo(self):
        print("Move undone")
m = MoveCommand()
m.execute()
m.undo()



class MLModel(ABC):
    @abstractmethod
    def train(self, data):
        pass
    @abstractmethod
    def predict(self, x):
        pass
    @abstractmethod
    def evaluate(self, test):
        pass
class LinearRegressionModel(MLModel):
    def train(self, data):
        print("Training Linear Regression")
    def predict(self, x):
        return x * 2
    def evaluate(self, test):
        print("Evaluating Model")
model = LinearRegressionModel()
model.train([1,2,3])
print(model.predict(5))



def email(msg):
    print("Email:", msg)
def sms(msg):
    print("SMS:", msg)
def push(msg):
    print("Push:", msg)
class Notifier(ABC):
    @abstractmethod
    def send(self, msg):
        pass
class EmailSender(Notifier):
    def send(self, msg):
        print("Email:", msg)
n = EmailSender()
n.send("Hello")


class MediaPlayer(ABC):
    @abstractmethod
    def load(self):
        pass
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class MP3Player(MediaPlayer):
    def load(self):
        print("MP3 Loaded")
    def play(self):
        print("MP3 Playing")
    def stop(self):
        print("MP3 Stopped")
m = MP3Player()
m.load()
m.play()
m.stop()


class Sensor(ABC):
    def __init__(self):
        self.__raw = 100
        self.__factor = 1.2
    @abstractmethod
    def read_value(self):
        pass
    @abstractmethod
    def calibrate(self):
        pass
    def get_reading(self):
        return self.read_value() * self.__factor
class TemperatureSensor(Sensor):
    def read_value(self):
        return 35
    def calibrate(self):
        print("Temperature Sensor Calibrated")
t = TemperatureSensor()
print(t.get_reading())

