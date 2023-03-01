# программа принимает на ввод число N выдает последовательность N чисел:

import string
num = int(input("введите число N \n"))
lst1 = [(-3)**i for i in range(0, num)]
print(lst1)

# для натурального n создать список последовательности 3n + 1

n = int(input("введите число N \n"))
lst = [(3*i+1) for i in range(1, n+1)]
print(lst)

# программа в которой пользователь задает 2 строки, а программа определяет количество вхождений одной строки в другую

str1 = input('insert string1 \n')
str2 = input('insert string2 \n')
print(str1.count(str2))

# (работает не корректно надо доработать )
count = 0
k = 0
if (len(str2) > 1):
    for i in range(1, len(str1)):
        if str2 in str1[k:1]:
            count = + 1
            k = i
else:
    for j in range(len(str1)):
        if str1[j] == str2:
            count = +1
print(count)
