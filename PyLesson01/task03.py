# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = str(input("Введите число: "))
n_2 = f'''{n}''' + f'''{n}'''
n_3 = f'''{n}''' + f'''{n}''' + f'''{n}'''
res = int(n) + int(n_2) + int(n_3)
print(res)