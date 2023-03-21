def productFib(prod):
    fib = [0, 1]
    while True:
        if fib[-2]*fib[-1] < prod:
            fib[0], fib[1] = fib[1], fib[0]+fib[1]
        elif fib[0]*fib[1] == prod:
            return [fib[0], fib[1], True]
        else:
            return [fib[0], fib[1], False]



print(productFib(714)) # should return [21, 34, true]
print(productFib(800)) # should return [34, 55, false]
print(productFib(4895)) # should return [55, 89, True]
print(productFib(5895)) # should return [89, 144, False]
