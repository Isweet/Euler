from itertools import count

# Generator for all pythagorean triples s.t. r < bound
def pyth_triples(bound):
    iterable = range(2, bound) if bound else count(2)
    
    for r in iterable:
        for s in range(1, r):
            yield [r*r - s*s, 2*r*s, r*r + s*s]

for a, b, c in pyth_triples(None):
    if (a + b + c == 1000):
        print(a * b * c)
        break


