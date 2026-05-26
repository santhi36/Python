class Product:
    tax = 10
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def total(self):
        return self.price + (self.price * Product.tax / 100)
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
print(p1.name, p1.total())
print(p2.name, p2.total())



#
class Student:
    total_students = 0
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1
    def is_passed(self):
        return self.marks >= 40
    def curve_marks(self):
        self.marks += self.marks * 0.10
s1 = Student("Ravi", 50)
s2 = Student("Sita", 70)
s1.curve_marks()
s2.curve_marks()
print(s1.name,s1.marks)
print(s2.name,s2.marks)


class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3


if Book.is_valid_title("Python"):
    b1 = Book("Python", "Guido")

if Book.is_valid_title("Java"):
    b2 = Book.from_string("Java-James")

print("Total Books:", Book.total_books)
