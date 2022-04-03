def insertion_sort(array, k):
    count = 0
    n = len(array)
    """
    3 1 2 5 4
    3 3 2 5 4 / 3
    1 3 2 5 4 / 1
    """
    for i in range(1, n):
        loc = i-1
        newItem = array[i]

        while (loc>=0) and (array[loc]>newItem):
            array[loc+1] = array[loc]
            loc -= 1
            count += 1
            
            if count == k:
                return array[loc+1]

        if loc != i-1:
            array[loc+1] = newItem
            count += 1

            if count == k:
                return array[loc+1]

    return -1


n, k = input().split()
n = int(n)
k = int(k)

array = list(map(int, input().split()))

print(insertion_sort(array, k))

