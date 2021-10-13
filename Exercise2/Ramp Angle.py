# Ramp Angle (15 points)
# -----------------------------------------------------------------------------------------------
#
# Suppose you need push a cart on a ramp as shown in the figure below.
#
#                              \
#                               \[] <- F
#                            ___θ\
#
# Ignoring friction, the force (in Newtons) required to push the cart mass (in kilograms) up a ramp
# of angle θ (in degrees) is determined by the formula:
#                                   
#                       F = m × g × sinθ
#
# Where g is the acceleration due to gravity, which is a constant 9.8 m/s2.
#
# Given this information, write a program that prompts the user to enter the Force and mass of
# the cart. (Store the value of g as a ‘constant’ in your program) The program should then use the
# formula to calculate the angle of the ramp. Format your output to 1 decimal place.
#
# Note: The trigonometric functions in the math module returns the values in radians. In addition
# to the arc sin function (asin), you will need to use the degrees function to convert the angle to
# degrees.
#
# -----------------------------------------------------------------------------------------------
# Sample output:
#
# Enter the mass of the cart (in kg): 100
# Enter the force to push the cart (in N): 250
# The angle of the ramp is 14.8 degrees
#
# -----------------------------------------------------------------------------------------------

import math

mass = eval(input("Enter the mass of the cart (in kg): "))
force = eval(input("Enter the force to push the cart (in N): "))

gravity = 9.8
angle_radians = math.asin(force / (mass * gravity))
angle_degrees = math.degrees(angle_radians)

print(f"The angle of the ramp is {round(angle_degrees, 1)} degrees")