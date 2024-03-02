# В матрице элементы первого столбца возвести в куб

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def cube(x):
    return x**3

result = list(map(lambda row: [cube(row[0])] + row[1:], matrix))

for row in result:
    print(row)
