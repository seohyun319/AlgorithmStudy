#24060
# 시간 초과 해결한 코드

import math

def merge_sort(array, n, k):

    if n <= 1:
        return array

    global count
    global result
    
    mid = math.ceil(n / 2)

    a1 = merge_sort(array[:mid], len(array[:mid]), k)
    a2 = merge_sort(array[mid:], len(array[mid:]), k)

    new_array = []

    i1, i2 = 0, 0

    while len(a1) > i1 and len(a2) > i2 :
        if a1[i1] < a2[i2]:
            new_array.append(a1[i1])
            count+=1
            if count == k:
                result = a1[i1]
            i1+=1
        else:
            new_array.append(a2[i2])
            count += 1
            if count == k:
                result = a2[i2]
            i2+=1

    while len(a1) > i1 and len(a2) <= i2 :
        new_array.append(a1[i1])
        count += 1
        if count == k:
            result = a1[i1]
        i1+=1

    while len(a2) > i2 and len(a1) <= i1 :
        new_array.append(a2[i2])
        count += 1
        if count == k:
            result = a2[i2]
        i2 += 1

    if count < k:
        result = -1

    return new_array


import sys

input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

count = 0

merge_sort(array, n, k)
print(result)
