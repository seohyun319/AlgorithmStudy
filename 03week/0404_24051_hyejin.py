def insertion_sort(array, k):
    count = 0
    for i in range(1, n):
        j = i-1
        newItem = array[i]

        while (j>=0) and (array[j]>newItem):
            array[j+1] = array[j]
            j -= 1
            count += 1
            if count == k:
                return array[j+1]
        
        if j != i-1:
            array[j+1] = newItem
            count += 1
            if count == k:
                return newItem

    return -1


n, k = input().split()
n = int(n)
k = int(k)

array = list(map(int, input().split()))

print(insertion_sort(array, k))