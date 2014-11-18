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

def lcm(nums):
    # Get the factorization of each of the arguments
    facts = [dict(fact(x)) for x in nums]
    # Get all of the primes in each of the factorizations
    keys = list(reduce(set.union, (set(x.keys()) for x in facts)))
    # Get the maximum exponent of each prime over all factorizations
    lcm_fact = dict(map(lambda (k, v): (k, max(v)), dict((k, [x.get(k, 0) for x in facts]) for k in keys).iteritems()))
    # Multiply it out
    return reduce(lambda a, b: a * b, map(lambda (k, v): k**v, lcm_fact.iteritems()), 1)

print lcm(xrange(2, 21))
