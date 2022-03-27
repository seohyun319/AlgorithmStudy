def selection_sort(n, k):
    count = 0
    l = len(n)
    for i in range(l):
        max_index = 0
        last = l-i-1
        for j in range(l-i):
            if n[max_index] < n[j]:
                max_index = j
        if max_index != l-i-1:
            count += 1
            if count == k:
                small = n[last]
                big = n[max_index]
                print(small, big)
            n[max_index], n[last] = n[last], n[max_index]
    if count < k:
        print(-1)
    
n, k = input().split()
n = int(n)
k = int(k)

array = list(map(int, input().split()))
selection_sort(array, k)

"""
시간 초과
23881 문제와 다른 점은 N의 범위, 시간 제한 뿐인데 어떻게 해결해야 할지 모르겠음
"""