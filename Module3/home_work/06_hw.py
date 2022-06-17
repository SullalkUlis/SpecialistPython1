# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
max_p = 0
for i in items:
    if i['price'] > max_p:
        max_p = i['price']
        max_e = i
quant = 1
sur = []
j = 0
print("Товары на складе представлены брэндами: ")
while True:
    it = items[j]
    it_n = {}
    i = j
    while i < len(items) - 1:
        if it['brand'] == items[i + 1]['brand']:
            quant += 1
            it_n['brand'] = items[i + 1]['brand']
            it_n['quantity'] = quant
        i += 1
    j += 1
    if quant > 1:
        sur.append(it_n)
    else:
        print(it['brand'])
    quant = 1
    if j == len(items):
        break
max_q = 0
k = 0
for i in range(len(sur)):
    #print('#', i + 1, sur[i]['brand'])
    if sur[i]['quantity'] > max_q:
        max_q = sur[i]['quantity']
        ma = sur[i]
    elif sur[i]['quantity'] == max_q:
        k += 1
print("На складе больше всего товаров брэнда(ов): ")
if k == 0:
    print(ma['brand'])
else:
    print('Одинаково:', ma['brand'],'и ', sur[-1]['brand'])
#print('Бренды', sur)
print("На складе самый дорогой товар брэнда(ов): ")
print(max_e['name'], max_e['brand'], max_e['price'])
