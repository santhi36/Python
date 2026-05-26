class Book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed =
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        if len(book.title) > 7 and book.is_borrowed == False:
            self.books.append(book)
    def display_books(self):
        for b in self.books:
            print(b.title, b.author, b.is_borrowed)
class User:
    def __init__(self, name, books_borrowed=0):
        self.name = name
        self.books_borrowed = books_borrowed
    def borrow_book(self, library, title, borrow_limit):
        if self.books_borrowed < borrow_limit:
            for b in library.books:
                if b.title == title and b.is_borrowed == False:
                    b.is_borrowed = True
                    self.books_borrowed += 1
                    print(self.name, "borrowed", b.title)
                    return
            print("Book not available")
        else:
            print("Borrow limit exceeded")
b1 = Book("PythonBook", "James", False)
b2 = Book("Java", "John", False)
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
u1 = User("santhi")
lib.display_books()
u1.borrow_book(lib, "PythonBook", 2)
lib.display_books()

#
class Product:
    def __init__(self,price,name,quality):
        self.name=name
        self.price=price
        self.quality=quality




