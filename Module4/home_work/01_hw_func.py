# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def may_abs(a):
    if a < 0:
        c = a * -1
    else:
        c = a
    return c

nam=float(input('введите число:'))
res = may_abs(-10)
print(res)


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
