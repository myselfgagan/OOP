from item import Item
from phone import Phone


# item1 = Item("Phone", 100, 2)
# item2 = Item("Laptop", 200, 5)
# item3 = Item("Cable", 10, 3)
# item4 = Item("Mouse", 10, 5)
# item5 = Item("Keyboard", 50, 5)

print(Item.pay_rate)
# print(item1.pay_rate)

# print(Item.__dict__) # all the attributes for class level
# print(item1.__dict__) # all the attributes for instance level

# item2.pay_rate = 0.7 # if we have to give different discount to an item

print(Item.is_integer(5)) 

for instance in Item.all:
    print(instance.name)

Item.instantiate_from_csv()
print(Item.all)


phone1 = Item("phone1.0", 500, 5)
phone1.broken_phones = 1
phone2 = Item("phone2.0", 700, 10)
phone2.broken_phones = 2


item1 = Item("myItem", 100)

#setting an attribute
item1.name = "updatedItem"

#getting an attribute
print(item1.name)