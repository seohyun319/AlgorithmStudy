# silver2. 수 정렬하기 2
# 시간초과 해결: pop이 삭제를 하고나서 인덱스 다 밀어줘야해서 오래 걸림

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
    left_idx, right_idx = 0, 0
    while len(left_array) > left_idx and len(right_array) > right_idx:
        if left_array[left_idx] < right_array[right_idx]:
            result.append(left_array[left_idx])
            left_idx += 1
        else:
            result.append(right_array[right_idx])
            right_idx += 1

    while len(left_array) > left_idx and len(right_array) <= right_idx:  # 왼쪽 배열이 남은 경우
        result.append(left_array[left_idx])
        left_idx += 1

    while len(right_array) > right_idx and len(left_array) <= left_idx:  # 오른쪽 배열이 남은 경우
        result.append(right_array[right_idx])
        right_idx += 1

    return result


print(*merge_sort(array), sep='\n')
