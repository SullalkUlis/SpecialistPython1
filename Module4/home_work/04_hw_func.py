# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def nod(a, b):
    if a == 0:
        return a
    a = abs(a)
    b = abs(b)
    while True:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
        elif a == b:
            return a
            break

# ---------------------------------- арифметическое действие--------------
def act_d(a, b, ac):
    if ac == '+':
        return a + b
    else:
        return a - b
# ---------------------- перевод дробей и вычисление

def my_math(c_ch, chis, znam, act):
    for i in range(len(c_ch)):
        chis[i] = znam[i] * abs(c_ch[i]) + chis[i]
        if c_ch[i] < 0:
            chis[i] = chis[i] * -1
    for i in range(len(c_ch) - 1):
        chis[i + 1] = act_d(chis[i] * znam[i + 1], chis[i + 1] * znam[i], act[i])
        znam[i + 1] = znam[i] * znam[i + 1]

# -------------------------- разбор строки подготовка данных и сбор строки для вывода
def m_oper(str_m):
    c_c = ''
    priz = ''
    c_ch = []
    chis = []
    znam = []
    act = []
    #===============Разбор строки и формирование списков для обработки данных==========
    for i in range(len(str_m)):
        if str_m[i].isdigit():
            c_c = c_c + str_m[i]
        if str_m[i] == ' ' and priz != '/' and c_c != '':
            c_ch.append(int(c_c))
            c_c = ''
        if str_m[i] == '/' and (c_c != '' or c_c != '-'):
            chis.append(int(c_c))
            priz = '/'
            c_c = ''
        if str_m[i] == ' ' and priz == '/':
            znam.append(int(c_c))
            c_c = ''
        if (str_m[i] == '+' or str_m[i] == '-') and not str_m[i + 1].isdigit():
            act.append(str_m[i])
            priz = str_m[i]
            if len(c_ch) > len(znam):
                chis.append(int(c_ch[-1]))
                c_ch[-1] = 0
                znam.append(1)
            c_c = ''
        if str_m[i] == '-' and str_m[i + 1].isdigit():
            priz = '--'
            c_c = '-'
        if i == len(str_m) - 1 and str_m[i].isdigit():
            if priz == '/':
                znam.append(int(c_c))
            else:
                c_ch.append(int(c_c))
                if len(c_ch) > len(znam):
                    chis.append(int(c_ch[-1]))
                    c_ch[-1] = 0
                    znam.append(1)
    #print(c_ch, ' ', chis, ' ', znam, ' ', act)
    #==========обработка и формирование результата=======================
    my_math(c_ch, chis, znam, act)
    el_ch = chis[-1]
    el_zn = znam[-1]
    if nod(el_ch, el_zn) == 0:
        result = 0
        return result
    el_c = el_ch / nod(el_ch, el_zn)
    el_z = el_zn / nod(el_ch, el_zn)
    c_c = el_c / el_z
    if c_c % 1 == 0:
        result = str(int(c_c))
        return result
    if c_c > 1:
        c_c = str(int(c_c))
        c_h = int(el_c % el_z)
    elif 0 < c_c < 1:
        c_c = ''
        c_h = int(el_c)
    elif -1 < c_c < 0:
        c_c = ''
        c_h = int(el_c)
    else:
        c_c = str(int(c_c))
        c_h = int(abs(el_c) % el_z)
    zn = int(el_z)
    result = str(c_c) + ' ' + str(c_h) + '/' + str(zn)
    return result



