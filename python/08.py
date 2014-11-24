import operator

text_file = open("../inputs/08.in", "r")
text = text_file.read().replace('\n', '')
text_file.close()

print max(reduce(operator.mul, s, 1) for s in (map(int, c) for c in (text[i:i + 13] for i in xrange(len(text) - 12))))
