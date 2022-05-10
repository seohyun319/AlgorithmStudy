import sys
k, n = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in lan:
        total += i // mid
        
    if total >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)

