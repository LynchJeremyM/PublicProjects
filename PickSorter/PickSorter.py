from AdjacencyItemList import GenAdjList, SortAdjList
from GenItemList import GenItemList
import MergeSort
from Items import Items
from MergeSortItems import MergeSortItems

items = [[1,3], [3,5], [9,6], [2, 10], [11, 15], [4, 7]]

#Assume that since each order is done in batches based on time the orders were placed, that you will always recieve the orders simultaneously as a whole unit.
#First, let's sort just by aisle number using a basic merge sort.
itemsSorted = MergeSort.merge_sort(items)
print(itemsSorted)

#Another solution would be to utilize an adjacency matrix/graph in the form of a linked list. Then, merge sort each aisle section.
#For this version, we created a Items class and randomly generate a new list of items.
more_items = GenItemList(30)
sorted = GenAdjList(more_items)


#TODO: Make output pretty ;)
for i in sorted:
    for j in i:
        print('[' + str(j.aisle) + ',' + str(j.shelf) + ']')


sorted_more = SortAdjList(sorted)
for i in sorted_more:
    for j in i:
        print('[' + str(j.aisle) + ',' + str(j.shelf) + ']')