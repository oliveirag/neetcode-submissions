from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    result = [] # create a new list
    for name in age_dict: # loop through each name in dictionary
        result.append(name) # add each name to end of list
    return result

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    result = [] # create new list
    for key, value in age_dict.items(): # loop through both the key and values at the same time
        result.append(value) # add each value to the end of the list
    return result

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
