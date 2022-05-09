def binary_search(list, x):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if x == list[mid]:
            return 1
        elif x > list[mid]:
            start = mid + 1
        elif x < list[mid]:
            end = mid - 1
    return 0

testcase = int(input())
for i in range(testcase):
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()
    m = int(input())
    m_list = list(map(int, input().split()))
    for x in m_list:
        print(binary_search(n_list, x))
        


    
