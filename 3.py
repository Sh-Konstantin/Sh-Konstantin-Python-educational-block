import random
import math

# 14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


users_num = float(input('Укажите вещественное число: '))
a = str (users_num)
nums_sum = 0
for num in a:
    if num.isdigit(): nums_sum += int(num)
print(nums_sum)


# 15). Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


Num = int (input('введите число \n'))
print ()
for i in range (1,Num+1):
    print (math.factorial(i) )

# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.


n = int(input('задайте число элементов последовательности \n'))
lst = [(1+1/i)**i for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {sum(lst)}')


# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2 

N = int(input("введите значение границ списка \n "))
lst = []
pos = 1

with open("numb_position.txt", 'w') as File:
    numb_position = random.randint(1, N)
    for i in range(0, numb_position):
        File.writelines(str(random.randrange(0, N+1)) + '\n')

for i in range(-N, N+1):
    lst.append(i)
print (lst)

with open("numb_position.txt", 'r') as File:
    for line in File:
        pos *= lst[int(line)]
print (pos)
# # 18). Реализуйте алгоритм перемешивания списка.

size = int (input(" размер списка \n"))
lst1 = list([random.randint(1,10) for i in range (size)])
print (lst1)
random.shuffle(lst1)
print (lst1)
#
