# Question 4
# -----------------------------------------------------------------------------------------------
#
# The aspect ratio of an image describes the relationship between the width and height. Aspect ratios are 
# usually expressed as two numbers separated by a colon that represent width and height respectively. 
# Common aspect ratios in photography are 4:3, 3:2, and 16:9. An image that has an aspect ratio of x : y 
# means that for every x inches of width you will have y inches of height no matter the size of the image 
# (and, of course, you can use any unit of length, not just inches, and even abstract units such as pixels). 
# Suppose you are writing a blog and you have an image that is m units wide and n units high but your blog 
# only has space for an image that is z units wide (where z is less than m). Write a function called calc new 
# height() that returns the height the image must be in order to preserve the aspect ratio (i.e., a height
# that will not distort the image). This function takes no arguments and prompts the user for the current 
# width, the current height, and the desired new width. In addition to returning the new height, this function 
# also prints the value. The new height is a float regardless of the types of the values the user entered.
# The following demonstrates the proper behavior of this function:
#
# -----------------------------------------------------------------------------------------------
#
# calc_new_height()
# Enter the current width: 800
# Enter the current height: 560
# Enter the desired width: 370
# The corresponding height is: 259.0
# 259.0
#
# -----------------------------------------------------------------------------------------------

def calc_new_height():
    current_width = eval(input("Enter the current width: "))
    height = eval(input("Enter the current height: "))
    desired_width = eval(input("Enter the desired width: "))

    #type float
    new_height = (height / current_width) * desired_width

    print(f"The corresponding height is: {new_height}")
    return new_height

new_height = calc_new_height()
print(new_height)