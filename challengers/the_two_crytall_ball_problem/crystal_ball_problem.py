from math import sqrt, floor

def crystal_ball_problem(arr: list[int]) -> int:
    jump_amount = floor(sqrt(len(arr)))
    andar_atual = jump_amount

    for i in range(andar_atual, len(arr) + 1, jump_amount):
        andar_atual = i - 1
        if arr[andar_atual] == 1:
            break

    andar_atual = andar_atual - jump_amount

    if andar_atual < 0:
        andar_atual = 0

    for j in range(jump_amount + 1):
        if andar_atual + j >= len(arr):
            break

        if arr[andar_atual + j] == 1:
            return andar_atual + j

    return -1