# создать число с заданной точностью N

value_precision = input("значение точности \n")
k = 1
pi = 0

for i in range(1000000):
    if i % 2 == 0:
        pi += 4/k
    else:
        pi -= 4/k
    k += 2
print (pi)
print (f'\n число пи с точность {value_precision}: {str(pi)[:len(value_precision)]}\n')


# задайте натуральное число n напишите программу для создания списка простых множителей n

n = int (input('введите число '))
i = 2
lst = []
temp = n
while i <= temp:
    if not temp %i:
        lst.append(i)
        temp//=i
        i = 2
    else:
        i+=1
print(lst)
print (f'{len(lst)} - количество простых множителей')

#  задайте последовательност чисел. напишите программу которая выведет список неповторяющихся элементов 

A = list(map(float, input().split()))
B = []
for i in A:
    if i not in B:
        B.append(i)
B.sort()
print (B)


#  задана натуральная степень k сформировать случайным образом список коэффициентов (0 до 100) многочлена и записать в файл многочлен степени k.
from random import randint
K = int (input("степень числа = "))
def str (sp):
    lst = sp[::-1]
    wr = ' '
    if len(lst) < 1:
        wr = ' x = 0 '
    else:
        for i in range (len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i -1 }'
                if lst [i+1] != 0:
                    wr += '+'
            elif i == len (lst) - 2 and lst [i] != 0:
                wr += f'{lst[i]}x'
                if lst [i+1] != 0:
                    wr += '+'
            elif i == len (lst) - 1 and lst [i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len (lst) - 1 and lst [i] == 0:
                wr += ' =0'
    return wr

p = [randint(0,101) for i in range(K+1)]
result = str(p)
with open ('res.txt' , "w") as text:
    text.write (result)
print (result, '\n\n')
