input_str1 = str(input("Input 1: "))
input_str2 = str(input("Input 2: "))

def are_anagrams(str1,str2):
    list1 = []
    list2 = []
    
    for i in str1:
        list1.append(i)
    for x in str2:
        list2.append(x)
    
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False
    
    
    
print(are_anagrams(input_str1,input_str2))