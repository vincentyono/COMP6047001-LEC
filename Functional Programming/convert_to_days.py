# Question 1
# -----------------------------------------------------------------------------------------------
#
# Write a function called convert to days() that takes no parameters. Have your function prompt the user 
# to input numbers of hours, minutes, and seconds. Write a helper function called get days() that uses these 
# values and converts them to days in float form (fractions of a day are allowed). get days() should return the 
# number of days. Use this helper function within the convert to days() function to display the numbers of 
# days to the user. The built-in function round() takes two arguments: a number and an integer indicating 
# the desired precision (i.e., the desired number of digits beyond the decimal point). Use this function to 
# round the number of days four digits after the decimal point.
#
# -----------------------------------------------------------------------------------------------
# The following demonstrates the proper behavior of convert to days():
# convert_to_days()
# Enter number of hours: 97
# Enter number of minutes: 54
# Enter number of seconds: 45
# The number of days is: 4.0797
# -----------------------------------------------------------------------------------------------

def get_days(hours, minutes, seconds):
    # convert hours, minutes, seconds to days
    return (hours / 24) + ((minutes / 60) / 24) + (((seconds / 60) / 60) / 24) 


def convert_to_days():
    hours = float(input("Enter number of hours: "))
    minutes = float(input("Enter number of minutes: "))
    seconds = float(input("Enter number of seconds: "))

    return round(get_days(hours, minutes, seconds), 4)

print(convert_to_days())