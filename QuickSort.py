import random               #for the randomlist
def make_me_an_list():
    list = []
    for i in range (5,25):
        list.append(random.randint(0,100))
    return list


def quicksort(list):
    if len(list) <= 1:                  # basecase checks how many items are in the list, 
        return list                     # if only 1 then the list is sorted so returns it
    else:
        pivot = list[0]                 # initlaises variables for each stack
        smaller = []
        larger = [] 
        for i in range(1,len(list)):    # starts a loop from 1-items in the list, allows us to iterate through each item
            if list[i] < pivot:         # if item at i index is < the pivot item
                smaller.append(list[i]) # adds it to the smaller list
            else:                       # else (if its bigger than pivot)
                larger.append(list[i])  # add to the bigger list
        return quicksort(smaller) + [pivot] + quicksort(larger) # once every item is iterated through
        # return the smaller list quicksorted + the pivot in the middle + the quicksorted larger list



list = make_me_an_list()   # initialises the list randomly 
print(list)                 #prints the unsorted list
print(quicksort(list))      #prints the list after putting it through the quicksort