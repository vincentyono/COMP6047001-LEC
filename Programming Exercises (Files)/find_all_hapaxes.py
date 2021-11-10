# Programming Exercises (Files)
# -----------------------------------------------------------------------------------------------
# 1. A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a 
#    language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its 
#    hapaxes. Make sure your program ignores capitalization. [open http://www.gutenberg.org/ and download an e-book 
#    as plain text, use the file for texting your program]
# -----------------------------------------------------------------------------------------------

import re

def find_all_hapaxes(filename: str) -> list[str]: # Python 3.10.0 feature
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
    
    f.close()

    return hapaxes # list of all hapaxes

print(find_all_hapaxes("ebook.txt"))