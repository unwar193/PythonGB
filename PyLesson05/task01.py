'''1) Создать программно файл в текстовом формате, записать в него
 построчно данные, вводимые пользователем. Об окончании ввода данных
 свидетельствует пустая строка.'''

user_data = input('введите свои данные: ')

my_f = open('task.01.txt', "a", encoding='utf-8')
my_f.write(user_data + '\n')
print('')
my_f.close()
