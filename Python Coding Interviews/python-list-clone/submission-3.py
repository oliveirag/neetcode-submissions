from typing import List

def remove_element(arr: List[int], element: int) -> List[int]:
    cloned_arr = arr.copy() # make a copy of arr
    cloned_arr = arr[:] # another way to make copy of arr
    cloned_arr = list(arr) # another way to make copy of arr
    while element in cloned_arr: # while the element is in cloned_arr
            cloned_arr.remove(element) # remove value from cloned_arr
    return cloned_arr # return new list

# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
