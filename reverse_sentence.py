in1 = str(input('Enter a sentence: '))

def reverse_sentence(x):
    strsplit = x.split(' ')
    reverse = strsplit[::-1]   
    
    print(' '.join(reverse))
    
reverse_sentence(in1)