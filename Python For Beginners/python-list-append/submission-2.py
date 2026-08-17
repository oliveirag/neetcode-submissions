from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
   # if we want to iterate over values..
    for i in elements:
         my_list.append(i) 
    return my_list

  # if we wanted to iterate over indices..
    for i in range(len(elements)):
        my_list.append(elements[i])
    return my_list

# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
