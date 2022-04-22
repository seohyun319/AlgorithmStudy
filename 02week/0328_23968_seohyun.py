# bronze 1. 알고리즘 수업 - 버블 정렬 1
# pypy로 맞음
import sys

put = sys.stdin.readline

n, k = map(int, put().split())  # 배열 A의 크기, 교환 횟수
array = list(map(int, put().split()))  # 서로 다른 배열 A의 원소
cnt: int = 0  # 교환 횟수


def bubble_sort(a):
    global cnt
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                cnt += 1
                if cnt == k:
                    print(a[j], a[j + 1])


bubble_sort(array)
if cnt < k:
    print(-1)
