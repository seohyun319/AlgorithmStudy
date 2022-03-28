# 23881

def select(a, n, k):
    count = 0
    for i in range(n, -1):
        max_idx = i

        for j in range(i-1, 0, -1):
            if a[j] > a[max_idx]:
                max_idx = j

                if count == k:
                    print(j, max_idx)
        
        a[i], a[max_idx] = a[max_idx], a[i]
        count += 1



# 원래의 선택정렬은 인덱스 0부터 가야 하는데 이 문제는 마지막 인덱스부터 순서대로 정렬하는 방식

n, k = input().split()
n = int(n)
k = int(k)
a = list(map(int, input().split()))

select(a, n, k)
print(a)

