# gold1. 입국 심사

import sys
put = sys.stdin.readline

n, m = map(int, put().split())
times = [int(put()) for _ in range(n)]

start = 0
end = max(times) * m
answer = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for time in times:
        total += mid // time
    if total >= m:
        end = mid - 1
        answer = mid # mid값은 계속 변하니까 새로운 변수에 저장해야
    else:
        start = mid + 1
print(answer)

# start값을 옮김: 30초에 7명 커버할 수 있는데 8명의 경우가 필요함 -> 범위 늘려줌. 
# end값을 옮김: mid값 안에 커버할 수 있음. 30초에 7명을 커버할 수 있는데 우리는 6명의 경우를 구함. 
# -> 최소 시간을 줄이는 거니까 남는 시간을 더 줄임. 