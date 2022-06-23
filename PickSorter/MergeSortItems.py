def MergeSortItems(item_list):
    if len(item_list) <= 1:
        return item_list
    
    left = []
    right = []

    for i, x in enumerate(item_list):
        if i < len(item_list) / 2:
            left.append(item_list[i])
            #print(left)
        else:
            right.append(item_list[i])
            #print(right)

    left = MergeSortItems(left)
    right = MergeSortItems(right)

    return Merge(left, right)

def Merge(left, right):
    result = []

    #TODO -> Fix input from calling class -> From List of Lists to 1 List
    while left and right:
        if left[0].shelf <= right[0].shelf:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    
    #Remove remaining elements in lists
    while left:
        result.append(left[0])
        left.pop(0)
    while right:
        result.append(right[0])
        right.pop(0)

    return result