from typing import List

# create helper function to get word length
def word_length(word: str) -> int:
    return len(word)

# create helper function to get absolute value
def abs_value(num: int) -> int:
    return abs(num)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=word_length, reverse=True) # sort by word length in descending order
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=abs_value) # sort by absolute value in ascending order
    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
