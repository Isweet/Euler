import operator

def right_prod(matrix, x, y):
    return reduce(operator.mul, [matrix[x][y + i] for i in range(4)], 1)

def down_prod(matrix, x, y):
    return reduce(operator.mul, [matrix[x + i][y] for i in range(4)], 1)

def rdiag_prod(matrix, x, y):
    return reduce(operator.mul, [matrix[x + i][y + i] for i in range(4)], 1)

def ldiag_prod(matrix, x, y):
    return reduce(operator.mul, [matrix[x + i][y - i] for i in range(4)], 1)

def max_prod(matrix, height, width):
    max_prod = 0

    for x in range(height):
        for y in range(width):
            if (y + 3 < width):
                r = right_prod(matrix, x, y)
                max_prod = max(max_prod, r)

            if (x + 3 < height):
                d = down_prod(matrix, x, y)
                max_prod = max(max_prod, d)

            if (y + 3 < width and x + 3 < height):
                rdiag = rdiag_prod(matrix, x, y)
                max_prod = max(max_prod, rdiag)

            if (y - 3 >= 0 and x + 3 < height):
                ldiag = ldiag_prod(matrix, x, y)
                max_prod = max(max_prod, ldiag)


    return max_prod

text_file = open("../inputs/11.in", "r")
matrix = [[int(x) for x in l.split()] for l in text_file.readlines()]
text_file.close()

print max_prod(matrix, 20, 20)

