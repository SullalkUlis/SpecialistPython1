# В файлк salaries.txt даны зарплаты сотрудников

# Задача: выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000
# Сотружников вывести в формате: Фамилия И.О. ,например: Иванов И.П. (зарплаты в файл не записывать)
path = 'Data/salaries.txt'
f = open(path, 'r', encoding='UTF-8')
keys = []
sal_lib = []
i = 0
j = 0
for line in f:
    sal_line = line.split()
    lib = {}
    for sal_l in sal_line:
        if i == 0:
            keys.append((sal_l))
        else:
            if keys[j] == 'Зарплата':
                lib[keys[j]] = int(sal_l)
            else:
                lib[keys[j]] = sal_l
            j += 1
    if len(lib) > 0:
        sal_lib.append(lib)
    i += 1
    j = 0
f_out = open('Data/salaries_out.txt', 'w', encoding='UTF-8')
i = 0
str_out = f'{str(keys[0]):>2}  {str(keys[1]):>10} {str(keys[2]):>15}' + '\n'
f_out.write(str_out)
for person in sal_lib:
    if person['Зарплата'] > 60000:
        str_out = str(person['Фамилия']) + ' ' * 6 + str(person['Имя']) + ' ' * 8 + str(person['Отчество']) + '\n'
    else:
        continue
    f_out.write(str_out)
