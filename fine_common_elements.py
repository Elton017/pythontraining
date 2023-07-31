input1 = str(input('Enter 1st list of spaced integers: '))
input2 = str(input('Enter 2nd list of spaced integers: '))

def find_common_elements(l1,l2):
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
         
    n1 = list_sort(list1)
    n2 = list_sort(list2)
    final_list = []
    
    for i in n1:
        if i in n2:
            final_list.append(i)
    
    return final_list

print(find_common_elements(input1,input2))
    