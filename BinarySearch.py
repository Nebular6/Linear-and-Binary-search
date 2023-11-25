def binary_search(array, search_item):
    midpoint = len(array)/2
    if search_item < array[midpoint]:
        return binary_search(array[:midpoint],search_item)
    elif search_item > array[midpoint]:
        return binary_search(array[midpoint:],search_item)
    elif search_item == array[midpoint]:
        return "the item is in the list"
    else:
        return "the item is not in the list"



array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] #sorted list
search_item = int(input("what item are you searching for: "))
print(binary_search(array,search_item))