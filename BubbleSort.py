import random
def Bubble_Sort(array):
    for i in range(len(array)):  # Iterate through each element in array
        for i in range(len(array)-1):  # Iterate through the unsorted portion of array
            if array[i] > array[i+1]:  # Check if the current element is greater than the next one
                array[i], array[i+1] = array[i+1], array[i]  # Swap the elements if they are in the wrong order
            else:
               pass  # Do nothing if the elements are in the correct order
    return array  # Return the sorted array

array = []
for i in range(random.randint(5,15)):
    array.append(random.randint(1,15))
print(array)
print(Bubble_Sort(array))
