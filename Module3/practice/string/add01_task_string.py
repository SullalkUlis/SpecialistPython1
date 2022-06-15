# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

# TODO: your code here
text_out = ''
for i in text:
    if i not in ('.', ',', ':', ';', '!', '"', '"', '?', '\\', '/', '|',):
        text_out = text_out + i
summa, s = 0, 0
while True:
    if text_out.find(' ', s) - s > 7 or (
            text_out.find(' ', s) == -1 and len(text_out) - s > 7):  # или проверка длины последнего слова
        summa += 1
    s = text_out.find(' ', s) + 1
    if s == 0:
        break
print(summa)
print(text_out)
