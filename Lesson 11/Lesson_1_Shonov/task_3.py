"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""
first_word = 'attribute'
second_word = 'класс'
third_word = 'функция'
fourth_word = 'type'

lst = [first_word, second_word, third_word, fourth_word]
for i in lst:
    try:
        print(bytes(i, 'ascii'))

    except UnicodeError:
        print('значение переменной ошибка')
