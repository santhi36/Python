class BankAccount:
    def __init__(self, acc_no, balance):
        self.account_number = acc_no
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Withdrawal denied")
    def show_balance(self):
        return self.__balance
acc = BankAccount(101, 5000)
acc.deposit(1000)
acc.withdraw(2000)
print("Balance =", acc.show_balance())
acc.balance = 100000
print(acc.balance)          # New attribute created
print(acc.show_balance())   # Original balance unchanged




class Student:
    def __init__(self):
        self.__marks = 0
    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")
    def get_marks(self):
        return self.__marks
s = Student()
s.update_marks(85)
print("Marks =", s.get_marks())
s.marks = 200
print("Outside marks =", s.marks)
print("Actual marks =", s.get_marks())




class SecureFile:
    def __init__(self, content, password):
        self.__content = content
        self.__password = password
        self.__log = []
    def read(self, password):
        if password == self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorized attempt")
            return "Access Denied"
file = SecureFile("Confidential Data", "1234")
print(file.read("1234"))
print(file.read("9999"))




class Employee:
    def __init__(self, salary):
        self.__salary = salary
    def get_salary(self):
        print("Salary access logged")
        return self.__salary
    def update_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
        else:
            print("Salary cannot be decreased")
e = Employee(50000)
print(e.get_salary())
e.update_salary(60000)
print(e.get_salary())
e.update_salary(40000)



class Product:
    def __init__(self, price, discount):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if discount > 70:
            raise ValueError("Discount cannot exceed 70%")
        self.__price = price
        self.__discount = discount
    def __final_price(self):
        return self.__price - (self.__price * self.__discount / 100)
    def get_final_price(self):
        return self.__final_price()
p = Product(1000, 20)
print("Final Price =", p.get_final_price())



class Character:
    def __init__(self, max_health):
        self.__health = max_health
        self.__max_health = max_health

    def damage(self, points):
        self.__health -= points
        if self.__health < 0:
            self.__health = 0
    def heal(self, points):
        self.__health += points
        if self.__health > self.__max_health:
            self.__health = self.__max_health
    def get_health(self):
        return self.__health
c = Character(100)
c.damage(30)
print("Health =", c.get_health())
c.heal(20)
print("Health =", c.get_health())
c.damage(150)
print("Health =", c.get_health())



class Engine:
    def __init__(self):
        self.__temperature = 30
    def start(self):
        self.__temperature += 20
        print("Engine Started")
    def cool(self):
        self.__temperature -= 10
        print("Engine Cooled")
    def show_temp(self):
        return self.__temperature
class Car:
    def __init__(self):
        self.__engine = Engine()
    def start_car(self):
        self.__engine.start()
    def cool_engine(self):
        self.__engine.cool()
    def engine_status(self):
        print("Temperature =", self.__engine.show_temp())
car = Car()
car.start_car()
car.engine_status()
car.cool_engine()
car.engine_status()



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
print(cart.get_items())
cart.remove_item("Mouse")
print(cart.get_items())



class AttendanceBad:
    def __init__(self):
        self.attendance = []
a = AttendanceBad()
a.attendance.append("Present")
a.attendance.append("Absent")
a.attendance.clear()
print(a.attendance)

class Attendance:
    def __init__(self):
        self.__attendance = []
    def mark_present(self):
        self.__attendance.append("Present")
    def mark_absent(self):
        self.__attendance.append("Absent")
    def show_attendance(self):
        return self.__attendance.copy()
obj = Attendance()
obj.mark_present()
obj.mark_absent()
print(obj.show_attendance())



class Student:
    def __init__(self):
        self._marks = 0
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks")
s = Student()
s.marks = 90
print(s.marks)
class Demo:
    def __init__(self):
        self.marks = 0
d = Demo()
d.marks = -500


class Example:
    def __init__(self):
        self._age = 0
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value
e = Example()
e.age = -20
print(e.age)




from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5
    def perimeter(self):
        return self.a + self.b + self.c
c = Circle(7)
r = Rectangle(10, 5)
t = Triangle(3, 4, 5)
print(c.area())
print(r.perimeter())
print(t.area())
class Square(Shape):
    def area(self):
        return 100




from abc import ABC, abstractmethod
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
        print("Paid", amount, "through UPI")
    def refund(self, amount):
        print("Refunded", amount, "through UPI")
class CardPayment(PaymentGateway):
    def authenticate(self):
        print("Card Authenticated")
    def pay(self, amount):
        print("Paid", amount, "through Card")
    def refund(self, amount):
        print("Refunded", amount, "through Card")
class NetBankingPayment(PaymentGateway):
    def authenticate(self):
        print("Net Banking Authenticated")
    def pay(self, amount):
        print("Paid", amount, "through Net Banking")
    def refund(self, amount):
        print("Refunded", amount, "through Net Banking")
payments = [
    UPIPayment(),
    CardPayment(),
    NetBankingPayment()
]
for p in payments:
    p.authenticate()
    p.pay(500)



from abc import ABC, abstractmethod
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
        print("Car accelerating")
    def brake(self):
        print("Car braking")
    def steer(self):
        print("Car steering")
class BikeControl(VehicleControl):
    def accelerate(self):
        print("Bike accelerating")
    def brake(self):
        print("Bike braking")
    def steer(self):
        print("Bike steering")
