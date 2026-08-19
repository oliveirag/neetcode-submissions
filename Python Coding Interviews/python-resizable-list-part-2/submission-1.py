from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for i in range(len(arr2)): # loop thru arr2
        arr1.append(arr2[i]) # add each value of arr2 to the end of arr1
    return arr1 # return updated list

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for element in arr2: # loop thru each value in arr2
        if element in arr1: # if this value is in arr1
            arr1.remove(element) # remove value from arr1
    return arr1 # return updated arr1

# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
