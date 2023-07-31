input_str1 = str(input("Input 1: "))
input_str2 = str(input("Input 2: "))

def are_anagrams(str1,str2):
    def create_char_count_dict(s):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char,0) + 1
        return char_count
    
    char_count_str1 = create_char_count_dict(str1)
    char_count_str2 = create_char_count_dict(str2)
    
    return char_count_str1 == char_count_str2

print(are_anagrams(input_str1,input_str2))