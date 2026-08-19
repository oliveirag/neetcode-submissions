from typing import List, Dict

def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    my_dict = {}
    # using two for loops
    for i in range(len(keys)):
        for i in range(len(values)):
            my_dict[keys[i]] = values[i]
    return my_dict
    # using one for loop
    for key, value in zip(keys, value):
        my_dict[key] = value
    return my_dict

def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    result = [] # create new list
    for key in keys: # loop through each key in keys list
        if key in hash_map: # checks if key is in the hashmap
            result.append(hash_map[key]) # retrieve value from hash_map and add it to result
    return result                   

# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
