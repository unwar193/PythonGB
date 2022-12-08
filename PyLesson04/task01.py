'''1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.'''

from sys import argv

script_name, emp_production, emp_bid, emp_premium = argv


def user_salary(emp_data):
    return print(f'Зар. плата равна: '
                 f'{(int(emp_data[1]) * int(emp_data[2])) + int(emp_data[3])}'
                 f' $')


user_salary(argv)
