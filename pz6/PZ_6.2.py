
# Дан список размера N. Найти максимальный из его локальных минимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).

def find_local_minimum(arr):
    min_index = 0
    min_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_index = i
            min_value = arr[i]
        elif arr[i] == min_value and arr[i - 1] > arr[i]:
            return i
    return min_index

try:
    arr = [16, 44, 10, 12, 87]
    print(arr[find_local_minimum(arr)])

except ValueError:
    print("Вы ввели не число")
