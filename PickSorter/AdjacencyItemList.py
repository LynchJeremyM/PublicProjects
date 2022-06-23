import Items
from MergeSortItems import MergeSortItems
def GenAdjList(items):

    size = 6
    sorted = [[] for x in  range(size)]

    #Assign each item to an index based on its aisle #
    #These aisles can then be sorted to improve efficiency
    for i in range(0, len(items)):
        j = int( items[i].aisle / 2)
        sorted[j].append(items[i])

    return sorted

def SortAdjList(items):

    sorted = []

    #for i in items:
    #    sorted.append(MergeSortItems(i))
    
    for i in range(0, len(items)):
        sorted.append(MergeSortItems(items[i]))
    return sorted