#6.23列表推导式
#squares

squares = []
for x in range(10):
    squares.append(x**2)
squares

squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        combs.append((x, y))
combs

vec = [-4, -2, 0, 2,4]
[x*2 for x in vec]
[x for x in vec if x >= 0]
[abs(x) for x in vec]

[(x, x**2) for x in range(6)]

#[x, x**2 for x in range(6)] #SyntaxError: invalid syntax

vec = [[1,2,3],[4,5,6],[7,8,9]]
[num for elem in vec for num in elem]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]

#6.23嵌套的列表推导式
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
[[row[i]] for row in matrix for i in range(4)]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

transposed = []
for i in range(4):
    transposed_row = []
for row in matrix:
    transposed_row.append(row[i])
    transposed.append(transposed_row)
transposed

list(zip(*matrix))