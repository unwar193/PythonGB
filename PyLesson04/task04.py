"""4) Представлен список чисел. Определить элементы списка, не имеющие 
повторений.Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке. Для выполнения 
задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]"""


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list, duplicates = [], []
for value in my_list:
    if my_list.count(value) > 1 and value not in duplicates:
        duplicates.append(value)

new_list_gen = [new_list.append(el) for el in my_list if el not in duplicates]
print(new_list)