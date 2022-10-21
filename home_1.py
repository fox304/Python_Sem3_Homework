# Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

given_list = [2, 3, -5, 6, 7, 8, -9]


def sum_elem_odd_position():
    my_sum = 0
    for i, j in enumerate(given_list):
        if i % 2:
            my_sum += j
    return my_sum


result = sum_elem_odd_position()

print(f"сумма элементов списка {given_list}, стоящих на нечётной позиции равна ",result)
