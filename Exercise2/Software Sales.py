# Software Sales (15 points)
# -----------------------------------------------------------------------------------------------
#
# A software company sells a package that retails for $99. Discounts for quantities are given
# according to the following table:
#
#       Quantity                Discount
#       10 -19                  10%
#       20 - 49                 20%
#       50 - 99                 30%
#       100 or more             40%
#
# Write a program that asks the user to enter the number of packages purchased. The program
# should then display the amount of the discount (if any) and the total of the purchase after the
# discount. (Use appropriate formatting to display currency and percentages in your output.)
#
# -----------------------------------------------------------------------------------------------
# Sample output (no discount):
#
# Enter the number of packages purchased: 5
# Discount Amount @ 0% : $ 0.00
# Total Amount: $ 495.00
# Sample output (with a discount):
# Enter the number of packages purchased: 45
# Discount Amount @ 20% : $ 891.00
# Total Amount: $ 3564.00
#
# -----------------------------------------------------------------------------------------------

number_of_packages = int(input("Enter the number of packages: "))

if number_of_packages >= 100:
    discount = 40
elif number_of_packages >= 50:
    discount = 30
elif number_of_packages >= 20:
    discount = 20
elif number_of_packages >= 10:
    discount = 10
else:
    discount = 0

subtotal = 99 * number_of_packages
discount_amount = subtotal * (discount / 100)
total_amount = subtotal - discount_amount

print(f"Discount Amount @ {discount}% : ${discount_amount:.2f}")
print(f"Total Amount: ${total_amount:.2f}")