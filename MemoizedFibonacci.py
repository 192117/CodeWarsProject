# def fibonacci(n):
#     fib = [0, 1] + [0] * (n-1)
#     for num in range(2, n+1):
#         fib[num] = fib[num-1] + fib[num-2]
#     return fib[n]

# def fibonacci(n):
#     n2, n1 = 0, 1
#     if n == 1:
#         return n2
#     elif n == 2:
#         return n1
#     else:
#         for num in range(2, n+1):
#             n2, n1 = n1, n1 + n2
#         return n1

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
