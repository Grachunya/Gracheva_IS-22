# Дан символ С, изображающий цифру или букву (латинскую или русскую)
# Если С - цифра, то выводится строка "digit"
# если латинская буква - выводится строка "lat"
# если русская - выводится строка "rus"

s = "ф"
if ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('z'):
    print("lat")
elif ord('а') <= ord(s) <= ord('я') or ord('А') <= ord(s) <= ord('Я'):
    print("rus")
else:
    print("digit")
