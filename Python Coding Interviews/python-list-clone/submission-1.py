from typing import List


def remove_element(arr: List[int], element: int) -> List[int]:
    cloned_arr = arr.copy() # make a copy
    cloned_arr = arr[:]
    for values in arr: # loop thru each value in arr
        if element in cloned_arr: # if this value is in cloned_arr
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
