import itertools

def prime_gen():
    yield 2

    curr = 3
    seen = [2]

    while (True):
        yield curr
        seen.append(curr)
        curr = next((x for x in itertools.count(curr + 2, 2) if all(x % i != 0 for i in seen)), None)

print itertools.islice(prime_gen(), 10000, 10001).next()
