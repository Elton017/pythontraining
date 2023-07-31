class ShoppingCart:
    def __init__(self):
        self.shopping = {}
        
    def add_item(self, item, price):
        self.shopping[item] = price
    
    def remove_item(self, item):
        if item in self.shopping:
            del self.shopping[item]
    
    def get_total_price(self):
        total = sum(self.shopping.values())
        return total
    
    def print_receipt(self):
        for item, price in self.shopping.items():
            print(f'{item}: {price}')
        total_price = self.get_total_price()
        print(f'Total: {total_price}')
            
cart = ShoppingCart()
cart.add_item("Apple", 2.0)
cart.add_item("Banana", 1.5)
cart.add_item("Orange", 3.0)

cart.print_receipt()

cart.remove_item("Banana")

cart.print_receipt()
            