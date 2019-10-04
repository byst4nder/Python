#! python3
# 冒泡排序、选择排序、快速排序、插入排序、希尔排序、归并排序、基数排序以及堆排序
import random
import datetime


# 生成随机序列
#def randList(num): return [random.randint(1, 100000) for x in range(0, num)]

def randList(num=10, start=1, end=100): return [
    random.randint(start, end) for x in range(0, num)]
#lstb = list(map(lambda x: random.randint(1, 100000), range(0, 10)))

# 比较函数
def asc(a, b): return a > b
def desc(a, b): return a < b
# asc = lambda a, b: a > b
# desc = lambda a, b: a < b

def logwrite(msg:str):
    fo = open("a.log",'a',encoding='utf-8')
    fo.write('{}\n'.format(msg))


def TotalTime(fn):
    def  runtime(*args,**kwargs):
        starttime = datetime.datetime.now()
        rt = fn(*args,**kwargs)
 #       endtime = datetime.datetime.now()
        dalta=datetime.datetime.now()-starttime
        log='{0}排序时间为：{1}'.format(fn.__name__,dalta)
        logwrite(log)
        # print('{0}排序时间为：{1}'.format(fn.__name__,dalta))
        return rt

    return runtime


class ListSort():

    # 1.冒泡排序
    
    # def BubbleSort(cls, lst: list, fn=lambda a, b: a > b):
    @classmethod
    @TotalTime
    def BubbleSort(cls,lst: list, compare=asc) -> '冒泡排序':

        for i in range(0, lst.__len__()-1):
            for y in range(0, lst.__len__()-i-1):
                if compare(lst[y], lst[y+1]):
                    lst[y], lst[y+1] = lst[y+1], lst[y]
        return lst

    # 2.选择排序
    @classmethod
    @TotalTime
    def ChooseSort(cls, lst: list, compare=asc):
        for i in range(0, lst.__len__()-1):

            index = i
            temvalue = lst[i]

            for y in range(i+1, lst.__len__()):
                if compare(temvalue, lst[y]):
                    temvalue = lst[y]
                    index = y
            lst[i], lst[index] = lst[index], lst[i]
        return lst

    # 3.快速排序
    @classmethod
    def _QuickSort(cls,lst: list, start: int, end: int, compare):

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
                low += 1
            lst[hight] = lst[low]

        lst[low] = temp

        cls._QuickSort(lst, start, low-1, compare)
        cls._QuickSort(lst, low+1, end, compare)


    @classmethod
    @TotalTime
    def QuickSort(cls, lst: list, compare=asc):

        cls._QuickSort(lst, 0, lst.__len__()-1, compare)

        return lst

    # 4.插入排序
    @classmethod
    @TotalTime
    def InsertSort(cls, lst: list, compare=asc):
        for i in range(1, lst.__len__()):
            tempvalue = lst[i]
            index = i
            while index >= 1 and compare(lst[index-1], tempvalue):
                lst[index] = lst[index-1]
                index -= 1
            lst[index] = tempvalue
        return lst

    # 5.希尔排序
    @classmethod
    @TotalTime
    def ShellSort(cls, lst: list, compare=asc):

        lstlen = lst.__len__()
        gap = lstlen//2

        while gap > 0:
            for x in range(gap, lstlen):
                temp = lst[x]
                index = x
                while index > 0 and compare(lst[index-gap], temp):
                    lst[index] = lst[index-gap]
                    index -= gap
                lst[index] = temp
            gap = gap//2

        return lst


# 6.归并排序

    @classmethod
    def _merge(cls,llist, hlist, compare):

        templst = list()
        while len(llist) > 0 and len(hlist) > 0:
            if compare(llist[0], hlist[0]):
                templst.append(llist.pop(0))
            else:
                templst.append(hlist.pop(0))

            templst += llist
            templst += hlist

            return templst

    @classmethod
    def _ParallelSort(cls,lst: list, compare=asc):

        # 将待排序列拆分为2，直到分为1个为止
        lenlst = len(lst)

        if lenlst <= 1:
            return lst

        mid = lenlst//2
        lowlst = lst[:mid]
        hightlst = lst[mid:]

        ll = cls._ParallelSort(lowlst, compare)
        hl = cls._ParallelSort(hightlst, compare)

        # 返回合并序列
        return cls._merge(ll, hl, compare)

    #调用并归排序函数
    @classmethod
    @TotalTime
    def ParallelSort(cls,lst:list, compare=asc):
        cls._ParallelSort(lst,compare)

   

    # 7.计数排序
    # 1.找出待排序的数组中最大和最小的元素
    # 2.统计数组中每个值为i的元素出现的次数，存入数组C的第i项
    # 3.对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
    # 4.反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个 元素就将C(i)减去1
    @classmethod
    @TotalTime
    def CountSort(cls, lst: list, compare=asc):

        minvalue = lst[0]
        maxvalue = lst[0]
        for x in lst:
            if x > maxvalue:
                maxvalue = x
            if x < minvalue:
                minvalue = x

        # 1.创建数据范围数组
        conlst = [0]*(maxvalue-minvalue+1)

        # 2.对数组内每个数进行计数
        for x in lst:
            conlst[x-minvalue] += 1

        # 3.清空lst列表
        lst.clear()

        # 4.根据计数重新生成列表
        if compare.__name__ == 'asc':
            for z in range(0, len(conlst)):
                lst += [z+minvalue]*conlst[z]
        elif compare.__name__ == 'desc':
            for z in range(len(conlst)-1, -1, -1):
                lst += [z+minvalue]*conlst[z]

        return lst

    # 8.堆排序
    @classmethod
    @TotalTime
    def HeapSort(cls, lst: list, compare=asc):
        n = len(lst)

        for lstlen in range(n, 1, -1):

            # 根据二叉树深度循环
            for depth in range(lstlen//2-1, -1, -1):
                # 在左、右孩子中找最大的数与节点交换
                lift = 2*depth+1
                # if lift+1 < lstlen:
                #     if lst[lift] < lst[lift+1]:
                #         lift += 1
                # if lst[depth] < lst[lift]:
                #     lst[depth], lst[lift] = lst[lift], lst[depth]

                if compare(lstlen, lift+1):
                    if compare(lst[lift+1], lst[lift]):
                        lift += 1
                if compare(lst[lift], lst[depth]):
                    lst[depth], lst[lift] = lst[lift], lst[depth]

            if compare(lst[0], lst[lstlen-1]):
                lst[0], lst[lstlen-1] = lst[lstlen-1], lst[0]

        return lst

    # 9.基数排序

    @classmethod
    @TotalTime
    def CardinalitySort(cls, lst: list, compare=asc):

        temlist = [[] for x in range(0, 10)]

        base = 10

        # 获取最大位数
        maxdepth = 1
        for x in lst:
            while x >= base:
                maxdepth += 1
                base *= 10

        for depth in range(0, maxdepth):

            for i in lst:
                temlist[(i//10**depth) % 10] += [i]
            lst.clear()

            for i in temlist:
                for y in i:
                    lst += [y]
                i.clear()
        if compare.__name__ == 'asc':
            pass
        elif compare.__name__ == 'desc':
            for i in range(0, len(lst)//2):
                lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]

        return lst




