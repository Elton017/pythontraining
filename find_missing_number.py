in1 = '1 3 2 5 6 7 8'

def find_missing_number(x):
    listsplit = x.split()
    listint = []
    for i in listsplit:
        try:
            listint.append(int(i))
        except ValueError:
            continue
    
    for i in range(1,len(listint)+1):
        if i not in listint:
            return i
    
result = find_missing_number(in1)
print(result)