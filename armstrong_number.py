int_input = int(input('Enter an integer: '))

def is_armstrong_number(intinput):
    new_list = []
    armstrong = 0
    power = len(str(intinput))
    
    for i in str(intinput):
        new_list.append(int(i))
    for x in new_list:        
        armstrong += x ** power
    
    if intinput == armstrong:
        print(f'{intinput} is an Armstrong number')
    else:
        print(f'{intinput} is not an Armstrong number')

is_armstrong_number(int_input)