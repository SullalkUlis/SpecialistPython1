# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
mport random

n = int(input('Введите количество чисел в списке:'))
i = 0
sp_nam = []
while i < n:
    sp = random.randint(-100, 100)
    sp_nam.append(sp)
    print(sp_nam[i], end=' ')
    i += 1
summa = 0
for i in sp_nam:
    if i > 0 and i % 2 == 0:
        summa += i
print(summa)
