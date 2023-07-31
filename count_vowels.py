input_str = str(input("input: "))

def count_vowels(strinput):
    new_dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in strinput.lower():
        if i in new_dict:
            new_dict[i] += 1
    return sum(new_dict.values())
    
print(count_vowels(input_str))

