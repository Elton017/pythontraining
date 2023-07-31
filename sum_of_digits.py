number_input = int(input("Enter a positive integer: "))

def sum_of_digits(number):
    new_list = []
    total = 0
    for i in str(number):
        new_list.append(i)
    for i in new_list:
        total += int(i)
    return total
        
result = sum_of_digits(number_input)
print(result)