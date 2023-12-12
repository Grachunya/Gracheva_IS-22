
# Дан список размера N и целое число K (K>1)
# Осуществить сдвиг элементов списка вправо на K позиций
# (при этом исходное значение K последних элементов будет утеряно)
# Первые K элементов полученного списка положить равными 0

def shift_and_zero(lst, k):
    new_lst = [0] * len(lst)
    for i in range(len(lst) - k):
            new_lst[i + k] = lst[i]
    return new_lst

lst = [1,5,7,8,4,2,9,10]
k = 2
if k < 1 or k >= len(lst):
    print("Ошибка: неверное число k!")
else:
    print(shift_and_zero(lst, k))
