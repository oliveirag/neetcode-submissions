from typing import List
from sortedcontainers import SortedDict

def remove_keys(sorted_dict: SortedDict[str, int], keys: List[str]) -> SortedDict[str, int]:
    for key in keys: # for each key in keys
        if key in sorted_dict: # if the key is in the sorted dictionary
            sorted_dict.pop(key) # remove the key and value from sorted dictionary
    return sorted_dict # return the new sorted dictionary

def get_values_before_target(sorted_dict: SortedDict[str, int], target: str) -> List[int]:
    res = [] # create new list

    for key, value in sorted_dict.items(): # for each key and value in the sorted dictionary
        if key == target: # if the key is the one we are looking for
            break # stop looping (we found the key)
        res.append(value) # if the key is not the target, append the value to res

    return res # return the list of values that come before the target key

# do not modify below this line
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), ['Bob']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), ['Bob', 'David']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45}), ['Alice', 'Eve']))

print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'David'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Charlie'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Alice'))
