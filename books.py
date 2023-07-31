class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
        return self.books

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
        return self.books

    def display_available_books(self):
        for book in self.books:
            if book.available:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                else:
                    print("no book")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                else:
                    print("book already returned")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    print(f'Title: {title}, Author: {book.author}, this book is available')
                else:
                    print(f'Title: {title}, Author: {book.author}, this book is not available')



