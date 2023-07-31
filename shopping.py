class Product:
    def __init__(self, name, price, qty = 0):
        self.name = name
        self.price = price
    
class Book(Product):
    pass

class Electronic(Product):
    pass

class Clothing(Product):
    pass

class Cart:
    def __init__(self):
        self.cart = []
    
    def additem(self, product, qty):
        if product in self.cart:
            product.qty += qty
        else:
            product.qty = qty
            self.cart.append(product)
    
    def removeitem(self, product, qty):
        if product in self.cart:
            if product.qty == qty:
                self.cart.remove(product)
            elif product.qty > qty:
                product.qty -= qty
            else:
                print('not enough to remove')
        else:
            print('error item not found in shopping cart')
            
    def display_products(self):
        for i in self.cart:
            print(f'{i.name} x {i.qty} - {i.price}')
            
    def total(self):
        total = 0
        for i in self.cart:
            total += i.price
        return total
            
book = Book("Python Crash Course", 29.99)
electronic = Electronic("Headphones", 49.99)
clothing = Clothing("T-Shirt", 19.99)

cart = Cart()
cart.additem(book, 2)
cart.additem(electronic, 1)
cart.additem(clothing, 3)

cart.display_products()
print(f"Total Price: ${cart.total()}")            
            
            
            
            
            
            
            
            
            
            