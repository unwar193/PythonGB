'''5) Создать (программно) текстовый файл, записать в него программно набор
чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в
файле и выводить ее на экран.'''

'''Код с "заХардКоджеными" значениями на запись в файл"'''
with open('task05.txt', 'w', encoding='utf-8') as my_obj:
    print(55, 25, 15, file=my_obj)

with open('task05.txt', 'r', encoding='utf-8') as my_obj:
    line = my_obj.readlines()
    res_sum = 0
    for el in line:
        my_num = el.split()
        for i in my_num:
            res_sum += int(i)
print(res_sum)

'''Тот же код с вводом значений в файл через ф-ю "input"'''
# with open('task05.txt', 'w', encoding='utf-8') as my_obj:
#     print(input('введите числа через пробел: '), file=my_obj)
#
# with open('task05.txt', 'r', encoding='utf-8') as my_obj:
#     line = my_obj.readlines()
#     res_sum = 0
#     for el in line:
#         my_num = el.split()
#         for i in my_num:
#             res_sum += int(i)
# print(res_sum)