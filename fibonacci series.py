number_input = int(input("Enter the number of terms in the Fibonacci series: "))

def fibonacci(number):
    fib = [0,1]
    for i in range(number-2): 
        fib.append(fib[i] + fib[i+1])
    print("Fibonacci Series: " + ", ".join(str(x) for x in fib))
    
fibonacci(number_input)
