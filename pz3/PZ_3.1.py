# Даны три целых числа: A, B, C.Проверить истинность высказывания: «Справедливо двойное неравенство A < B < C»
while True:
    try:
        A = int(input("Введите первое число: "))
        B = int(input("Введите второе число: "))
        C = int(input("Введите третье число: "))
        if (A < B) and (B < C):
            print("True")
        else:
            print("False")

        break

    except ValueError:  # обработка исключений
        print("Ошибка! Введите число")
