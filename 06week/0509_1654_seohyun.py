# silver3. 랜선 자르기

import sys
put = sys.stdin.readline

k, n = map(int, put().split())
length = [int(put()) for _ in range(k)]
start = 1 # 0으로 하면 zeroDivisionError
end = max(length) # 최대 길이 구하기 위함

while start <= end:
    mid = (start + end) // 2
    sum = 0 # 총 개수
    for i in length:
        sum += i // mid  # 나눈 몫을 더해줌
    print(sum)
    if sum >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)