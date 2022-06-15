# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# "count" - количествотовара в магазине
# Считая,что курс доллара равен dollar_rate
# Вычислите стоимость всех товаров с названием "name" в долларах

item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub", "count": "10"}
dollar_rate = 74.12

# TODO: your code here
tem = {"name": "Кроссовки", "price": "7540.5", "currency": "rub", "count": "10"}
dollar_rate = 74.12
summa = 0
rub = 'USD'
price, quant = 0, 0
for key, value in item.items():
    if key == 'price':
        price = float(value)
    if key == 'count':
        quant = int(value)
    if key == "currency" and value == "rub":
        rub = 'RUB'
    elif key == "currency" and value == 'USD':
        rub = 'USD'
    if rub == 'USD':
        summa = summa + price * quant / dollar_rate
    else:
        summa = summa + price * quant
print(round(summa, 2), rub)
