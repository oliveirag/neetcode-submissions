from typing import List

def contains_duplicate(words: List[str]) -> bool:

    # version 2: if len of set is smaller than len of list
    my_set = set(words) # remove all duplicates
    return len(my_set) < len(words) # return true or false

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
