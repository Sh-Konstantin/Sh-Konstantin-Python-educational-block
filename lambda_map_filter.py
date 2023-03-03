# в списке хранятся числа. нужно выбрать только четный числа и составить пары ( число, квадрат числа )
n = [1, 2, 3, 4, 5, 7, 9, 13, 58]
lst = list()

for i in n:
    if i % 2 == 0:
        lst.append((i, i**2))
print(lst)




# запишем с использованимем lambda



def sel(u, y):
    return [u(x) for x in y]


def vel(u, y):
    return [x for x in y if u(x)]

d = [1, 2, 3, 4, 5, 7, 9, 13, 58]
res = sel(int, d)
res = vel(lambda x: x % 2 == 0, res)
res = sel(lambda x: (x, x**2), res)
print(res)


# запишем с использованимем map

def vel(u, y):
    return [x for x in y if u(x)]

d = [1, 2, 3, 4, 5, 7, 9, 13, 58]
res = map(int, d)
res = vel(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)

# запишем с использованимем filter

d = [1, 2, 3, 4, 5, 7, 9, 13, 58]
res = map(int, d)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)