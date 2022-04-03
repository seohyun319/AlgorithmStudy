# bronze1. 수 정렬하기

import sys
put = sys.stdin.readline

n: int = int(put())
array: list = [int(put()) for _ in range(n)]


def insert_sort(array: list) -> None:
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


insert_sort(array)
for i in range(n):
    print(array[i])
