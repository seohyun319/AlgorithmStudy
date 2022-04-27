# silver5. 알고리즘 수업 - 퀵 정렬 1
# 리스트에 append해주는 방식은 메모리 초과 -> count해주는 방식으로.

import sys
put = sys.stdin.readline
sys.setrecursionlimit(10**4)

n, k = map(int, put().split())  # 배열의 크기, 저장 횟수
array = list(map(int, put().split()))
cnt: int = 0

def partition(array: list, start:int, end:int) -> int:
    global cnt    
    pivot: int = array[end]
    i: int = start
    for j in range(start, end):
        # 피봇보다 작으면
        if array[j] <= pivot:
            cnt += 1
            if cnt == k:
                # 작은 수부터 출력해주기 위해 정렬
                print(*sorted((array[i], array[j])))
            array[i], array[j] = array[j], array[i]
            i += 1
    if i != end:
        cnt += 1
        if cnt == k:
            # 작은 수부터 출력해주기 위해 정렬
            print(*sorted((array[i], array[end])))
        array[i], array[end] = array[end], array[i]
    return i

def quick_sort(array: list, start:int, end:int) -> None:    
    if start < end:
        position = partition(array, start, end)
        quick_sort(array, start, position - 1)
        quick_sort(array, position + 1, end)

quick_sort(array, 0, len(array) - 1)

if cnt < k:
    print(-1)