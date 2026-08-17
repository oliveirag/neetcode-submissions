from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    # the colon is necessary because it starts at the third last element and goes till the end
    return my_list[-3:] 
    # same thing as..
    return my_list[len(my_list) -3:]

# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
