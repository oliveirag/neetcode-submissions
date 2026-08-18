from typing import List

def read_integers() -> List[int]:
    res = input() # store user input (always a string)
    list_of_strings = res.split(",") # breaks res into a list of substrings
    new_list = [] # create a new list
    for string in list_of_strings: # loop through each string in list_of_strings
        new_list.append(int(string)) # convert the current string to an integer and add it to new list
    return new_list


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
