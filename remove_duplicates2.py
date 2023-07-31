#pretty shit code this could be better
from collections import OrderedDict

n = str(input('Enter a list of spaced integers: '))

def remove_duplicates(intinput):
    splitlist = intinput.split(' ')
    new_dict = OrderedDict()
    
    for i in splitlist:
        try:
            num = int(i)
            if num not in new_dict:
                new_dict[num] = None
        except ValueError:
            continue
        
    new_list = set(new_dict.keys())
    return new_list

print(remove_duplicates(n))
