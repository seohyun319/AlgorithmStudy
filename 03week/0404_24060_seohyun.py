# silver5. 알고리즘 수업 - 병합 정렬 1
# 문제 예시랑 정렬 과정 다른 거 해결
# 문제 예시 순서는 2 / 3이 아니라 3 / 2로 나눔 => 올림

import sys, math
put = sys.stdin.readline

n, k = map(int, put().split())  # 배열의 크기, 저장 횟수
array = list(map(int, put().split()))
save_num: list = []  # 저장되는 수


def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    mid = math.ceil(len(array) / 2) # 올림: 문제에서 요구하는 순서에 따름
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    result: list = []
    while left_array and right_array:
        if left_array[0] < right_array[0]:
            pop_num = left_array.pop(0)
            result.append(pop_num)
            save_num.append(pop_num)
        else:
            pop_num = right_array.pop(0)
            result.append(pop_num)
            save_num.append(pop_num)

    while left_array:  # 왼쪽 배열이 남은 경우
        pop_num = left_array.pop(0)
        result.append(pop_num)
        save_num.append(pop_num)
    while right_array:  # 오른쪽 배열이 남은 경우
        pop_num = right_array.pop(0)
        result.append(pop_num)
        save_num.append(pop_num)

    return result


merge_sort(array)

if len(save_num) >= k:
    # 인덱스 0부터 시작하니까 k번째 값 프린트하기 위해 1 빼줌
    print(save_num[k-1])
else:
    print(-1)
