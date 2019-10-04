import random
from sortLearn import TotalTime

def randList(num): return [random.randint(1, 100000) for x in range(0, num)]

# 快速排序 传入列表、开始位置和结束位置

@TotalTime
def quick_sort(li: list, start, end):
    # 如果start和end碰头了，说明要我排的这个子数列就剩下一个数了，就不用排序了
    if not start < end:
        return

    mid = li[start]  # 拿出第一个数当作基准数mid
    low = start  # low来标记左侧从基准数始找比mid大的数的位置
    high = end  # high来标记右侧end向左找比mid小的数的位置

    # 我们要进行循环，只要low和high没有碰头就一直进行,当low和high相等说明碰头了
    while low < high:
        # 从high开始向左，找到第一个比mid小或者等于mid的数，标记位置,（如果high的数比mid大，我们就左移high）
        # 并且我们要确定找到之前，如果low和high碰头了，也不找了
        while low < high and li[high] > mid:
            high -= 1
        # 跳出while后，high所在的下标就是找到的右侧比mid小的数
        # 把找到的数放到左侧的空位 low 标记了这个空位
        li[low] = li[high]
        # 从low开始向右，找到第一个比mid大的数，标记位置,（如果low的数小于等于mid，我们就右移low）
        # 并且我们要确定找到之前，如果low和high碰头了，也不找了
        while low < high and li[low] <= mid:
            low += 1
        # 跳出while循环后low所在的下标就是左侧比mid大的数所在位置
        # 我们把找到的数放在右侧空位上，high标记了这个空位
        li[high] = li[low]
        # 以上我们完成了一次 从右侧找到一个小数移到左侧，从左侧找到一个大数移动到右侧
    # 当这个while跳出来之后相当于low和high碰头了，我们把mid所在位置放在这个空位
    li[low] = mid
    # 这个时候mid左侧看的数都比mid小，mid右侧的数都比mid大

    # 然后我们对mid左侧所有数进行上述的排序
    quick_sort(li, start, low-1)
    # 我们mid右侧所有数进行上述排序
    quick_sort(li, low + 1, end)

    return li


def quicksort(data):     #快速排序
    stone = data[0]
    i = 1
    j = len(data)-1
    if len(data) > 1:     #分为len(data) >2和len(data) == 2两种情况，可合并
        while j > i:
            if data[j] <= stone:
                if data[i] > stone:
                    data[j], data[i] = data[i], data[j]
                else:
                    i += 1
            else:
                j -= 1
        if data[j] < stone:     #当len(data) == 2时只执行此部分
            data[0], data[j] = data[j], data[0]
        return quicksort(data[:j]) + quicksort(data[j:])
    else:     #回归条件，len(data) <= 1
        return data
#快速排序2
def quick_sortA(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left <= right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left

L = randList(5000)

#print(quick_sortA(L))


# ok我们实践一下
if __name__ == '__main__':
    li = randList(5000)
#    quick_sort(li, 0, len(li) - 1)
#    print(li)
    quick_sort(li,0,10)
    print()
#    print(quicksort(randList(10)))