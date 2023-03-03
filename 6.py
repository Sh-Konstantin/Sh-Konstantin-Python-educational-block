# написать программу которая реализует алгоритм создания случаныйх числе без метода random
import time

def Ram (i1=0,i2=1):
    sec = time.time()
    Next = True
    while Next:
        R = i2 * (sec%1)
        if R >= i1 or R>i2: Next= False
    return int(R)
print (Ram(1,1000))