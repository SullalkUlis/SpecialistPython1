# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    # TODO: your code here
   return  ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5 < r # даже не на самой окружности

# Не забудьте протестировать вашу функцию
