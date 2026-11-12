from typing import List

def sort_words(words: List[str]) -> List[str]:
    words.sort() # sort words in ascending order
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort() # sort numbers in ascending order
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort() # sort numbers in ascending order
    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
