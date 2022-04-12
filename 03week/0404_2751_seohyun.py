# silver2. 수 정렬하기 2
# 시간 초과

import sys
put = sys.stdin.readline

n: int = int(put())
array: list = [int(put()) for _ in range(n)]


def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    result: list = []
    while left_array and right_array:
        if left_array[0] < right_array[0]:
            result.append(left_array.pop(0))
        else:
            result.append(right_array.pop(0))
    result = result + left_array + right_array

    return result


print(*merge_sort(array), sep='\n')
