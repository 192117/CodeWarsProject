import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         wrapper.called_times += 1
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time() - start_time
#         wrapper.total_time += end_time
#         print(f"Время выполнения функции {func.__name__}: {end_time} секунд.")
#         avg_time = wrapper.total_time / wrapper.called_times
#         print(f"Среднее время выполнения функции {func.__name__} за {wrapper.called_times} вызовов: {avg_time} секунд.")
#         return result
#     wrapper.called_times = 0
#     wrapper.total_time = 0
#     return wrapper

# @timer
# def high_and_low(numbers):
#     values = [int(value) for value in numbers.split()]
#     def heap_sort(numbers):
#         if len(numbers) <= 1:
#             return
#         left, middle, right = [], [], []
#         barrier = numbers[len(numbers) % 2]
#         for number in numbers:
#             if number < barrier:
#                 left.append(number)
#             elif number > barrier:
#                 right.append(number)
#             else:
#                 middle.append(number)
#             heap_sort(left)
#             heap_sort(right)
#         index = 0
#         for number in left + middle + right:
#             numbers[index] = number
#             index += 1
#     heap_sort(values)
#     return f'{values[-1]} {values[0]}'

# @timer
def high_and_low(numbers):
    values = sorted(numbers.split(), key=int)
    return '{} {}'.format(values[-1], values[0])


high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")

