"""3) Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор."""

# for el in range(20, 241):
#     if el % 20 == 0 or el % 21 == 0:
#         print(el)

# [print(el) for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]

# print(list.append(el) for el in range(20, 241) if el % 20 == 0 or el % 21 == 0)

# print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

print(list([i for i in range(20, 241) if i % (20 or 21) == 0]))