# Question 2
# -----------------------------------------------------------------------------------------------
#
# Write a function called calc weight on planet() that calculates your equivalent weight on another planet. 
# This function takes two arguments: your weight on Earth in pounds and the surface gravity of the planet of 
# interest with units m/s2. Make the second argument optional and supply a default value of 23.1 m/s2 which 
# is the approximate surface gravity of Jupiter (Earth’s suface gravity is approximately 9.8 m/s2). To perform 
# the conversion, use the equation: weight is equal to mass times suface gravity. Since your weight on Earth 
# is given and you know the Earth’s surface gravity, have your function use this information to calculate your 
# mass (it is fine if, at this point, the units of mass are a mix of Imperial and the MKS system). Then, use your 
# mass and the given surface gravity to calculate your effective weight on the other planet.
#
# -----------------------------------------------------------------------------------------------
#
# The following demonstrates the proper behavior of this function:
# calc_weight_on_planet(120, 9.8)
# 120.0
# calc_weight_on_planet(120)
# 282.85714285714283
# calc_weight_on_planet(120, 23.1)
# 282.85714285714283
#
# -----------------------------------------------------------------------------------------------

def calc_weight_on_planet(weight_on_earth, gravity = 23.1):
    return (weight_on_earth / 9.8 ) * gravity

print(calc_weight_on_planet(120, 9.8))
print(calc_weight_on_planet(120))
print(calc_weight_on_planet(120, 23.1))