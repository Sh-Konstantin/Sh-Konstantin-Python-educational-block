
# вывести массив с элементами не имеющих повторений
# Lst = [1, 2, 3, 5, 7, 8, 10, 1, 8, 10, 11, 3, 5, 8]

def sort (lst):
    uniq_elements = set()               # используем множества
    for el in lst:                      # берем каждый элемент 
        if el not in uniq_elements:     # если элемента нет
            uniq_elements.add(el)       # добавляе элемент 
        else:
            uniq_elements.discard(el)   # удаляе элемент если он там есть  
    s = list(uniq_elements)
    s.sort()                            # сортируем
    return s 