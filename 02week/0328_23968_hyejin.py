def bubble_selection(n, k):
    count = 0
    l = len(n)
    for i in range(l-1):
        for j in range(l-1-i):
            if n[j] > n[j+1]:
                count += 1
                if count == k:
                    print(n[j+1], n[j])
                n[j], n[j+1] = n[j+1], n[j]
    if count < k:
        print(-1)

n, k = input().split()
n = int(n)
k = int(k)
array = list(map(int, input().split()))
bubble_selection(array, k)

#시간 초과