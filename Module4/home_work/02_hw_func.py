# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(p_a, p_b, p_c):
    xa, ya = p_a
    xb, yb = p_b
    xc, yc = p_c
    len_lin_ab = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
    print(len_lin_ab, 'AB')
    len_lin_ac = ((xc - xa) ** 2 + (yc - ya) ** 2) ** 0.5
    print(len_lin_ac, 'AC')
    len_lin_cb = ((xc - xb) ** 2 + (yc - yb) ** 2) ** 0.5
    print(len_lin_cb, 'CB')
    if len_lin_ab > len_lin_ac > len_lin_cb:
        return ' CB'
    elif len_lin_ab > len_lin_ac:
        return 'AC'
    else:
        return 'AB'


# TODO: your code here
print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
