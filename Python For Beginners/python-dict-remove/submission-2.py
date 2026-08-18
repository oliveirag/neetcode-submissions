from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for key in keys: # loop through each key in the list
        if key in my_dict: # if the key is in the dictionary
            my_dict.pop(key) # remove the key
        # my_dict.pop(key, 0) also works
    return my_dict # return new dictionary
        
# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
