import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = list(int(input()) for _ in range(n))

start = 0
end = min(t)*m
result = 0

while start <= end:
    mid = (start+end)//2
    
    
# 일단 여기까지 해봤는데.. while 다음에 어떻게 접근해야 할지 감이 안 옵니다.
# start랑 end를 어떤 기준으로 변경해야 할지 모르겠습니다.
# end는 제일 빨리 처리되는 곳으로만 간다는 전제 하에 저렇게 설정해보았는데 다른 풀이도 궁금합니다.

