# 23883

count = 0
result = '-1'

def select(a, n, k):
    for i in range(n, -1):
        max_idx = i

        for j in range(i-1, 0, -1):
            if a[j] > a[max_idx]:
                max_idx = j
                count += 1
        a[i], a[max_idx] = a[max_idx], a[i]
        if count == k:
            result = f"{a[j]} {a[max_idx]}"


# 원래의 선택정렬은 인덱스 0부터 가야 하는데 이 문제는 마지막 인덱스부터 순서대로 정렬하는 방식

n, k = input().split()
n = int(n)
k = int(k)
a = list(map(int, input().split()))

select(a, n, k)
print(result)

'''
23883이랑 뭐가 달라진지 모르겠다...?
애초에 23881이 자꾸 틀렸다고 나와서 어디서부터 손 대야 할지 감이 잡히지 않음
'''