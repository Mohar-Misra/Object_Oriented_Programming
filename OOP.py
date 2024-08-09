import csv


class Item:
    pay_rate = 0.8 #Payrate after discount of 20%
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        #Run validations to the received arguements

        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def totalprice(self):
        return self.price *self.quantity
    
    def discount(self):
        return self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero. i.e: 10.0, 5.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

print(Item.is_integer(4.5))

#Item.instantiate_from_csv()
#print(Item.all)

# print(Item.all) Prints the presence of the number of instances in the Class atribute: 'all' in a list.
#for items in Item.all: # Loops through the instances in the list from the class attribute.
#    print(items.name, f"- {items.price} USD") # Prints the instance name and the price. 
#print(item1.discount())
#item2.pay_rate = 0.7
#print(item2.discount())
#print(Item.__dict__)  all atributes for class level
#print(item1.__dict__) #all atributes for instance level
#item1.is_smart_phone = False
#print(item1.totalprice())
#print(Item.pay_rate)
#print(item1.is_smart_phone)
#print(item1.totalprice(item1.price,item1.quantity))