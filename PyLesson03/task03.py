"""
3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""
arg_1 = int(input('введите первое число:'))
arg_2 = int(input('введите второе число:'))
arg_3 = int(input('введите третье число:'))


def sum_two_of_three(arg_01, arg_02, arg_03):
    my_list = [arg_01, arg_02, arg_03]
    my_list.sort()
    my_sum = my_list[2] + my_list[1]
    return my_sum


print(sum_two_of_three(arg_1, arg_2, arg_3))
