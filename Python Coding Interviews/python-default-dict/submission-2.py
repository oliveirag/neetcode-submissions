from collections import defaultdict
from typing import List, Dict

def count_chars(s: str) -> Dict[str, int]:
    freq = defaultdict(int) # set default value for keys that don't exist in dictionary

    for char in s: # for each character
        freq[char] += 1 # add it to the dictionary and assign its value

    return freq # return the dictionary

def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    d = defaultdict(list) # create dictionary where default value is an empty list

    for sublist in nums: # for each list in nums
        key = sublist[0] # set the key as the first element in each sublist

    for i in range(1, len(sublist)): # loop thru each list starting at the first sublist
        d[key].append(sublist[i])

    return d


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
