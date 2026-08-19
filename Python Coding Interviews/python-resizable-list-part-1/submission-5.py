from typing import List

def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for i in range(len(arr2)): # loop thru arr2
        arr1.append(arr2[i]) # append current value of arr2 to the end of arr1
    return arr1 # return updated arr

def pop_n(arr: List[int], n: int) -> List[int]:
    if n > len(arr): # if n is greater than length of list
        return [] # return empty list
    while n > 0: # while n is not zero, remove the last n elements of the list
        arr.pop() # arr.pop() will always remove from the end
        n -= 1
    return arr # return updated arr

def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    if 0 <= index <= len(arr): # if index is in bounds
        arr.insert(index, element) # insert element at the index
    else: # if index is out of bounds
        arr.append(element) # insert element at the end of list
    return arr # return updated arr

# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
