from functools import reduce


def solution(number):
    return reduce(lambda x, y: x+y, filter(lambda x: x % 3 ==0 or x % 5 == 0, range(number))) if number > 0 else 0

dict_values = {
    4: 3,
    6: 8,
    16: 60,
    3: 0,
    5: 3,
    15: 45,
    0: 0,
    -1: 0,
    10: 23,
    20: 78,
    200: 9168
}

for number in dict_values:
    print(f'Для числа {number}: функция вернула {solution(number)}, а в словаре {dict_values[number]}')