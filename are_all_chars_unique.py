n = str(input('Enter a list of spaced integers: '))

def are_all_characters_unique(strinput):
    seen_chars = set()
    
    for i in strinput:
        if i in seen_chars:
            return False
        seen_chars.add(i)
    
    return True

result = are_all_characters_unique(n)

print(result)