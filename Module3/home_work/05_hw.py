# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
i = 0
name_long = ''
while i < len(names):
    if len(names[i]) > len(name_long):
        name_long = names[i]
    i += 1
print(name_long)
