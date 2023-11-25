def Linear_Search(list, search_item):
    for i in range(len(list)):  # Iterate through each element in the list
        if list[i] == search_item:  # Check if the current element is equal to the search item
            return i  # If found, return the index of the item in the array
        else:
            pass  # If not found, do nothing and continue to the next iteration
    i = "not in array"  # If the search item is not found in the array set i to "not in array"
    return i  # Return the result

array = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
search_item = int(input("What item are you searching for: ")) 
print(Linear_Search(array, search_item))