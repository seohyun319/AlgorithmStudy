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
리턴으로 처리할 시 리턴값이 2개의 값을 가진 튜플이 되거나, -1이 되는 2가지 경우가 있음
print(selection_sort(array, k)일 시, 튜플의 경우는 괄호까지 출력되므로 문제 조건에 맞지 않음
따라서 별도의 return값 없이 함수 내에서 print 사용
"""
