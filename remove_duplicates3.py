#in1 = str(input('Enter list of spaced integers: '))
in1 = '1 2 3 4 5 6 1 1 5 5 '

def remove_duplicates(l1):
    list1 = l1.split()
    
    def list_sort(lists):
        sorted_list = []
        for i in lists:
            try:
                num = int(i)
                sorted_list.append(num)
            except ValueError:
                continue
        return sorted_list
    
    list2 = list_sort(list1)
    new_list = []
    
    for i in list1:
        num = int(i)
        if num not in new_list:
            new_list.append(num)
            
    return new_list

print(remove_duplicates(in1))