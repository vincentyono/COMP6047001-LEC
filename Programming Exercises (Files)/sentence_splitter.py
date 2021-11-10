# Program Exercises (Files)
# -----------------------------------------------------------------------------------------------
# 4. A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence 
#    splitting includes (but isn't limited to) the following rules:
#
#       Sentence boundaries occur at one of "." (periods), "?" or "!", except that .
#       Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
#
#                a) Periods followed by a digit with no intervening whitespace are not sentence boundaries.
#                b) Periods followed by whitespace and then an upper case letter, but preceded by any of short 
#                list of titles are not sentence boundaries.
#                c) Sample titles include Mr., Mrs., Dr., and so on.
#                d) Periods internal to a sequence of letters with no adjacent whitespace are not sentence 
#                boundaries
#                e) (for example, www.aptex.com, or e.g).
#                f) Periods followed by certain kinds of punctuation (notably comma and more periods) are
#                   probably not sentence boundaries.
#
#    Your task here is to write a program that given the name of a text file can write its content with each sentence on a 
#    separate line. Test your program with the following short text:
#
#    Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he 
#    didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. 
#    
#    The result should be:
#
#    Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
#    Did he mind?
#    Adam Jones Jr. thinks he didn't.
#    In any case, this isn't true...
#    Well, with a probability of .9 it isn't
# -----------------------------------------------------------------------------------------------

def sentence_splitter(sentence: str) -> str:
    text = sentence.split()
    for i in range(len(text) - 1):
        if text[i][-1] == "?" or text[i][-1] == "!":
            text[i] += "\n"

        elif text[i] == "Mr." or text[i] == "Ms." or text[i] == "Mrs." or text[i] == "Dr." or text[i] == "Jr.": 
            continue

        elif text[i][-1] == "." and text[i + 1][0].isupper():
            text[i] += "\n"

        else:
            text[i] += " "

    return "".join(text)

print(sentence_splitter("Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. "))
