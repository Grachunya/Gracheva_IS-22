# Дана строка-предложение на русском языке
# Зашифровать ее, выполнив циклическую замену каждой каждой буквы на следующие за ней в алфавите
# и сохранив при этом регистр букв (А-Б, а-б, Б-В, я-а)

def encrypt_cyclic(input_text):
    result = ""
    for i in input_text:
        if i.isalpha():
            if i == 'я':
                result += 'а'
            elif i == 'Я':
                result += 'А'
            else:
                result += chr(ord(i) + 1)
        else:
            result += i

    return result

input_text = "Пример строки для шифрования"
encrypted_text = encrypt_cyclic(input_text)

print("Исходная строка: ", input_text)
print("Зашифрованная строка: ", encrypted_text)
