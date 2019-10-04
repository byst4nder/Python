
import random

def randList(num): return [random.randint(1, 10) for x in range(0, num)]

def bucketSort(arr: list):
    maximum, minimum = max(arr), min(arr)
    bucketArr = [[] for i in range(maximum // 10 - minimum // 10 + 1)]  # set the map rule and apply for space
    for i in arr:  # map every element in array to the corresponding bucket
        index = i // 10 - minimum // 10
        bucketArr[index].append(i)
    arr.clear()
    for i in bucketArr:
        heapSort(i)   # sort the elements in every bucket
        arr.extend(i)  # move the sorted elements in bucket to array


print(bucketSort(randList(10)))