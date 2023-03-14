"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
first_word = 'разработка'
second_word = 'фдминистрирование'
third_word = 'protocol'
fourth_word = 'standart'

lst = [first_word, second_word, third_word, fourth_word]
new_lst = []
lst2 = []
for i in lst:
    new_lst.append(i.encode('utf-8'))
print(new_lst)

for j in new_lst:
    lst2.append(j.decode('utf-8'))
print(lst2)
