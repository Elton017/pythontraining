input1 = str(input('Enter 1st list of spaced integers: '))
input2 = str(input('Enter 2nd list of spaced integers: '))

def find_intersection(l1,l2):
    list1 = l1.split()
    list2 = l2.split()
    
    def list_sort(lists):
        sorted_list = []
        for i in lists:
            try:
                num = int(i)
                if num not in sorted_list:
                    sorted_list.append(num)
            except ValueError:
                continue
        return sorted_list
         
    n1 = set(list_sort(list1))
    n2 = set(list_sort(list2))
    
    common_elements = n1.intersection(n2)
    
    return common_elements

print(find_intersection(input1,input2))
    