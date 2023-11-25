import random

def Insertion_Sort(array):
    sorted_list = [array[0]]  # Create a new list sorted_list with the first element of array
    for ItemToCompare in range(1, len(array)):  # Iterate over elements in array starting from the second element 
        value_to_insert = array[ItemToCompare]  # Get the value to be inserted from array
        InsertionIndex = ItemToCompare - 1  # Initialize 'InsertionIndex' to the previous index
        while InsertionIndex >= 0 and sorted_list[InsertionIndex] > value_to_insert:  # Iterate until correct position found
            InsertionIndex -= 1  # Move left in 'sorted_list'
        sorted_list.insert(InsertionIndex + 1, value_to_insert)  # Insert the value at the correct position in 'sorted_list'
    return sorted_list 

array = []  
for i in range(random.randint(5, 15)):
    array.append(random.randint(1, 15))
print(array)
print(Insertion_Sort(array))