in1 = int(input('Enter a positive integer: '))

def sum_of_squares(n):
    new_list = []
    
    for i in range(n+1):
        new_list.append(i**2)
        
    return sum(new_list)

print(sum_of_squares(in1))