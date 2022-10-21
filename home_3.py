# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from decimal import Decimal

given_list_real = [1.5, 1.2, 3.003, 5, 10.01]


def convert():

    list_str = list(map(str, given_list_real))
    list_decimal = list(map(Decimal, list_str))
    list_fractal = [i - int(i) for i in list_decimal]
    list_without_zero = list(filter(lambda x: x != 0, list_fractal))
    return (list_without_zero)


res = convert()
result = max(res) - min(res)

print(result)
