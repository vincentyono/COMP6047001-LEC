# Programming Exercises (Files)
# -----------------------------------------------------------------------------------------------
# 2. Write a program that given a text file will create a new text file in which all the lines from the original file are numbered 
#    from 1 to n (where n is the number of lines in the file).
# -----------------------------------------------------------------------------------------------

def add_number(input_file: str, output_file) -> None: # Python 3.10.0 feature
    with open(input_file, "r", encoding="utf-8") as inputfile:
        lines = inputfile.readlines()

    with open(output_file, "w", encoding="utf8") as outputfile:
        for i in range(len(lines)):
            print(f"{i + 1}. {lines[i]}", file=outputfile, end="")

add_number("ebook.txt", "numbered_ebook.txt")