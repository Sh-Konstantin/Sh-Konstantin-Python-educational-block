import math
import random
# Задачи:
# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n =  [1, 2, 3, 4, 5]

def Summ(n):
    a=0
    for i in range(len(n)):
        if n[i]%2!=0:
            a=a+n[i]
    return a
print(Summ(n))

# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o [2, 3, 4, 5, 6] => [12, 15, 16];
# o [2, 3, 5, 6] => [12, 15]

n = list(map(int, input("ведите несколько цифр через пробел \n").split()))
product = []

if  len(n) == 2:
    product.append(n(0)*n[1])
else:
    if len(n) % 2 ==0:
        for i in range  (len(n)//2):
            product.append(n[i]*n[len(n)-i-1])
    else:
        for i in range  (len(n)//2+1):
            product.append(n[i]*n[len(n)-i-1])
print (product)


# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

A = list(map(float, input().split()))
B = []
for i in range (len(A)):
    c = A[i]
    c, _ = math.modf(c)
    B.append ("%.2f"%c)

d = float(max(B)) - float(min(B))
print (d)


# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10

d = int (input("введите число "))
res = bin(d)
print (res)


# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def FibFunc(n):
    if n == 0:
        return 0
    NF = False
    if n < 0:
        NF = True
        n *= -1
    f1 = 1
    f2 = 2
    i = 0
    while i < n-2:
        fs = f1+f2
        f2 = f1
        f1 = fs
        i = i + 1
    if NF:

        f1 = (-1)**(n+1)*f1
    return f1

k = int(input(""))
fib = []


for i in range(-k, k+1):
    fib.append(FibFunc(i))
print(fib)