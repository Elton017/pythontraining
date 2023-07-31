in1 = str(input('Enter list of spaced integers: '))

def find_second_smallest(list1):
    l1 = list1.split()
    new_list = []
    
    for i in l1:
        try: 
            new_list.append(int(i))
        except ValueError:
            continue
        
    new_list.remove(min(new_list))
    
    return min(new_list)

print(find_second_smallest(in1))
