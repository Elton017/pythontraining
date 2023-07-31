in1 = 'hello world hello world hello'.lower()

def word_frequency_counter(x):
    splitlist = x.split(' ')
    new_dict = {}
    for i in splitlist:
        if i not in new_dict:
            new_dict[i] = 0
        if i in new_dict:
            new_dict[i] += 1
    return new_dict

print(word_frequency_counter(in1))
