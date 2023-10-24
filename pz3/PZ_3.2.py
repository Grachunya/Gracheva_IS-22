# Смоделировать пройстейший калькулятор,умеющий выполнять 4 основные арифметические операции
while True:
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                exit()
            result = num1 / num2
        else:
            print("Ошибка: неверный оператор!")
            exit()
        print("Результат:", result)
        break

    except ValueError:  # обработка исключений
        print("Ошибка! Введите число")
