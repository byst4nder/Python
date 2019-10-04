# ！python3
# 基数排序
# 算法执行步骤：
# (1)遍历序列找出最大的数(为的是确定最大的数是几位数)；
# (2)开辟一个与数组大小相同的临时数组tmp；
# (3)用一个count数组统计原数组中某一位(从低位向高位统计)相同的数据出现的次数；
# (4)用一个start数组计算原数组中某一位(从最低位向最高位计算)相同数据出现的位置；
# (5)将桶中数据从小到大用tmp数组收集起来；
# (6)重复(3)(4)(5)直到所有位都被统计并计算过，用tmp收集起来；
# (7)将tmp数组拷回到原数组中；


import random

# 生成随机序列


def randList(num=10, start=1, end=100): return [
    random.randint(start, end) for x in range(0, num)]

# 基数排序


def CardinalitySort(lst: list):

    temlist = [[] for x in range(0, 10)]

    base = 10
    maxdepth = 1
    for x in lst:
        while x >= base:
            maxdepth += 1
            base *= 10

    for depth in range(0, maxdepth):
        for i in lst:
            temlist[(i//10**depth) % 10] += [i]
        # print(depth, temlist)
        # print()
        lst.clear()

        for i in temlist:
            for y in i:
                lst += [y]
            i.clear()

    return lst


lst = randList(100, 1, 1000)
print(CardinalitySort(lst))
