def quick_sort(array):
    quick_sort_sub(array, 0, len(array)-1)

def quick_sort_sub(array, start, end):
    if start < end:
        pos = partition(array, start, end)
        quick_sort_sub(array, start, pos-1)
        quick_sort_sub(array, pos+1, end)

def partition(array, start, end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    if i != end:
        array[i], array[end] = array[end], array[i]
    return i


n = int(input())
array = list()
for i in range(n):
    num = int(input())
    array.append(num)

quick_sort(array)
print(*array, sep='\n')


