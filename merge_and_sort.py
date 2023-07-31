#in1 = str(input('Enter 1st list of spaced integers: '))
#in2 = str(input('Enter 2nd list of spaced integers: '))
in1 = '1 3 5 7'
in2 = '2 4 6 8'

def merge_and_sort(list1,list2):
    li1 = list1.split()
    li2 = list2.split()
    
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
         
    n1 = list_sort(li1) + list_sort(li2)
    
    return n1

def remove_duplicates(list1):
    x = set(list1)
    y = list(x)
    return y

print(remove_duplicates(merge_and_sort(in1,in2)))
    