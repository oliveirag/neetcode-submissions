from typing import List

def read_integers() -> List[int]:
    res = input() # store user input (a string)
    list_of_strings = res.split(",") # split the list of strings and store it in a different list
    list_of_int = []
    for string in list_of_strings:
        list_of_int.append(int(string))
    return list_of_int


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
