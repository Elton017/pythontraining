orig_list = ['apple', 'banana', 'orange', 'grapes', 'kiwi']

lengthinput = int(input("Input an integer"))

def filter_strings(input_list):
    new_list = []
    for i in input_list:
        if len(str(i)) > lengthinput:
            new_list.append(i)
    return new_list

print(filter_strings(orig_list))