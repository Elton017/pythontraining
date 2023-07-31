in1 = str(input('Enter 1st list of spaced integers: '))
in2 = str(input('Enter 2nd list of spaced integers: '))

def find_union(list1,list2):
    l1 = list1.split()
    l2 = list2.split()
    
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
    
    return n1.union(n2)

print(find_union(in1,in2))