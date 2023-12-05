
# Даны целые числа N (>2), A и B.
# Сформировать и вывести целочисленный список размера 10
# первый элемент которого равен A, второй равен B
# а каждый последующий элемент равен сумме всех предыдущих.

def FirstList(A, B, N):
    result = [A, B]
    for i in range(2, 10):
        result.append(sum(result[:i]))
    return result

while True:
    try:
        A = int(input("Введите первое число: "))
        B = int(input("Введите второе число: "))
        N = int(input("Введите третье число: "))
        if N > 2:
            SecondList = FirstList(A, B, N)
            print(SecondList)
        else:
            print('N должно быть больше 2')
        break

    except ValueError:
        print("Вы ввели не число!")
