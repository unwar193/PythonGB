'''2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

my_f = open('task02.txt', 'r', encoding='utf-8')
cont = my_f.readlines()
cont_length = len(cont)
print(f'Число строк: {cont_length}')
count_words = [len(el.split()) for el in cont]
print(f'Число слов в строках: {count_words}')
my_f.close()
