# bronze1 - 선택정렬 1
# 기존에 아는 선택정렬 코드에서 반복문 범위를 둘 다 뒤집어줌
import sys

put = sys.stdin.readline

n, k = map(int, put().split())  # 배열 A의 크기, 교환 횟수
array = list(map(int, put().split()))  # 서로 다른 배열 A의 원소
cnt: int = 0  # 교환 횟수


def selection_sort(array: list):
    global cnt
    for i in range(len(array) - 1, 0, -1):  # n-1(마지막 인덱스)부터 1까지
        max_idx = i
        # 범위 내에서 최대값을 가진 인덱스 찾기
        for j in range(0, i):
            if array[max_idx] < array[j]:
                max_idx = j
        # for 문이 끝났으면 min_idx 안에 최소값의 위치가 들어있다.
        if max_idx != i:
            array[i], array[max_idx] = array[max_idx], array[i]  # 스왑
            cnt += 1
            if cnt == k:
                print(array[max_idx], array[i])


selection_sort(array)
if cnt < k:
    print(-1)
