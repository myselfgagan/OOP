import csv

class Item:
    pay_rate = 0.8 #the rate after 20% discount
    all = []

    def __init__(self, name: str, price: int, quantity=0):
        # run validation to received arguments
        assert price >= 0, f"price {price} is negative"
        assert quantity >=0, f"quantity {quantity} is negative"

        # assign to self object
        self.__name = name      # double underscore makes the variable "private"
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    
    @property   #  -->  Read only attribute if setter is not present
    def name(self):           # this is getter  -->  will not let change/update the value after initialisation
        return self.__name


    @name.setter
    def name(self, value):    # this is setter  -->  will help update value if getter is used
        self.__name = value


    def calculate_total_price(self):
        return self.price * self.quantity

    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    
    @classmethod
    def instantiate_from_csv(cls):  #class object is passed as 1st argument
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    
    @staticmethod
    def is_integer(num):  # object is not send as 1st argument.... behaves like normal function
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


