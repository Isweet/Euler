import itertools

# It's slow... but its one line! Don't judge me.

# Results from % time python 05.py
# real	5m45.726s
# user	5m44.579s
# sys	0m0.227s

print next((x for x in itertools.count(1) if all(x % i == 0 for i in xrange(2, 21))), None)
