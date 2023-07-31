int_input = int(input('Enter a integer: '))

def is_prime(intinput):
    if intinput <= 2:
        return False
    for i in range(2,intinput):
        if intinput % i == 0:
            return False
    else:
        return True

if is_prime(int_input):
    print("Is a prime")
else:
    print("Not a prime")