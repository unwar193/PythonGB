# 2) Для списка реализовать обмен значений соседних элементов, т.е. значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

my_list = input("Введите элементы списка через пробел: ").split()

for i in range(0, len(my_list) - 1, 2):
    temp_el = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = temp_el

print(my_list)
