# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого положительного числа K на обратный
# K - параметр целого типа, являющийся одновременно входным и выходным
# Поменять порядок для каждого из пяти данных чисел

def InvertDigits(K):
    return int(str(K)[::-1])


while True:
    try:
        K = int(input("Введите целое число: "))
        K = InvertDigits(K)
        print(K)
        K = int(input("Введите целое число: "))
        K = InvertDigits(K)
        print(K)
        K = int(input("Введите целое число: "))
        K = InvertDigits(K)
        print(K)
        K = int(input("Введите целое число: "))
        K = InvertDigits(K)
        print(K)
        K = int(input("Введите целое число: "))
        K = InvertDigits(K)
        print(K)
        break
    except ValueError:
        print("Ошибка: введите число!")