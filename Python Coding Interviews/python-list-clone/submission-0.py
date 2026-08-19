from typing import List


def remove_element(arr: List[int], element: int) -> List[int]:
    cloned_arr = arr.copy() # cloned_arr = arr[:]
    for values in arr: # loop thru each value in cloned_arr
        if element in cloned_arr: # if this value is in arr
            cloned_arr.remove(element) # remove value from arr1
    return cloned_arr # return new list


# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
