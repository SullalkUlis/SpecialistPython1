## "Обработка списка фруктов"

### Задание

Дана ведомость расчета заработной платы [data/workers.txt](data/workers.txt).

Рассчитайте зарплату всех работников, зная что они получат полный оклад, если отработают норму часов. \
Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально, \
а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме. \
Кол-во часов, которые были отработаны, указаны в файле ["data/hours_of.txt](data/hours_of.txt)

### Формат входных данных

Дано два текстовых файла. Один с информацией о сотрудниках, второй с количеством отработанных часов.

Гарантируется, что каждый сотрудник имеет уникальную фамилию(однофамильцев нет).

### Формат выходных данных

Выведите зарплату сотрудников с учетом переработки и недоработки.

### Решение задачи

import operator

#----------# функция создания библиотеки из данных файла--------
def struct(file):
    path = 'Data/' + str(file).strip()
    f = open(path, 'r', encoding='UTF-8')
    i = 0
    j = 0
    keys = []
    sal_lib = []
    for line in f:
        sal_line = line.split()
        lib = {}
        for sal_l in sal_line:
            if i == 0:
                keys.append(sal_l)
            else:
                if keys[j].isdigit():
                    lib[keys[j]] = int(sal_l)
                else:
                    lib[keys[j]] = sal_l
                j += 1
        if len(lib) > 0:
            sal_lib.append(lib)
        i += 1
        j = 0
    i = 0
    return sal_lib
#-----------# функция вывода итоговой таблицы
def tab_out(lib):
    i = 0
    j = 0
    while i < len(lib):
        for k, v in lib[i].items():
            if i == 0 and j == 0:
                print(f'{k:>15}', end=' ')
            if i == 0 and j == 1:
                print(f'{v:>15}', end=' ')
            elif i > 0 and j > 1:
                print(f'{v:>15}', end=' ')
        i += 1
        j += 1
        if j == 1:
            i = 0
        print()
lib_1 = struct('workers.txt')
lib_2 = struct('hours_of.txt')
lib_1.sort(key=operator.itemgetter('Фамилия'))
lib_2.sort(key=operator.itemgetter('Фамилия'))
i = 0
while True:
    for k, v in lib_2[i].items():
        if k not in lib_1[i].items():
            lib_1[i][k] = lib_2[i][k]
    i += 1
    if i == len(lib_1) or i == len(lib_2):
        break
i = 0
while i < len(lib_1):
    k = 'ЗП_на_руки'
    if k not in lib_1[i].items():
        if int(lib_1[i]['Отработано_часов']) < int(lib_1[i]['Норма_часов']):
            rel_wok = int(lib_1[i]['Отработано_часов']) / int(lib_1[i]['Норма_часов']) * int(lib_1[i]['Зарплата'])
        else:
            rel_wok = (int(lib_1[i]['Отработано_часов']) - int(lib_1[i]['Норма_часов'])) * int(
                lib_1[i]['Зарплата']) / int(lib_1[i]['Норма_часов']) + int(
                lib_1[i]['Зарплата'])
        lib_1[i]['ЗП_на_руки'] = round(rel_wok, 2)
    i += 1
tab_out(lib_1)
