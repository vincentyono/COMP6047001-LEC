# Tip Calculator (15 points)
# -----------------------------------------------------------------------------------------------
#
# Write a program that reads the subtotal and gratuity rate. The program then calculates and
# gratuity as a dollar amount, followed by the total amount, and displays all information in
# dollars.
#
# Your code should include currency formatting (i.e., use the $ in your output, include comma
# separation and format the result to 2 decimal places.)
#
# -----------------------------------------------------------------------------------------------
# Sample output:
#
# Enter the subtotal: $1250
# Enter tip amount (as a %): 25
# Subtotal: $ 1,250.00
# Tip: $ 312.50
# Total: $ 1,562.50
#
# -----------------------------------------------------------------------------------------------

subtotal = eval(input("Enter the subtotal: "))
tip_percent = eval(input("Enter tip amount (as a %): "))

tip = subtotal * (tip_percent / 100)
total = subtotal + tip

print(f"Subtotal: ${subtotal:,.2f}")
print(f"Tip: ${tip:,.2f}")
print(f"Total: ${total:,.2f}")