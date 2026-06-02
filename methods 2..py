class Student:
    total_students = 0
    passing_mark = 40
    students = []
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1
        Student.students.append(self)
    def result(self):
        if self.marks >= Student.passing_mark:
            return "Passed"
        else:
            return "Failed"
    @classmethod
    def curve_marks(cls, percentage):
        for student in cls.students:
            student.marks += student.marks * percentage / 100
            if student.marks > 100:
                student.marks = 100
    @staticmethod
    def grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"
s1 = Student("Karishma", 35)
s2 = Student("Shameena", 70)
s3 = Student("Zoya", 40)
print("Before Curving:")
for s in Student.students:
    print(s.name, s.marks, s.result(), Student.grade(s.marks))
Student.curve_marks(10)
print("\nAfter Curving:")
for s in Student.students:
    print(s.name, s.marks, s.result(), Student.grade(s.marks))
print("\nTotal Students:", Student.total_students)


class Product:
    tax_rate = 18
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
    def final_price(self):
        return self.base_price + (self.base_price * Product.tax_rate / 100)
    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate
    @staticmethod
    def valid_price(price):
        return price >= 0 and price < 100000
p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 30000)
print("Before Tax Change:")
for p in [p1, p2]:
    print(p.name,"Final price:",p.final_price(),"Valid:",Product.valid_price(p.base_price))
Product.change_tax_rate(12)
print("\nAfter Tax Change:")
for p in [p1, p2]:
    print(p.name,"Final price:",p.final_price(),"Valid:",Product.valid_price(p.base_price))


class Employee:
    min_experience = 3
    def __init__(self, name, experience, department):
        self.name = name
        self.experience = experience
        self.department = department
    def check_promotion(self):
        if self.experience >= Employee.min_experience:
            return "Eligible for promotion"
        else:
            return "Not Eligible"
    @classmethod
    def update_criteria(cls, new_exp):
        cls.min_experience = new_exp
    @staticmethod
    def valid_department(dept):
        valid = ["HR", "Tech", "Admin"]
        return dept in valid
e1 = Employee("Karishma", 2, "HR")
e2 = Employee("Kavitha", 4, "Tech")
e3 = Employee("Nandini", 5, "Admin")
print("Before changing criteria:")
for e in [e1, e2, e3]:
    print(e.name,"-",e.department,"-",e.check_promotion(),"- valid dept:",Employee.valid_department(e.department))
Employee.update_criteria(4)
print("\nAfter changing criteria:")
for e in [e1, e2, e3]:
    print(e.name,"-",e.department,"-",e.check_promotion(),"- valid dept:",Employee.valid_department(e.department))




class Loan:
    interest_rate = 10
    def __init__(self, borrower_name, principal):
        self.borrower_name = borrower_name
        self.principal = principal
    def total_payable(self):
        return self.principal+(self.principal * Loan.interest_rate / 100)
    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
    @staticmethod
    def check_eligibility(salary):
        return salary > 25000
l1 = Loan("Karishma", 50000)
l2 = Loan("Santhi", 60000)
print("Before Interest Update:")
print(l1.borrower_name,l1.total_payable(),Loan.check_eligibility(30000))
print(l2.borrower_name,l2.total_payable(),Loan.check_eligibility(20000))
Loan.update_interest_rate(12)
print("\nAfter Interest Update:")
print(l1.borrower_name,l1.total_payable(),Loan.check_eligibility(30000))
print(l2.borrower_name,l2.total_payable(),Loan.check_eligibility(20000))


class Course:
    total_courses = 0
    min_duration = 30
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.enrolled_students = []
        Course.total_courses += 1
    def enroll(self, student):
        self.enrolled_students.append(student)
    @classmethod
    def update_min_duration(cls, new_duration):
        cls.min_duration = new_duration
    @staticmethod
    def check_duration(duration):
        return duration >= 36
c1 = Course("Python", 60)
c2 = Course("Java", 45)
c1.enroll("Karishma")
c2.enroll("Viharika")
print("Before update:")
print(c1.title, c1.enrolled_students, Course.check_duration(c1.duration))
print(c2.title, c2.enrolled_students, Course.check_duration(c2.duration))
Course.update_min_duration(40)
print("\nAfter updating Minimum Duration:")
print("Minimum Duration:", Course.min_duration)
print("Total Courses:", Course.total_courses)




class Vehicle:
    svc = 0.1
    def __init__(self, m, km, sh):
        self.model = m
        self.km_run = km
        self.sv_history = sh
    def calc(self):
        return self.km_run * self.svc
    @classmethod
    def update(cls, sv):
        cls.svc = sv
    @staticmethod
    def eligible(v):
        return 0 < v < 16



class Inventory:
    total = 0
    min_stock = 100
    def __init__(self, n):
        self.name = n
        self.stock = {}
    def add(self, item, quantity):
        self.stock[item] = quantity
        Inventory.total += 1
    def remove(self, item):
        if item in self.stock:
            self.stock.pop(item)
            Inventory.total -= 1
        else:
            print("Item not found")
    @classmethod
    def update(cls, n):
        cls.min_stock = n
    @staticmethod
    def valid(s):
        return s > Inventory.min_stock


class HostelRoom:
    base_price = 900
    def __init__(self, rno, nb, gn):
        self.room_no = rno
        self.nights_booked = nb
        self.guest_name = gn
    def calc(self):
        return self.base_price * self.nights_booked
    @classmethod
    def update(cls, np):
        cls.base_price = np
    @staticmethod
    def valid(n):
        return 0 < n < 15




class LibraryMember:
    total_active_members = 0
    borrowing_limit = 5
    def __init__(self, name, books_borrowed):
        self.name = name
        self.books_borrowed = books_borrowed
        self.is_active = True
        LibraryMember.total_active_members += 1
    def borrow_books(self, no):
        if self.books_borrowed + no <= LibraryMember.borrowing_limit:
            self.books_borrowed += no
        else:
            print("Borrow limit reached")
    @classmethod
    def update(cls, np):
        cls.borrowing_limit = np
    @staticmethod
    def valid(title):
        return len(title) > 6

