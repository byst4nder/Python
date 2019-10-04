# 生成随机序列
# 二叉堆是完全二元树或者是近似完全二元树，它分为两种：最大堆和最小堆。
# 最大堆：父结点的键值总是大于或等于任何一个子节点的键值；最小堆：父结点的键值总是小于或等于任何一个子节点的键值。
# 假设"第一个元素"在数组中的索引为 0 的话，则父节点和子节点的位置关系如下：
# (01) 索引为i的左孩子的索引是 (2*i+1);
# (02) 索引为i的左孩子的索引是 (2*i+2);
# (03) 索引为i的父结点的索引是 floor((i-1)/2);
import random

def randList(num): return [random.randint(1, 100000) for x in range(0, num)]





lst = randList(10)
print(lst)
print(HeapSort(lst))


def HeapSort(lst: list):
    n = len(lst)
    for x in range(n, 1, -1):
        lstlen = x
        a = lstlen//2-1

        for depth in range(a, -1, -1):
            # 在左、右孩子中找最大的数与节点交换
            if 2*depth+2 >= lstlen:
                if lst[depth] < lst[2*depth+1]:
                    lst[depth], lst[2*depth+1] = lst[2*depth+1], lst[depth]
            else:
                if lst[depth] < lst[2*depth+1]:
                    if lst[2*depth+1] < lst[2*depth+2]:
                        lst[depth], lst[2*depth+2] = lst[2*depth+2], lst[depth]
                    else:
                        lst[depth], lst[2*depth+1] = lst[2*depth+1], lst[depth]
                else:
                    if lst[depth] < lst[2*depth+2]:
                        lst[depth], lst[2*depth+2] = lst[2*depth+2], lst[depth]

        lst[0], lst[lstlen-1] = lst[lstlen-1], lst[0]

    return lst

