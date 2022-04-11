def quick_sort(array, k):
    quick_sort_sub(array, 0, len(array)-1, k)

def quick_sort_sub(array, start, end, k):
    if start < end:
        pos = partition(array, start, end)
        quick_sort_sub(array, start, pos-1, k)
        quick_sort_sub(array, pos+1, end, k)

def partition(array, start, end):
    global count
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            count += 1
            if count == k:
                print(array[j], array[i])
            array[j], array[i] = array[i], array[j]
            i += 1
    if i != end:
        count += 1
        if count == k:
            print(array[end], array[i])
        array[i], array[end] = array[end], array[i]
    return i

global count
count = 0

n, k = input().split()
n = int(n)
k = int(k)

array = list(map(int, input().split()))

quick_sort(array, k)
if count < k:
    print(-1)