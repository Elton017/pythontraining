input1 = input("Enter a list of space-seperated integers: ")
input2 = int(input('Enter an integer to count its occurrences: '))

def count_occurrences(inputlist, cnt):
    cunt = str(cnt)
    
    x = inputlist.count(cunt)
    return x
    
result = count_occurrences(input1,input2)

print(f'Occurences of {input2} in the list: {result}')