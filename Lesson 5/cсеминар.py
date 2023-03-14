from memory_profiler import memory_usage 
def decor (func):
    def wrapper (*args,**kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_dif = m2[0] - m1[0]
        # print (f"memory {mem_dif} Mib")
        return res, mem_dif
    
    return wrapper

# @decor
# def check_even_2 (numbers):
#     my_list = [num*num for num in numbers if num % 2 == 0]
#     return my_list

# res, mem_diff = check_even_2 (list(range(100000)))
# print (f"время {mem_diff} Mib")


@decor
def check_even_1(lst):
    new_list = [i for i in lst if i % 2 == 0]
    return new_list
res, mem_diff = check_even_1 (list(range(100000)))
print (f"время {mem_diff} Mib")

@decor
def check_even_2(lst):
    new_list = filter(lambda x: x % 2 == 0, lst)
  
    return new_list
res, mem_diff = check_even_2 (list(range(100000)))
print (f"время {mem_diff} Mib")

check_even_1(list(range(5000000)))
check_even_2(list(range(5000000)))