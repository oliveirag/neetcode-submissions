def add_two_numbers() -> int:
    res = input() # take user input
    numbers = res.split(",") # create list of substrings
    new_list = [] # create integer list
    for string in numbers: # loop through each string in numbers
        new_list.append(int(string)) # convert each string to an int, and add to end of list
    result = new_list[0] + new_list[1] # add both numbers in list
    return result

    #one liner
    return int(numbers[0]) + int(numbers[1])

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
