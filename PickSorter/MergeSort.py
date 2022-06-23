#https://en.wikipedia.org/wiki/Merge_sort
#O(nlogn)
#Example mergesort that custom sorts are based on for this project.
def merge_sort(item_list):
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

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []

    while left and right:
        if left[0][0] <= right[0][0]:
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