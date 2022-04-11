def remove_overlap(array):
    tmp_set = set(array)
    new_list = list(tmp_set)
    return new_list

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
array = list(map(int, input().split()))
new_array = remove_overlap(array)
quick_sort(new_array)
print(*new_array, sep=' ')

