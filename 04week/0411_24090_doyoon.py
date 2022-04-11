# 24090

n, k = map(int, input().split())
array = list(map(int, input().split()))
global count

def partition(a, start, end):
    global count
    count = 0
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    count += 1 
    if count == k: 
        print(array[i], array[end])
    a[i], a[end] = a[end], a[i]
    return i

def quick_sort_sub(a, start, end):
    if start < end:
        num = partition(a, start, end)
        quick_sort_sub(a, start, num-1)
        quick_sort_sub(a, num + 1, end)
    
def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)

quick_sort(array)

if count < k:
    print(-1)
