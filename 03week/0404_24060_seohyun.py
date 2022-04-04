# silver5. 알고리즘 수업 - 병합 정렬 1
# 시간 초과

import sys
put = sys.stdin.readline

n, k = map(int, put().split())  # 배열의 크기, 저장 횟수
array = list(map(int, put().split()))
save_num: list = []  # 저장되는 수


def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    # print("LR", left_array, right_array, end=' ')

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
        # print("res", result, left_array, right_array, save_num)

    # result = result + left_array + right_array

    while left_array:  # 왼쪽 배열이 남은 경우
        pop_num = left_array.pop(0)
        result.append(pop_num)
        save_num.append(pop_num)
    # print("left", result, end=' ')
    while right_array:  # 오른쪽 배열이 남은 경우
        pop_num = right_array.pop(0)
        result.append(pop_num)
        save_num.append(pop_num)
    # print("right", result)

    return result


# print(merge_sort(array))

merge_sort(array)
# print(save_num)


if len(save_num) >= k:
    # 인덱스 0부터 시작하니까 k번째 값 프린트하기 위해 1 빼줌
    print(save_num[k-1])
else:
    print(-1)
