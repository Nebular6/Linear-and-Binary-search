def binary_search(array, search_item):
    midpoint = round(len(array)/2)   #initialises midpoint per recursion
    if search_item < array[midpoint]:
        return binary_search(array[:midpoint],search_item) #returns the lesser half of this list
    elif search_item > array[midpoint]:
        return binary_search(array[midpoint:],search_item) #returns the greater half of this list
    elif search_item == array[midpoint]: #if found
        return "the item is in the list"
    else:
        return "the item is not in the list" # if not found



array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] #sorted list
search_item = int(input("what item are you searching for: "))
try:
    print(binary_search(array,search_item)) #code gives an error when item is outside of list so i jsut gave it an exeption to print its outside, smartdumb solution
except:
    print("not in list")