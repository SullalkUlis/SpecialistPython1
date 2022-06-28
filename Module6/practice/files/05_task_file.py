# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день
import operator

path = 'Data/items_sold.txt'
f = open(path, 'r', encoding='UTF-8')
prod_list = []
typ = []
keys = ['type', 'price']
summa = 0
for line in f:
    if len(line.strip()) > 0:
        line = line.replace(':', ' ').split()
        i = 0
        while True:
            el_p = {}
            el_p[keys[0]] = line[i]
            el_p[keys[1]] = float(line[i + 1])
            summa += float(line[i + 1])
            if len(el_p) > 0:
                prod_list.append(el_p)
            i = i + 2
            if i == len(line):
                break
prod_list.sort(key=operator.itemgetter('price'))
print(f'Выручка магазина: {summa:.2f}')
typ = {}
count_typ = 0
print(f'выручка магазина по каждому типу товаров:')
for el in prod_list:
    k = el['type']
    if not k in typ:
        typ[k] = el['price']
        count_typ += 1
    else:
        typ[k] += el['price']
for k in typ.items():
    print(f'{k[0]:<15} на сумму: {k[1]:.2f}')
print('Самая большая выручка была по категории: ', prod_list[-1]['type'])
print('За день было продано:', count_typ, ' типов товаров')
