# Напишите функцию находящую n-ое число Фибоначчи.
def fibonachi(num):
    fib = 0
    i, j = 1, 0
    while i < num:
        if 0 <= i <= 1:
            fib = j + i
        else:
            fib = j + fib
            j = fib - j
        i += 1
    return fib
