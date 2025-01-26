# Big O - LogN

from math import floor

def binary_search(arr: list[int], target: int) -> bool:
    low_point = 0
    high_point = len(arr)

    while low_point < high_point:
        mid_point = floor(low_point + (high_point - low_point) / 2)
        mid_point_value = arr[mid_point]

        if target == mid_point_value:
            return True
        elif target > mid_point_value:
            l_point = mid_point + 1
        else:
            h_point = mid_point

    return False
