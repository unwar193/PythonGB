"""
2) Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""

user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_year = input('Введите год рождения: ')
user_city = input('Введите ваш город: ')
user_email = input('Введите ваш email: ')
user_phone_num = input('Введите номер телефона: ')


def get_user_info(**kwargs):
    return kwargs


print(get_user_info(Имя=user_name, Фамилия=user_surname, Год=user_year,
                    Город=user_city, Email=user_email, Номер=user_phone_num))
