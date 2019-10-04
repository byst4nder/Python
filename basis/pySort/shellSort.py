#!python 3
# 这是一个希尔排序算法
import random


def shllSort(lst: list):

    lenlst = len(lst)
    gap = lenlst//2

    while gap > 0:  # 判断循环终止

        for x in range(gap, lenlst):  # 分组循环

            temp = lst[x]
            index = x

            while index >= gap and lst[index-gap] > temp:  # 插入排序法
                lst[index] = lst[index-gap]
                index -= gap

            lst[index] = temp
        gap = gap//2

    return lst


def InsertSort(lst: list):

    lenlst = len(lst)

    for x in range(1, lenlst):

        indexi = x
        temp = lst[indexi]

        while indexi >= 1 and temp < lst[indexi-1]:
            lst[indexi] = lst[indexi-1]
            indexi -= 1

        lst[indexi] = temp

    return lst

# 分组插入排序实现  gap  是分组数量   n为组号


def InsertGapSort(lst: list, gap=1, n=1):

    lenlst = len(lst)

# 如果没有gap步长值，对所有分组组内插入排序
    for x in range(gap+n-1, lenlst, gap):

        indexi = x
        temp = lst[indexi]

        while indexi >= gap and temp < lst[indexi-gap]:
            lst[indexi] = lst[indexi-gap]
            indexi -= gap

        lst[indexi] = temp

    return lst


# 分组插入排序实现  gap  是分组数量


def InsertGapAllSort(lst: list, gap=1):

    lenlst = len(lst)

    for x in range(gap, lenlst):

        indexi = x
        temp = lst[indexi]

        while indexi >= gap and temp < lst[indexi-gap]:
            lst[indexi] = lst[indexi-gap]
            indexi -= gap

        lst[indexi] = temp

    return lst

# 将单个值插入分组排序位置


def insertN(lst: list, n, i):

    i -= 1 
    temp = lst[i]

    while i >= n and lst[i-n] < temp:
        lst[i] = lst[i-n]
        i -= n
    lst[i] = temp
    return lst

lst = random.sample(list(range(1, 10000)), 12)
print('{0}{1}{0}'.format('#'*30, '打印LST原始序列'))
print(lst)
# print('{0}{1}{0}'.format('#'*30, InsertSort.__name__))
# print(InsertSort(lst))
#print(InsertGapSort(lst, 2, 1))
#print(InsertGapSort(lst, 2, 2))
# print(shllSort(lst))
#print(InsertGapAllSort(lst, 3))
print(insertN(lst,2,10))
