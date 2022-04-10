# silver5. 중복 빼고 정렬하기
# 맞았는데 set을 프린트 때 해주는 방법이 왜 틀린지 모르겠음

import sys
put = sys.stdin.readline

n: int = int(put())
array: list = list(set(map(int, put().split())))

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
