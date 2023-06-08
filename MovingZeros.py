def move_zeros(lst):
    answer = list(filter(lambda x: x>0 if len(lst)>0 else lst, lst))
    return answer + [0] * (len(lst) - len(answer))


dict_values = [
    [1, 2, 0, 1, 0, 1, 0, 3, 0, 1], # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9], # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    [0, 0], # [0, 0]
    [0], # [0]
    [], # []
]

for value in dict_values:
    print(move_zeros(value))