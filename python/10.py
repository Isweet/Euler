def sieve(lim):
    is_prime = [True] * lim

    is_prime[0] = False
    is_prime[1] = False

    for i in xrange(lim):
        if (is_prime[i]):
            yield i

            for j in xrange(i**2, lim, i):
                is_prime[j] = False

print sum(sieve(2000000))
