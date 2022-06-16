# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
swap = True  # сортировка пузырьком по 'salary'
while swap:
    swap = False
    for i in range(len(staff) - 1):
        if staff[i]['salary'] > staff[i + 1]['salary']:
            staff[i], staff[i + 1] = staff[i + 1], staff[i]
            swap = True
print("Самая высокая зарплата:", staff[-1]['name'], staff[-1]['surname'], staff[-1]['salary'])
print("Самая низкая зарплата:", staff[0]['name'], staff[0]['surname'], staff[0]['salary'])
quant = 1
sur = []
j = 0
while True:  # поиск однофамильцев
    s_staff = staff[j]
    sur_n = {}
    i = j
    while i < len(staff) - 1:
        if s_staff['surname'] == staff[i + 1]['surname']:
            quant += 1
            if quant > 1:
                sur_n[staff[i + 1]['surname']] = quant
        i += 1
    j += 1
    if quant > 1:
        sur.append(sur_n)
    quant = 1
    if j == len(staff):
        break
print('Однофамильцы: ', sur)
summa = 0
quantity_staff = 0
for i in staff:
    summa = summa + float(i['salary'])
    quantity_staff += 1
    print(i['name'], i['surname'], i['salary'])
print("Среднеарифметическая зарплата", round(summa / quantity_staff, 2))
