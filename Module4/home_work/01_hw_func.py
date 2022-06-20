# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    summa1 = 0
    summa2 = 0
    if len(str(ticket_number)) != 6:
        str_out = 'Не шестизначный номер'
        return str_out
    else:
        number = str(ticket_number)
        for num in range(len(str(number))):
            if num <= 2:
                summa1 += int(number[num])
            else:
                summa2 += int(number[num])
    if summa1 == summa2:
        str_out = 'Счастливый билет'
    else:
        str_out = 'Не счастливый билет'
    return str_out

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
