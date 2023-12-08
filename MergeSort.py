import random

def merge(left, right):
    merged = []                             #initialises the list 
    left_idx = right_idx = 0                # set left and right index to 0
    while left_idx < len(left) and right_idx < len(right):      
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged



def merge_sort(m):
    if len(m) == 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)




list = []
for i in range(random.randint(5,15)):
    list.append(random.randint(1,15))
print(list)
print (merge_sort(list))