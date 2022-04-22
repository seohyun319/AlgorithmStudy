# bronze1. 알고리즘 수업 - 삽입 정렬 1
# pypy

import sys
put = sys.stdin.readline

n, k = map(int, put().split())  # 배열의 크기, 저장 횟수
array = list(map(int, put().split()))
save_num: list = []  # 저장되는 수


def insert_sort(array: list):
    for i in range(1, n):
        key = array[i]
        j = i-1

        while j >= 0 and array[j] > key:
            save_num.append(array[j])
            array[j+1] = array[j]
            j -= 1

        # 이미 맞는 자리에 있으면 안 함.
        if j+1 != i:  # 맞지 않은 자리에 있으면~
            save_num.append(key)
            array[j+1] = key


insert_sort(array)

if len(save_num) >= k:
    # 인덱스 0부터 시작하니까 k번째 값 프린트하기 위해 1 빼줌
    print(save_num[k-1])
else:
    print(-1)
