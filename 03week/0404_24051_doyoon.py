#24051

def ins_sort(A, n, k):
    count = 0
    for i in range(1, n):
        loc = i-1
        newItem = A[i] # 원래 값 저장해두기

        while (A[loc] > newItem and 0 <= loc):
            A[loc+1] = A[loc] # 값 복사
            loc -= 1 # 맨 왼쪽까지 차례대로 검사
            count += 1 
            if (count == k):
                result = A[loc+1]
                return result
        
        if (loc+1 != i):
            A[loc+1] = newItem # 제자리에 원래 값 넣기
            count += 1
            if (count == k):
                result = A[loc+1]
                return result
            
    if (count < k):
        return -1
    else:
        return result

n, k= map(int, input().split())
A = list(map(int, input().split()))

print(ins_sort(A, n, k))