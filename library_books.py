class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False
        
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.borrowed:
                book.borrowed = True
                return f"You have borrowed {book.title}."
        return "Book not found or already borrowed."
    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.borrowed:
                book.borrowed = False
                return f"You have returned {book.title}."
        return "Book not found or already returned."
    
    def display_books(self):
        for book in self.books:
            print(book)
# Creating books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
book3 = Book("1984", "George Orwell", "9780451524935")

# Creating a library
library = Library()

# Adding books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all books in the library
library.display_books()

# Borrowing and returning books
print(library.borrow_book("9780061120084"))
print(library.borrow_book("9780451524935"))
print(library.return_book("9780061120084"))

# Display all books in the library after borrowing and returning
library.display_books()