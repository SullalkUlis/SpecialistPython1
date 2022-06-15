# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
import random

n = int(input('Введите количество чисел в списке:'))
i, summa = 0, 0
sp_nam = []
while i < n:
    sp = random.randint(-10, 10)
    sp_nam.append(sp)
    summa += sp
    print(sp_nam[i], end=' ')
    i += 1
print()
print(summa)
