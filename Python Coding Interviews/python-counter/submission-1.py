from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    counter = Counter(s1) # create a dict that counts the occurences of each character in s1
    counter.update(s2) # update that dict with the occurences of s1

    return counter # return the dict

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
