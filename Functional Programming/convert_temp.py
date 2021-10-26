# Question 5
# -----------------------------------------------------------------------------------------------
#
# Write a function called convert temp() that takes no arguments. This function obtains a temperature in 
# Fahrenheit from the user and uses two helper functions to convert this temperature to Celsius and Kelvin. 
# Write a helper function called convert to celsius() that takes a single argument in Fahrenheit and returns 
# the temperature in Celsius using the formula
#
#               Tc = (5 / 9) * (Tf - 32)
#
# where Tc is the temperature in Celsius and Tf is the temperature in Fahrenheit. Write another helper 
# function called convert to kelvin() that takes a single argument in degrees Celsius and returns degrees 
# Kelvin using the formula
#
#               Tk = Tc + 273.15
#
# where Tk is the temperature in Kelvin. Use these two functions within your convert temp() function to 
# display (i.e., print) the temperatures for the user. The convert temp() does not return anything.
#
# -----------------------------------------------------------------------------------------------
#
# The following demonstrates the proper behavior of this function:
# convert_temp()
# Enter a temperature in Fahrenheit: 32
# The temperature in Fahrenheit is: 32
# The temperature in Celsius is: 0.0
# The temperature in Kelvin is: 273.15
# convert_temp()
# Enter a temperature in Fahrenheit: 80
# The temperature in Fahrenheit is: 80
# The temperature in Celsius is: 26.666666666666668
# The temperature in Kelvin is: 299.81666666666666
#
# -----------------------------------------------------------------------------------------------

def convert_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def convert_to_kelvin(celsius):
    return celsius + 273.15

def convert_temp():
    fahrenheit = eval(input("Enter a temperature in Fahrenheit: "))
    celsius = convert_to_celsius(fahrenheit)
    kelvin = convert_to_kelvin(celsius)

    print(f"The temperature in Fahrenheit is: {fahrenheit}")
    print(f"The temperature in Celsius is: {celsius}")
    print(f"The temperature in Kelvin is: {kelvin}")

convert_temp()