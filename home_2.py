# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

given_list = [2, 3, 4, 5, 6]


def couple_of_list():
    half_elements = (len(given_list)+1)//2
    for i in range(half_elements):
        print(given_list[i] * given_list[-i-1],end = " ")


print(
    f"произведение пар чисел списка {given_list} по заданному условию равно ")
couple_of_list()
