class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    # getters
    def get_name(self):
        return self._name
    
    def get_address(self):
        return self._address
    
    # setters
    def set_name(self, name):
        self._name = name
    
    def set_address(self, address):
        return self._address
    
    # toString()
    def __str__(self):
        return f"name: {self._name}\naddress: {self._address}"