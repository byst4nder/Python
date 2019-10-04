
import datetime
import time
from sortLearn import randList
from sortLearn import asc
from sortLearn import desc


# starttime = datetime.datetime.now()
# endtime = datetime.datetime.now()
# time.sleep(2)
# dalta = (datetime.datetime.now()-starttime)
# print('{0}\t{1}\t{2}'.format(starttime,endtime, dalta))


def TotalTime(fn):
    def  runtime(*args,**kwargs):
        starttime = datetime.datetime.now()
        rt = fn(*args,**kwargs)
 #       endtime = datetime.datetime.now()
        dalta=datetime.datetime.now()-starttime
        print('{0}排序时间为：{1}'.format(fn.__name__,dalta))
        return rt

    return runtime

@TotalTime
def BubbleSort(lst: list, compare=asc) -> '冒泡排序':

    for i in range(0, lst.__len__()-1):
        for y in range(0, lst.__len__()-i-1):
            if compare(lst[y], lst[y+1]):
                lst[y], lst[y+1] = lst[y+1], lst[y]
    return lst


# 3.快速排序

def _QuickSort(lst: list, start: int, end: int, compare):

    if start >= end:
        return

    temp = lst[start]
    low = start
    hight = end

    while low < hight:

        while compare(lst[hight], temp) and low < hight:
            hight -= 1
        lst[low] = lst[hight]

        while (compare(temp, lst[low]) or temp == lst[low]) and low < hight:
        # while compare(temp, lst[low]) and low < hight:
            low += 1
        lst[hight] = lst[low]

    lst[low] = temp

    _QuickSort(lst, start, low-1, compare)
    _QuickSort(lst, low+1, end, compare)



@TotalTime
def QuickSort(lst: list, compare=asc):

    _QuickSort(lst, 0, lst.__len__()-1, compare)

    return lst



#foo = TotalTime(BubbleSort)
lst = randList(5000,1,100000)
lst=[5,8,5,4,1,5,3,2,5,10]
print(lst)
QuickSort(lst,asc)
print(lst)