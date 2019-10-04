# list排序函数
import random
import datetime

# 生成一个随机数序列
lst = list(random.sample(range(1, 1000), 10))
lst2 = list(random.sample(range(1, 1000), 10))
print('{0}{1}{0}'.format('*'*30, '初始序列'))
print(lst)


def listrand():
    yield random.randint(1, 10000)

print(datetime.datetime.now())
def g(x): return x+1


print(g(2))

lambda x: random.randint(1, 10000)
print('{0}{1}{0}'.format('*'*30, '初始序列2'))

#print([random.randint(1, 10000) for x in range(1, 10)])


def listRnd(num=10, start=1, stop=10000): return [random.randint(start, stop) for x in range(1, num)]


print(listRnd(20))

'''
print(l(5))
print('{0}{1}{0}'.format('*'*30, '初始序列3'))
#print(random.randint(1, 10000))
print('{0}{1}{0}'.format('*'*30, '初始序列'))
#lst3 = [(lambda: random.randint(1, 10000)) for x in range(1, 10)]

lambda x, y: x*y

# print(lst3)
# 定义一个sortlist函数，对序列进行排序; 直接插入法，返回新序列


def sortlist(lst, key=1):
    if key != 1 and key != 0:
        return 'useage:sortlist(list,key);\nlist为列表;\nkey升序为1，降序为0。'

    newlst = []
    for i in lst:
        for y, m in enumerate(newlst):
            if key == 1 and i < m:
                newlst.insert(y, i)
                break
            elif key == 0 and i > m:

                newlst.insert(y, i)
                break
        else:
            newlst.append(i)
    return newlst


# 定义一个bubbleSortlist函数，对序列进行排序；冒泡法排序，原序列排序，不返回新序列
def bubbleSortlist(lst, key=1):
    if key != 1 and key != 0:
        return 'useage:sortlist(list,key);\nlist为列表;\nkey升序为1，降序为0。'

    for i in range(0, len(lst)-1):
        for y in range(0, len(lst)-i-1):
            if key == 1 and lst[y] > lst[y+1]:
                temp = lst[y]
                lst[y] = lst[y+1]
                lst[y+1] = temp
            elif key == 0 and lst[y] < lst[y+1]:
                temp = lst[y]
                lst[y] = lst[y+1]
                lst[y+1] = temp
    return lst


# 优化bubbleSortlist函数，对序列进行排序；冒泡法排序，原序列排序，不返回新序列
def bubbleSortlist2(lst, key=1):
    if key != 1 and key != 0:
        return 'useage:sortlist(list,key);\nlist为列表;\nkey升序为1，降序为0。'

    for i in range(0, len(lst)-1):
        for y in range(0, len(lst)-i-1):
            if key == 1 and lst[y] > lst[y + 1]:
                lst[y], lst[y + 1] = lst[y + 1], lst[y]
            elif key == 0 and lst[y] < lst[y + 1]:
                lst[y], lst[y + 1] = lst[y + 1], lst[y]
    return lst


# SelectSortlist函数，对序列进行排序；选择排序法
def SelectSortlist(lst, key=1):
    if key != 1 and key != 0:
        return 'useage:sortlist(list,key);\nlist为列表;\nkey升序为1，降序为0。'

    for i in range(0, len(lst)-1):
        minIndex = i
        for y in range(i+1, len(lst)):
            if key == 1 and lst[minIndex] > lst[y]:
                minIndex = y
            elif key == 0 and lst[minIndex] < lst[y]:
                minIndex = y
        if minIndex != i:
            lst[minIndex], lst[i] = lst[i], lst[minIndex]
    return lst


# InsertSortlist函数，对序列进行排序；选择排序法
def InsertSortlist(lst, key=1):
    if key != 1 and key != 0:
        return 'useage:sortlist(list,key);\nlist为列表;\nkey升序为1，降序为0。'

    for i in range(0, len(lst)-1):
        count = i
        temp = lst[i + 1]
        if key == 1:
            while temp < lst[count] and count >= 0:
                lst[count + 1] = lst[count]
                count -= 1
        elif key == 0:
            while temp > lst[count] and count >= 0:
                lst[count + 1] = lst[count]
                count -= 1
        lst[count+1] = temp
    return lst


# ShellSortlist函数，对序列进行排序；希尔排序法
def ShellSortlist(lst, key=1):
    if key != 1 and key != 0:
        return 'useage:sortlist(list,key);\nlist为列表;\nkey升序为1，降序为0。'

    lenlst = len(lst)
    gap = int(lenlst/2)

    while gap > 0:
        for i in range(gap, lenlst):
            temp = lst[i]
            preIndex = i - gap
            while preIndex >= 0 and lst[preIndex] > temp:
                lst[preIndex + gap] = lst[preIndex]
                preIndex -= gap
            lst[preIndex + gap] = temp
        gap = int(gap/2)

    return lst


def shell(arr):
    n = len(arr)
 #   h = 1
#    while h < n/3:
    h = n//3+1
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and arr[j] < arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j -= h
        h = h//3
    return arr


print('{0}{1}{0}'.format('*'*30, shell.__name__))
print(shell(lst))

# 调用list排序函数
print('{0}{1}{0}'.format('*'*30, sortlist.__name__))
print(sortlist(lst))
print(sortlist(lst, 0))
print('{0}{1}{0}'.format('*'*30, bubbleSortlist.__name__))
print(bubbleSortlist(lst))
print(bubbleSortlist(lst, 0))
print(bubbleSortlist2(lst))
print(bubbleSortlist2(lst, 0))
print('{0}{1}{0}'.format('*'*30, SelectSortlist.__name__))
print(SelectSortlist(lst))
print('{0}{1}{0}'.format('*'*30, SelectSortlist.__name__))
print(SelectSortlist(lst, 0))
print('{0}{1}{0}'.format('*'*30, 'lst2原始序列'))
print(lst2)
#print('{0}{1}{0}'.format('*'*30, InsertSortlist.__name__))
# print(InsertSortlist(lst2))
#print('{0}{1}{0}'.format('*'*30, InsertSortlist.__name__))
#print(InsertSortlist(lst2, 0))

print('{0}{1}{0}'.format('*'*30, ShellSortlist.__name__))
print(ShellSortlist(lst2, 0))

print(shell(lst))
'''
