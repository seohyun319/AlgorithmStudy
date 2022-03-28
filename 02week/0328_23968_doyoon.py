n,k = map(int,input().split())
a = list(map(int,input().split()))

count = 0
result = '-1'

for i in range(n):
    for j in range(n-i-1):
        if a[j] > a[j + 1]:
            count += 1
            a[j], a[j + 1] = a[j + 1], a[j]
            if count == k:
                result = f"{a[j]} {a[j+1]}"

print(result)

# 시간 초과...