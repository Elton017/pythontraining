class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        
    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Price: {self.price}'
        
class BookCatalog:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False
    
    def search_by_author(self, author):
        authorbooks = []
        for book in self.books:
            if book.author == author:
                authorbooks.append(str(book))
        return authorbooks
    
    def search_by_genre(self, genre):
        genrebooks = []
        for book in self.books:
            if book.genre == genre:
                genrebooks.append(str(book))
        return genrebooks
    
    def get_total_price(self):
        totalprice = 0
        for book in self.books:
            totalprice += book.price
        return totalprice
        
    
book1 = Book('bigdog', 'jeff', 'fiction', 100)
book2 = Book('dog', 'jff', 'fiction', 100)
book3 = Book('big', 'jeff', 'fiction', 100)

catalog = BookCatalog()
catalog.add_book(book1)
catalog.add_book(book2)
catalog.add_book(book3)

print(catalog.remove_book(book2))
print(catalog.search_by_author('jeff'))
print(catalog.search_by_genre('fiction'))
print(catalog.get_total_price())