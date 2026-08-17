def remove_fourth_character(word: str) -> str:
    message = word
    before_fourth = word[:3]
    after_fourth = word[5:]
    return before_fourth + after_fourth


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
