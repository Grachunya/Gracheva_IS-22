
# Даны целые числа A и B
# Сформировать и вывести целочисленный список размера 10
# первый элемент которого равен A, второй равен B
# а каждый последующий элемент равен сумме всех предыдущих.

def FirstList(A, B):
    result = [A, B]
    for i in range(2, 10):
        result.append(sum(result[:i]))
    return result

A = 3
B = 4

print(FirstList(A, B))
