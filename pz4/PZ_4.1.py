# Даны два целых числа A и B (А<B). Найти сумму всех целых чисел от A до B включительно.
while True:
    try:
        A = int(input("Введите первое число: "))
        B = int(input("Введите второе число "))
        summ = 0
        if B > A:
            for i in range(A, B+1):
                summ += i
            print(summ)
        else:                   # обработка исключений
            print("Ошибка: A>B!")
        break

    except ValueError:  # обработка исключений
        print("Ошибка! Введите число")