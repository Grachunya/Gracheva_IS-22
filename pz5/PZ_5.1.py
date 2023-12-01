# Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов
while True:
    try:
        def stroka(a):
            kolichestvo = len(a)
            print("Количество симвлов в сообщении: ", kolichestvo)
        a = str(input("Введите сообщение: "))

        stroka(a)

        break
    except ValueError:
        print("Ошибка!")
