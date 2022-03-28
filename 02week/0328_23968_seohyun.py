import sys
put = sys.stdin.readline

n, k = map(int, put().split())  # 배열 A의 크기, 교환 횟수
array = list(map(int, put().split()))  # 서로 다른 배열 A의 원소
cnt: int = 0  # 교환 횟수


def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


bubble_sort(array)
print(array)
