from datetime import datetime
"""Simple examples from Python Design Patterns"""

squares = [value**2 for value in range (1,11)]
print(squares)

squares = [value**2 for value in range(1,11)]
print (squares)

nlist = [x**2 for x in range(11) if x%2 == 0]
print (nlist)


start = datetime.now()
for _ in range(1_000_000):
    squares = [value ** 2 for value in range(1, 21)]
endt = datetime.now()
print("time=", endt - start)
diff1 = endt - start
print(squares)

# equivalent code
start = datetime.now()
for _ in range(1_000_000):
    squares = [value ** 2 for value in range(1, 21)]
endt = datetime.now()
print("time=", endt - start)
diff2 = endt - start
print(squares)

"""Examples taken from Programmiz.com"""
start = datetime.now()
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

#transposed = []
for _ in range(1_000_000):
    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = [row[i] for row in matrix]

        transposed.append(transposed_row)


endt= datetime.now()
elapsed =  endt-start
print(elapsed)
print(transposed)


start = datetime.now()
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
for _ in range(1_000_000):
    transpose = [[row[i] for row in matrix] for i in range(4)]

endt= datetime.now()
elapsed =  endt-start
print(elapsed)
print (transpose)