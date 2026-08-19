from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    val1, val2, val3 = triplet # unpack values from the list
    sum = val1 + val2 + val3 # sum up the values
    return sum

def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    width, height, depth = box_dimensions # unpack the values from the tuple
    volume = width * height * depth # calculate volume
    return volume

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
