import collections

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

print (max(fact(600851475143)))
