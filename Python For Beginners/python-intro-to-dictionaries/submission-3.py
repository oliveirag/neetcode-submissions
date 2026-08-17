from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    # mapping directly
    my_dict = {name: age} # notice the use of the colon
    return my_dict

    # using an empty dictionary then mapping
    my_dict = {}
    my_dict[name] = age
    return my_dict

def list_to_dict(words: List[str]) -> Dict[str, int]:
    my_dict = {}
    for i in range(len(words)): # loop through indexes
        word = words[i] # create word variable and set it to current word
        my_dict[word] = i # map the current word to its current index
    return my_dict

# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
