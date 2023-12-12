

# Дан список размера N. Найти максимальный из его локальных минимумов.
# (локальный минимум — это элемент, который меньше любого из своих соседей).

def find_local_minimum(arr):
    minimums = []
    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            minimums.append(arr[i])
    return minimums

try:
    arr = [16, 44, 10, 12, 87, 14, 1, 23]
    print(max(find_local_minimum(arr)))

except ValueError:
    print("Вы ввели не число")