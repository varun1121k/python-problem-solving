# Day 13 - Library System

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Borrowed:", title)
                return
        print("Book not available")

    def show_books(self):
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(book.title, "-", status)


lib = Library()
lib.add_book(Book("Python"))
lib.add_book(Book("DSA"))

lib.borrow_book("Python")
lib.show_books()
