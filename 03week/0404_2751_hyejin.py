def make_array():
    n = int(input())
    array = []
    for i in range(n):
        num = int(input())
        array.append(num)
    return array

def merge_sort(array):
    n = len(array)

    if n <= 1:
        return array

    mid = n // 2
    g1 = merge_sort(array[:mid])
    g2 = merge_sort(array[mid:])

    result = []

    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    result = result + g1 + g2

    return result

print(merge_sort(make_array()))
