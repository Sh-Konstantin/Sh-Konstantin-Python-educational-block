
import math
from operator import truediv
a = "1 2 3 45 5"
str_1 = a.split()
new_str_1 = []
for i in str_1:
    new_str_1.append(int(i))
print(new_str_1)
print(max(new_str_1), min(new_str_1))
new_str_1.sort()
print(new_str_1[-1], new_str_1[0])


A = float(input('Введите А '))
B = float(input('Введите B '))
C = float(input('Введите C '))
# D = B ** 2 - 4 * A * C
# x = 0
# x1 = 0
# if 
#   D == 0:
#   x = -B/(2*A)
#   print(f'Уровнение имеет корень = {x}')
# elif 
#   D > 0:
#   x1 = (-B + D ** 0.5)/(2*A)
#   x = (-B - D ** 0.5)/(2*A)
#    print(f'Уровнение имеет корни = {x} {x1}')
# else:
#   print('Уровнение не имеет корней')

D = pow(B, 2) - 4 * A * C
if D == 0:
    x = -B/(2*A)
    print(f'Уровнение имеет корень = {x}')
elif D > 0:
    x1 = (-B + math.sqrt(D))/(2*A)
    x = (-B - math.sqrt(D))/(2*A)
    print(f'Уровнение имеет корни = {x} {x1}')
else:
    print('Уровнение не имеет корней')


A = int(input('Введите А '))
B = int(input('Введите B '))
def Efclid(a,b):
    while a!=0 and b !=0:
        if a>b:
            a = a%b
        else:
            b = b%a
        return a+b

print(A*B/Efclid(A,B))