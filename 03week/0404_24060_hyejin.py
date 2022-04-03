import math

global count
count = 0

def merge_sort(array, k):
    global count
    n = len(array)
    if n <= 1:
        return array

    mid = math.ceil(n / 2)
    g1 = merge_sort(array[:mid], k)
    g2 = merge_sort(array[mid:], k)

    result = []

    while g1 and g2:
        if g1[0] < g2[0]:
            count += 1
            if count == k:
                print(g1[0])
            result.append(g1.pop(0))
        else:
            count += 1
            if count == k:
                print(g2[0])
            result.append(g2.pop(0))
    
    while g1:
        count += 1
        if count == k:
            print(g1[0])
        result.append(g1.pop(0))

    while g2:
        count += 1
        if count == k:
            print(g2[0])
        result.append(g2.pop(0))

    return result


n, k = input().split()
n = int(n)
k = int(k)

array = list(map(int, input().split()))

merge_sort(array, k)
if count < k:
    print -1