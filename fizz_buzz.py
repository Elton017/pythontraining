intinput = int(input("Enter an integer: "))

def fizz_buzz(int_input):
    for i in range(1, int_input + 1):
        if i % 3 == 0 and i %5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
            
fizz_buzz(intinput)