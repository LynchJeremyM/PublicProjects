import random
from Items import Items
def GenItemList(size):
    
    items = []
    for i in range (0, size):
        items.append(RandomItem())
    return items
        
#TODO: Add generation of inventory count for backstock and shelf locations
def RandomItem():
    shelf = random.randrange(0, 20)
    aisle = random.randrange(0,12)
    item = Items(shelf, aisle)
    return item