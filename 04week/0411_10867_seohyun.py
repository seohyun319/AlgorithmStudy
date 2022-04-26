# silver5. 중복 빼고 정렬하기
# 원래 인풋 받을 때 말고 퀵 소트를 한 후 set을 했는데 틀렸다고 나와서 input 받을 때 set을 해줌
# 기존에 한 방법을 python은 틀렸다고 하는데 pypy로 돌리니까 맞게 나옴. 새로 고친 방법은 python으로 돌려도 맞게 나옴. 

# 기존 방법: pypy로 됨
# array: list = list(map(int, put().split()))
# ----------
# quick_sort(array, 0, n -1)
# set_array = set(array)
# print(*set_array)

# 고친 방법: python으로 해도 됨
# array: list = list(set(map(int, put().split())))
# ----------
# quick_sort(array, 0, len(array) - 1)
# print(*array)

import sys
put = sys.stdin.readline

n: int = int(put())
array: list = list(set(map(int, put().split())))
# pypy로 할 경우
# array: list = list(map(int, put().split()))

def quick_sort(array: list, start: int, end: int) -> None:
    if start >= end:
        return
    
    pivot:int = start
    left_idx:int = start + 1
    right_idx:int = end
    while left_idx <= right_idx:
        if left_idx <= end and array[left_idx] <= array[pivot]:
            left_idx += 1
        if right_idx > start and array[right_idx] >= array[pivot]:
            right_idx -= 1
        # 엇갈리면
        if left_idx > right_idx:
            array[pivot], array[right_idx], array[right_idx], array[pivot]
        else:
            array[left_idx], array[right_idx], array[right_idx], array[left_idx]
    
    quick_sort(array, start, right_idx - 1)
    quick_sort(array, right_idx + 1, end)

quick_sort(array, 0, len(array) - 1)
print(*array)

# pypy로 할 경우
# quick_sort(array, 0, n -1)
# set_array = set(array)
# print(*set_array)