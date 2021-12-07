class FoodItem:
    # constructor
    def __init__(self, name: str, amount: float):
        self.__name = name
        self.__amount = float(amount)
        self.__price = self.__price_list()
        self.__total_price = self.calculate_total_price()

    def __price_list(self) -> None:
        if self.__name == "Dry Cured Iberian Ham":  return 177.80
        elif self.__name == "Wagyu Steaks":         return 450.00
        elif self.__name == "Matsutake Mushrooms":  return 272.00
        elif self.__name == "Kopi Luwak Coffee":    return 306.50
        elif self.__name == "Moose Cheese":         return 487.20
        elif self.__name == "White Truffles":       return 3600.00
        elif self.__name == "Blue Fin Tuna":        return 3603.001
        elif self.__name == "Le Bonnette Potatoes": return 270.81
        else:                                       return 0.00
    
    def calculate_total_price(self):
        return self.__price * self.__amount
    
    # getters
    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def get_price(self):
        return self.__price

    def get_total_price(self):
        return self.__total_price