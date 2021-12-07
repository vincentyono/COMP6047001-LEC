from FoodItemVY import FoodItem

def shop():
    shopping_cart = []
    number_of_order = 0

    # Loop while Number of items below 1
    while number_of_order < 1:
        number_of_order = eval(input("How many items will you order today? "))
        if number_of_order < 1:
            print("Number of items must be at least 1.")

    for i in range(number_of_order):
        print(f"Item #{i + 1}")
        food_name = input("Enter food: ")
        amount_in_pound = 0

        while amount_in_pound <= 0: # Loop while amount of pound is below or equal to 0
            amount_in_pound = float(input("Enter amount of pounds: "))
            if amount_in_pound <= 0:
                print("Amount of pounds must be greater than 0.")

        print() # spacing
        
        shopping_cart.append(FoodItem(food_name, amount_in_pound))
    
    print("Here's a summary of the items puchaed:")
    print("--------------------------------------")
    for fooditem in shopping_cart:
        print(f"Item: {fooditem.get_name()}")
        print(f"Amount ordered: {fooditem.get_amount()} {'pound' if fooditem.get_amount() <= 1 else 'pounds'}") # pound(without 's') if amount ordered is 1 or below 1
        print(f"Price per pound: ${fooditem.get_price():.2f}")
        print(f"Price of order: ${fooditem.get_total_price():.2f}")
        print() # spacing

    total_price = 0
    for fooditem in shopping_cart:
        total_price += fooditem.get_total_price()
    
    print(f"Total cost: ${total_price:.2f}")

if __name__ == '__main__':
    shop()