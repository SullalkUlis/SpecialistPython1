# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(*args):
    # TODO: тело из предыдущей задачи
    def average(*args):
    print(*args,'++')
    ar = args[0]
    count_arg = 0
    summa = 0
    for arg in ar:
        count_arg += 1
        summa = summa + arg
        print(arg, ':', count_arg, ':', summa)
    return summa / count_arg


def gen_list(size, at=-10, to=10):
    import random  # импорт в функции возможен, но не рекомендуется PEP-8
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list


my_list = gen_list(10)
my_tuple = 5, 7, -4, 10, 8
