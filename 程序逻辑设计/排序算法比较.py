# 数据量为100时，插入排序的比较次数： 99
# 数据量为100时，冒泡排序的比较次数： 4950
# 数据量为100时，快速排序的比较次数： 99
# 数据量为100时，堆排序的比较次数： 622
# 数据量为1000时，插入排序的比较次数： 999
# 数据量为1000时，冒泡排序的比较次数： 499500
# 数据量为1000时，快速排序的比较次数： 1098
# 数据量为1000时，堆排序的比较次数： 10162
# 数据量为10000时，插入排序的比较次数： 9999
# 数据量为10000时，冒泡排序的比较次数： 49995000
# 数据量为10000时，快速排序的比较次数： 11097
# 数据量为10000时，堆排序的比较次数： 138386
# 数据量为100000时，插入排序的比较次数： 99999
# 数据量为100000时，冒泡排序的比较次数： 4999950000
# 数据量为100000时，快速排序的比较次数： 111096
# 数据量为100000时，堆排序的比较次数： 1751051


import random
data1 = [random.randint(0,100) for _ in range(100)]
data2 = [random.randint(0,100) for _ in range(1000)]
data3 = [random.randint(0,100) for _ in range(10000)]
data4 = [random.randint(0,100) for _ in range(100000)]


# 插入排序
def insert_sort(data):
    data = data[:]
    compare_count = 0
    for k in range(1, len(data)):
        cur = data[k]
        j = k
        while j > 0 and data[j - 1] > cur:
            data[j] = data[j - 1]
            j -= 1
        compare_count += 1
        data[j] = cur
    return compare_count


# 冒泡排序
def bubble_sort(data):
    data = data[:]
    compare_count = 0
    length = len(data)
    for i in range(length):
        for j in range(1, length - i):
            compare_count += 1
            if data[j - 1] > data[j]:
                data[j], data[j - 1] = data[j - 1], data[j]
    return compare_count


# 快速排序
quick_compare_count = 0


def quick_sort(arr):
        global quick_compare_count
        if len(arr) < 2:
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            quick_compare_count += len(less)
            greater = [i for i in arr[1:] if i > pivot]
            quick_compare_count += len(greater)
            return quick_compare_count


def use_quick_sort(data):
    data = data[:]
    result = quick_sort(data)
    return result


heap_compare_count = 0


# 堆排序
def heap_sort(data):
    data = data[:]
    global heap_compare_count
    length = len(data)
    def sift_down(start, end):
        global heap_compare_count
        root = start
        while True:
            child = 2 * root + 1
            heap_compare_count += 1
            if child > end:
                break
            if child + 1 <= end and data[child] < data[child + 1]:
                child += 1
            if data[root] < data[child]:
                data[root], data[child] = data[child], data[root]
                root = child
            else:
                break
    for start in range((length - 2) // 2, -1, -1):
        sift_down(start, length - 1)
    for end in range(length - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        sift_down(0, end - 1)
    return heap_compare_count


for data in [data1,data2,data3,data4]:
    print(f'数据量为{len(data)}时，插入排序的比较次数：',insert_sort(data))
    print(f'数据量为{len(data)}时，冒泡排序的比较次数：', bubble_sort(data))
    print(f'数据量为{len(data)}时，快速排序的比较次数：', quick_sort(data))
    print(f'数据量为{len(data)}时，堆排序的比较次数：', heap_sort(data))