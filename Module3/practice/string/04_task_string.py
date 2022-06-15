# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here
summa, s = 0, 0
while True:
    if text.find(' ', s) - s > 5 or (
            text.find(' ', s) == -1 and len(text) - s > 5):  # или проверка длины последнего слова
        summa += 1
    s = text.find(' ', s) + 1
    if s == 0:
        break
print(summa)
# ===  2 способ===========================
summa = 0
total = 0
i = 0
while True:
    if text[i] != ' ':
        summa += 1
    else:
        if summa > 5:
            total += 1
        summa = 0
    i += 1
    if i == len(text):
        if summa > 5:
            total += 1
        break
print(total)
