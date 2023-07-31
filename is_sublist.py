
#list1 = str(input('Enter 1st list of spaced integers: '))
#list2 = str(input('Enter 2nd list of spaced integers: '))
list1 = '1 2 3 4 5 6'
list2 = '3 4 5 6'

def is_sublist(l1,l2):
    li1 = l1.split()
    li2 = l2.split()
    
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
         
    n1 = list_sort(li1)
    n2 = list_sort(li2)
    
    if len(n1) >= len(n2):
        for i in n2:
            if i not in n1:
                return False
    else:
        for i in n1:
            if i not in n2:
                return false
    return True
    
print(is_sublist(list1,list2))

#def is_sublist(l1, l2):
#    for i in l2.split():
#        if i not in l1:
#            return False
#    return True
