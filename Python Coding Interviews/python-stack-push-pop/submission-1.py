from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    stack = [] # create new stack
    while len(arr) > 0: # while arr has integers
        stack.append(arr.pop()) # remove from arr and add to stack
    return stack # list is returned in reverse

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
