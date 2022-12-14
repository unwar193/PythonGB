'''4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.'''

my_num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task04.txt', 'r', encoding='utf-8') as my_obj:
    my_line = my_obj.readlines()
    for el in my_line:
        if el.split()[0] in my_num_dict:
            with open('task04_result.txt', 'a', encoding='utf-8') as my_obj2:
                print(f'{my_num_dict[el.split()[0]]} - {el.split()[2]}',
                      file=my_obj2)
    print('Данные записаны в файл "task04_result.txt"')
