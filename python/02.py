def fib_gen(lim):
    first = 1
    second = 2

    while (first <= lim):
        yield first
        first, second = second, first + second

print sum(filter(lambda x: x % 2 == 0, fib_gen(4000000)))
