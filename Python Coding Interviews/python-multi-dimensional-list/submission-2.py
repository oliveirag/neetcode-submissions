from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_list = [] # create a new list
    for sublist in nested_arr: # loop thru each sublist inside list
        max_in_sublist = sublist[0] # set current max as the first number in sublist
        for number in sublist: # loop thru each number in sublist
            # if current number is greater than current max, update current max
            max_in_sublist = max(max_in_sublist, number) 
        max_list.append(max_in_sublist) # add current max after each sublist iteration
    return max_list # return list of all max number from each list

# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
