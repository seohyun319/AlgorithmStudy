#24060
def merge_sort(array, n, k):
    q = n//2
    a1 = array[:q]
    a2 = array[q:]
    merge_sort(a1)
    merge_sort(a2)

    result = list()
    while a1 and a2:
        if (a1[0] < a2[0]):
            result.append(a1.pop(0))
        else:
            result.append(a2.pop(0))


n, k = list(map(int, input().split()))
array = list(map(int, input().split()))

print(merge_sort(array,n,k))
