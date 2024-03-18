import random
import time
import sys
sys.setrecursionlimit(1000000)

def exchange_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



def quick_sort(array, l, r):
  if l >= r:
    return
  stack = []
  stack.append(l)
  stack.append(r)
  while stack:
    low = stack.pop(0)
    high = stack.pop(0)
    if high - low <= 0:
      continue
    x = array[high]
    i = low - 1
    for j in range(low, high):
      if array[j] <= x:
        i += 1
        array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    stack.extend([low, i, i + 2, high])


def test(n):
    a = [random.randint(1,1000) for i in range(n)]
    time_start=time.time()
    exchange_sort(a)
    time_end=time.time()
    print(f'n={n},A:',(time_end - time_start))
    time_start=time.time()
    quick_sort(a,0,len(a)-1)
    time_end=time.time()
    print(f'n={n},B:',(time_end - time_start))


test(80000)

