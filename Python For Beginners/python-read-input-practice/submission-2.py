def add_two_numbers() -> int:
    res = input() # take user input
    numbers = res.split(",") # create list of substrings
    new_list = [] # create integer list
    for string in numbers:
        new_list.append(int(string))
    result = new_list[0] + new_list[1]
    return result




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
