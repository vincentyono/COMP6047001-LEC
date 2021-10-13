# Runway Length (15 points)
# -----------------------------------------------------------------------------------------------
#
# Given an airplane’s acceleration, a, and take-off speed, v, the minimum runway length needed
# for the airplane to take off is computed using the formula (v ** 2)/(2 * a)
#
# Write a program that prompts the user to enter the speed in meters per second (m/s) and the
# acceleration in meters per second squared (m/s ** 2). The program should calculate and display the
# minimum runway length. Format the result to four decimal places. (For this question, assume
# that all values entered are positive.)
#
# -----------------------------------------------------------------------------------------------
# Sample output:
#
# Enter the plane's take off speed in m/s: 60
# Enter the plane's acceleration in m/s**2: 3.5
# The minimum runway length needed for this airplane is 514.2857 meters.
#
# -----------------------------------------------------------------------------------------------

take_off_speed = eval(input("Enter the plane's take off speed in m/s: "))
acceleration = eval(input("Enter the plane's acceleration in m/s**2: "))

mininum_runway_length = (take_off_speed ** 2)/(2 * acceleration)

print(f"The minimum runway length needed for this airplane is {round(mininum_runway_length, 4)} meters")