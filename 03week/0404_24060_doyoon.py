# 24060

def merge_sort(A, n, k):
    count = 0

    if n <= 1:
        return A
    
    mid = n // 2
    s1 = merge_sort(A[:mid], len(A[:mid]), k)
    s2 = merge_sort(A[:mid], len(A[:mid]), k)

    result = []
    while s1 and s2:
        if s1[0] > s2[0]:
            result.append(s1.pop(0))
            count += 1
        else:
            result.append(s2.pop(0))
            count += 1

    result = result + s1 + s2
    return result

    if (count == k):
        answer = A[-1]
        return answer
        
    elif (count < k):
        return -1

n, k = map(int, input().split())
A = list(map(int, input().split()))

print(merge_sort(A, n, k))

# count를 어디에서 세야 하는지 모르겠음.