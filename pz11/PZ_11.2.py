f3 = open('text18-6.txt', 'r', encoding='UTF-16LE')
text = f3.read()
space_count = text.count(' ')
print("Содержимое файла: ", text)
print(f'Количество пробельных символов: {space_count}')

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for char in punctuation:
    text = text.replace(char, '!')


f4 = open('poem_text.txt', 'w')
f4.write(text)
f4.close()
f3.close()