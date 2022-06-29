# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data/info.txt", "r") as f:
    summa = 0
    for line in f:
        if len(line.strip()) > 0:
            if line.strip().isdigit():
                summa = summa + int(line.strip())
                print(line, '++', summa, '!!!  ')
            else:
                print(line, '---')
                continue
        else:
            continue
    print(summa)
