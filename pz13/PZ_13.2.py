# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.

matrix = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

def replace(element):
    return 0 if element > 10 else element

new_matrix = [list(map(replace, row)) for row in matrix]

print("\nМатрица с заменой элементов: ")
for row in new_matrix:
    print(row)
