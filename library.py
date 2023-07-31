from abc import ABC, abstractmethod

class Library(ABC):
    @abstractmethod
    def removebook(self):
        pass
    
    @abstractmethod
    def addbook(self):
        pass
    
    @abstractmethod
    def displaybooks(self):
        pass
    
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
class FictionBook(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self.genre = 'Fiction'

class NonFictionBook(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self.genre = 'Non-Fiction'

class Member(Library):
    def __init__(self, name, idno):
        self.name = name
        self.idno = idno
        self.borrowed = []
    
    def removebook(self, isbn):
        for i in self.borrowed:
            if i.isbn == isbn:
                self.borrowed.remove(i)
    
    def addbook(self, book = Book):
        self.borrowed.append(book)
            
    def displaybooks(self):
        for i in self.borrowed:
            print(f'Title: {i.title}, Author: {i.author}, ISBN: {i.isbn}')
    
class LibraryManager(Library):
    def __init__(self, name, idno):
        self.name = name
        self.idno = idno
        self.books = []
    
    def removebook(self, isbn):
        for i in self.books:
            if i.isbn == isbn:
                self.books.remove(i)
                 
    def addbook(self, book = Book):
        self.books.append(book)             
                 
    def displaybooks(self):
        for i in self.books:
            print(f'Title: {i.title}, Author: {i.author}, ISBN: {i.isbn}')             
                 
b1 = FictionBook('hello', 'jon', 1234124)
b2 = NonFictionBook('bye', 'jeff', 213415)
guy = Member('Jeff', 1)               
guy.addbook(b1)
guy.addbook(b2)
guy.displaybooks()
                 
                 
                 
                 
                 
                 
                 
                 
                 