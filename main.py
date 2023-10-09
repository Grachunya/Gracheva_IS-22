t = 10
while t:
    t -= 1
    if t % 2 != 0: continue # пропуск нечетных чисел
    print(t, end=' ')