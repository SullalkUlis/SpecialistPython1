# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
ef time_f(t):
    hh = t // 3600
    mm = t // 60 - hh * 60
    ss = t % 60
    if hh < 10:
        hh = '0' + str(hh)
    if mm < 10:
        mm = '0' + str(mm)
    if ss < 10:
        ss = '0' + str(ss)
    str_out = str(hh) + ':' + str(mm) + ':' + str(ss)
    return str_out
