#! python3
# 这是一个计数排序算法

import random


def randList(num=10,start=1,end=100): return [random.randint(start, end) for x in range(0, num)]


def CountSort(lst: list):
    
    minvalue = lst[0]
    maxvalue = lst[0]
    for x in lst:
        if x > maxvalue:
            maxvalue = x
        if x < minvalue:
            minvalue = x

    # 1.创建数据范围数组
    conlst = [0 for i in range(minvalue, maxvalue+1)]

    # 2.对数组内每个数进行计数
    for x in lst:
        conlst[x-minvalue] += 1

    # 3.清空lst列表
    lst.clear()

    # 4.根据计数重新生成列表
    for z in range(0, len(conlst)):
        lst += [z+minvalue]*conlst[z]

    return lst


lst = randList(150,30,10000)

print(len(lst),CountSort(lst))

