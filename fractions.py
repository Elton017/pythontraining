class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        
    def __str__(self):
        return f'{self.num}/{self.den}'
    
    def simplify(self):
        gcd = 0
        for i in range(1, int(min(self.num, self.den)) + 1):
            if self.num % i == 0 and self.den % i ==0:
                gcd = i
        if gcd >= 2:
            self.num = self.num // i
            self.den = self.den // i
        return f'{self.num}/{self.den}'
    
    def add(self, other):
        self.num = self.num * other.den + other.num * self.den
        self.den = self.den * other.den
        self.simplify()
        return f'{self.num}/{self.den}'
    
    def subtract(self, other):
        self.num = self.num * other.den - other.num * self.den
        self.den = self.den * other.den
        self.simplify()
        return f'{self.num}/{self.den}'
    
    def multiply(self, other):
        self.num = self.num * other.num
        self.den = self.den * other.den        
        self.simplify()
        return f'{self.num}/{self.den}'
    
    def divide(self, other):
        self.num = self.num * other.den
        self.den = self.den * other.num
        self.simplify()
        return f'{self.num}/{self.den}'
        
    
f1 = Fraction(4, 8)
print(f1.simplify())

f2 = Fraction(3, 6)
print(f2)

f3 = f1.add(f2)
print(f3)

f4 = f1.subtract(f2)
print(f4)

f5 = f1.multiply(f2)
print(f5)

f6 = f1.divide(f2)
print(f6)