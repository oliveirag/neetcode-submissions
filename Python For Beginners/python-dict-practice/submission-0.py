from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count = {} # create dictionary
    for char in word: # loop though every character
        if char not in count: # if char wasn't added to dictionary yet
            count[char] = 0
        count[char] += 1
    return count


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
