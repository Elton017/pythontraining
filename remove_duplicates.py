original_list = [1, 2, 2, 3, 1, 4, 2, 5, 1]

def remove_duplicates(list_input):
    new_list = []
    for i in list_input:
        if i not in new_list:
            new_list.append(i)
    return new_list
    
result = remove_duplicates(original_list)
print("New List: " + str(result))