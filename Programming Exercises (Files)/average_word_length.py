# Programming Exercises (Files)
# -----------------------------------------------------------------------------------------------
# 3. Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the 
#    word tokens in the text, divided by the number of word tokens). [open http://www.gutenberg.org/ and download an 
#    e-book as plain text, use the file for texting your program]
# -----------------------------------------------------------------------------------------------

import re

def average_word_length(filename: str) -> float: # Python 3.10.0 feature
    with open(filename, "r") as f:
        lines = f.readlines()
        words = []
        sum = 0

    for line in lines:
        res = re.sub(r"[^\w\s]", "", line) # removes punctuations
        res = res.split() 
        for word in res:
            words.append(word)
            sum += len(word)
    
    return sum / len(words)

print(average_word_length("ebook.txt"))