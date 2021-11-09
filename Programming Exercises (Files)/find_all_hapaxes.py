import re

def find_all_hapaxes(filename):
    f = open(filename, "r")
    lines = f.readlines()
    dictionary = {}
    hapaxes = []
    for line in lines:
        res = re.sub(r"[^\w\s]", "", line) # removes punctuations
        res = res.lower().split()
        for word in res:
            dictionary[word] = dictionary.get(word, 0) + 1
    
    for i in dictionary.keys():
        if dictionary[i] == 1:
            hapaxes.append(i)
    return hapaxes # list of all hapaxes

print(find_all_hapaxes("ebook.txt"))