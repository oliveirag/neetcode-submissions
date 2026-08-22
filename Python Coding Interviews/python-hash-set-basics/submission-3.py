from typing import List, Set


def build_hash_set(keys: List[str]) -> Set[str]:
    my_set = set() # create set

    for i in range(len(keys)): # for each string in the list
        my_set.add(keys[i]) # add the string to the set
    return my_set # return the set

def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    exists = []

    for i in range(len(keys)): # loop thru each key
        if keys[i] in hash_set:
            exists.append(True)
        else:
            exists.append(False)
    return exists


# do not modify below this line

output1 = build_hash_set(["Alice", "Bob", "Charlie"])
print(type(output1))         # check the type of the output
print(sorted(list(output1))) # set order is not guaranteed so we need to sort the list

output2 = build_hash_set(["XY", "XX", "YY", "XY", "YX"]) 
print(type(output2))         # check the type of the output
print(sorted(list(output2))) # set order is not guaranteed so we need to sort the list

print(check_keys({"Alice", "Bob", "Charlie"}, ["Alice", "Bob", "Charlie", "David"]))
print(check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']))
print(check_keys({'a', 'c'}, ['d', 'c']))
