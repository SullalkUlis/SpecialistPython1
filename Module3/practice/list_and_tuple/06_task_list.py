# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
while first_number <= second_number:
    if first_number % 3 == 0:
        print(first_number, end=' ')
        first_number += 3
    else:
        first_number += 1
