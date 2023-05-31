class Item:
    def __init__(self, itemname, itemprice, itemquantity):
        self.name = itemname 
        self.price= itemprice
        self.quantity = itemquantity

item1 = Item("sugar", 100, 1)
item2 = Item("salt", 20, 2)

print (item1.name, item1.price, item1.quantity)
print (item2.name, item2.price, item2.quantity)