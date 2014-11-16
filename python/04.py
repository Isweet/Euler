# Reverse digits in a number
def rev(n):
    rev = 0

    while (n):
        rev = rev * 10 + n % 10
        n /= 10

    return rev

print max(filter(lambda x: x == rev(x), (a * b for a in xrange(100, 1000) for b in xrange(a, 1000))))
