# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    if x2 - x1 == 0 and x3 - x1 == 0:
        return False
    elif x3 - x1 != 0:
        x2, x3 = x3, x2  # меняем местами 2 и 3 точки
        y2, y3 = y3, y2
    k = (y2 - y1) / (x2 - x1)     # уравнение прямой по любым 2 точкам 
    b = y2 - x2 * k
    return y3 != k * x3 + b  # проверяем может ли точка лежать на  прямой если да то нельзя построить треугольник

# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