class TruckControl(VehicleControl):
    def accelerate(self):
        print("Truck accelerating")
    def brake(self):
        print("Truck braking")
    def steer(self):
        print("Truck steering")
vehicles = [CarControl(), BikeControl(), TruckControl()]
for v in vehicles:
    v.accelerate()
    v.brake()
    v.steer()



from abc import ABC, abstractmethod
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
        print("Connected to MySQL")
    def execute(self, query):
        print("Executing:", query)
    def close(self):
        print("MySQL Connection Closed")
class PostgresDriver(DatabaseDriver):
    def connect(self):
        print("Connected to PostgreSQL")
    def execute(self, query):
        print("Executing:", query)
    def close(self):
        print("PostgreSQL Connection Closed")
class SQLiteDriver(DatabaseDriver):
    def connect(self):
        print("Connected to SQLite")
    def execute(self, query):
        print("Executing:", query)
    def close(self):
        print("SQLite Connection Closed")
db = MySQLDriver()
db.connect()
db.execute("SELECT * FROM student")
db.close()
db = SQLiteDriver()



from abc import ABC, abstractmethod
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
        print("Processing PDF report")
    def export(self):
        print("Exporting PDF file")
class ExcelReport(ReportGenerator):
    def load_data(self):
        print("Loading Excel data")
    def process(self):
        print("Processing Excel report")
    def export(self):
        print("Exporting Excel file")
reports = [PDFReport(), ExcelReport()]
for report in reports:
    report.load_data()
    report.process()
    report.export()



from abc import ABC, abstractmethod
class RobotCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass
class PickCommand(RobotCommand):
    def execute(self):
        print("Picking object")
    def undo(self):
        print("Undo Pick")
class PlaceCommand(RobotCommand):
    def execute(self):
        print("Placing object")
    def undo(self):
        print("Undo Place")
class MoveCommand(RobotCommand):
    def execute(self):
        print("Moving robot")
    def undo(self):
        print("Undo Move")
commands = [PickCommand(), PlaceCommand(), MoveCommand()]
for command in commands:
    command.execute()
print()
for command in commands:
    command.undo()



from abc import ABC, abstractmethod
class MLModel(ABC):
    @abstractmethod
    def train(self, data):
        pass
    @abstractmethod
    def predict(self, x):
        pass
    @abstractmethod
    def evaluate(self, test_set):
        pass
class LinearRegressionModel(MLModel):
    def train(self, data):
        print("Training Linear Regression Model")
    def predict(self, x):
        return x * 2
    def evaluate(self, test_set):
        print("Evaluating Linear Regression Model")
class DecisionTreeModel(MLModel):
    def train(self, data):
        print("Training Decision Tree Model")
    def predict(self, x):
        return x + 10
    def evaluate(self, test_set):
        print("Evaluating Decision Tree Model")
models = [
    LinearRegressionModel(),
    DecisionTreeModel()
]
for model in models:
    model.train("training data")
    print("Prediction =", model.predict(5))
    model.evaluate("test data")

def email_sender(message):
    print("Email:", message)
def sms_sender(message):
    print("SMS:", message)
def push_sender(message):
    print("Push Notification:", message)
choice = "sms"
if choice == "email":
    email_sender("Hello")
elif choice == "sms":
    sms_sender("Hello")
elif choice == "push":
    push_sender("Hello")


from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailSender(Notifier):
    def send(self, message):
        print("Email:", message)
class SMSSender(Notifier):
    def send(self, message):
        print("SMS:", message)
class PushSender(Notifier):
    def send(self, message):
        print("Push Notification:", message)
notifiers = [
    EmailSender(),
    SMSSender(),
    PushSender()
]
for n in notifiers:
    n.send("Welcome")


from abc import ABC, abstractmethod
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
        print("MP3 file loaded")
    def play(self):
        print("Playing MP3")
    def stop(self):
        print("Stopping MP3")
class WAVPlayer(MediaPlayer):
    def load(self):
        print("WAV file loaded")
    def play(self):
        print("Playing WAV")
    def stop(self):
        print("Stopping WAV")
class AACPlayer(MediaPlayer):
    def load(self):
        print("AAC file loaded")
    def play(self):
        print("Playing AAC")
    def stop(self):
        print("Stopping AAC")
players = [
    MP3Player(),
    WAVPlayer(),
    AACPlayer()
]
for player in players:
    player.load()
    player.play()
    player.stop()
    print()



from abc import ABC, abstractmethod
class Sensor(ABC):
    def __init__(self):
        self.__raw_reading = 0
        self.__calibration_factor = 1
    @abstractmethod
    def read_value(self):
        pass
    @abstractmethod
    def calibrate(self):
        pass
    def get_reading(self):
        return self.read_value()
class TemperatureSensor(Sensor):
    def read_value(self):
        print("Temperature Sensor")
        return 35
    def calibrate(self):
        print("Temperature calibration successful")
class PressureSensor(Sensor):
    def read_value(self):
        print("Pressure Sensor")
        return 120
    def calibrate(self):
        print("Pressure calibration successful")
class HumiditySensor(Sensor):
    def read_value(self):
        print("Humidity Sensor")
        return 65
    def calibrate(self):
        print("Humidity calibration successful")
sensors = [
    TemperatureSensor(),
    PressureSensor(),
    HumiditySensor()
]
for sensor in sensors:
    sensor.calibrate()
    print("Reading =", sensor.get_reading())
    print()
