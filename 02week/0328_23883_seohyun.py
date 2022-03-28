import sys
put = sys.stdin.readline

n, k = map(int, put().split())  # 배열 A의 크기, 교환 횟수
array = list(map(int, put().split()))  # 서로 다른 배열 A의 원소
cnt: int = 0  # 교환 횟수


def selection_sort(array: list):
    global cnt
    for i in range(len(array), 0, -1):
        max_value = i
        for j in range(i+1, len(array)):
            if array[max_value] > array[j]:
                array[j], array[max_value] = array[max_value], array[j]
                cnt += 1
                print(array, cnt)


selection_sort(array)
print(array)
