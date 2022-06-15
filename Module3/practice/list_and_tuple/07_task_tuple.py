# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here
max_t = 0
for i in tup:
    if max_t < i:
        max_t = i
print(max_t)
