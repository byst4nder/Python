from sortLearn import asc
from sortLearn import desc
from sortLearn import randList
from sortLearn import ListSort
from sortLearn import logwrite
import sortLearn


for i in range(1,50):
    n=randList(1,10,1000000)[0]
    s=randList(1,1,1000)[0]
    e=randList(1,1000,10000000)[0]
    logwrite('\n本次排序情况：排序量为{}，数字区间为{}至{}'.format(n,s,e))
    myclass=ListSort()
    lst = randList(n,s,e)
    #选择排序
    ListSort.ChooseSort(lst,desc)
    lst = randList(n,s,e)
    #冒泡排序
    ListSort.BubbleSort(lst,desc)
    lst = randList(n,s,e)
    #基数排序
    ListSort.CardinalitySort(lst,desc)
    lst = randList(n,s,e)
    #计数排序
    ListSort.CountSort(lst,desc)
    lst = randList(n,s,e)
    #堆排序
    ListSort.HeapSort(lst,desc)
    lst = randList(n,s,e)
    #插入排序
    ListSort.InsertSort(lst,desc)
    lst = randList(n,s,e)
    #希尔排序
    ListSort.ShellSort(lst,desc)
    lst = randList(n,s,e)
    #归并排序
    ListSort.ParallelSort(lst,desc)
    lst = randList(n,s,e)
    #快速排序
    ListSort.QuickSort(lst,desc)
    print('循环了第{}次'.format(i))



