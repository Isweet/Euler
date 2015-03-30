import collections
import itertools
import operator

def next_div(n):
    for i in xrange(2, n):
        if (n % i == 0):
            return i

    return n

# d | n, d is prime
def elim(n, p):
    c = 0

    while (n % p == 0):
        n /= p
        c += 1

    return n, c

# n >= 2
def fact(n):
    f = collections.Counter()

    while (n != 1):
        p = next_div(n)
        n, f[p] = elim(n, p)

    return f

for n in itertools.count(1):
    trian = n*(n + 1) / 2
    divs = reduce(operator.mul, [x + 1 for x in fact(trian).values()], 1)
    if (divs > 500):
        print trian
        break
