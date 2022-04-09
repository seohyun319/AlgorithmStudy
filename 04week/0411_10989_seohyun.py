# silver5. 수 정렬하기 5
# 메모리 초과

import sys
put = sys.stdin.readline

n: int = int(put())
array: list = [int(put()) for _ in range(n)]

def partition(array: list, start: int, end: int):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i

def quick_sort(array: list, start: int, end: int):
    if start < end:
        position = partition(array, start, end)
        quick_sort(array, start, position - 1)
        quick_sort(array, position + 1, end)

quick_sort(array, 0, len(array) - 1)
print(*array, sep='\n')