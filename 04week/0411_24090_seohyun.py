# silver5. 알고리즘 수업 - 퀵 정렬 1
# 정답은 맞음
# sys.setrecursionlimit(10**6) 해주면 메모리 초과, 안 하면 런타임에러(Recursion Error)

import sys

put = sys.stdin.readline

n, k = map(int, put().split())  # 배열의 크기, 저장 횟수
array = list(map(int, put().split()))
save_num: list = []  # 저장되는 수


def partition(array: list, start: int, end: int) -> int:
    pivot: int = array[end]
    i: int = start
    for j in range(start, end):
        # 피봇보다 작으면
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            save_num.append((array[i], array[j]))
            i += 1
    if i != end:
        array[i], array[end] = array[end], array[i]
        save_num.append((array[i], array[end]))
    return i


def quick_sort(array: list, start: int, end: int) -> None:
    if start < end:
        position = partition(array, start, end)
        quick_sort(array, start, position - 1)
        quick_sort(array, position + 1, end)


quick_sort(array, 0, len(array) - 1)

if len(save_num) >= k:
    # 인덱스 0부터 시작하니까 k번째 값 프린트하기 위해 1 빼줌
    print(*save_num[k - 1])
else:
    print(-1)
