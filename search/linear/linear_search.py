# Big O -> N

def linear_search(arr: list[int], number: int) -> bool:
    for i in range(len(arr)):
        if arr[i] == number:
            return True

    return False