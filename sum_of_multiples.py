n = int(input('Enter an integer: '))

def sum_of_multiples(intinput):
    new_list = []
    p1 = 3
    p2 = 5
    
    for i in range(intinput):
        if i * p1 < intinput:
            if i * p1 not in new_list:
                new_list.append(i * p1)
        if i * p2 < intinput:
            if i * p2 not in new_list:
                new_list.append(i * p2)
    return sum(new_list)

print(sum_of_multiples(n))
