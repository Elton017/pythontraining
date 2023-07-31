#in1 = str(input('Enter list of spaced integers: '))
in1 = '1 2 3 4 5 6 '

def find_second_largest(l1):
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
    list2.remove(max(list2))
    
    return max(list2)

print(find_second_largest(in1))
    