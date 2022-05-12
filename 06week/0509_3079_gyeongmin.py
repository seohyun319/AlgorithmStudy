# 백준 3079
n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]

t.sort()
result = []
sum = 0

if n >= m: # 심사대의 수가 사람 수보다 많거나 같을 때
	print(t[m-1])
else: 
	
# 모르겠어요..... 뭔가 규칙이 있을 것 같긴 한데 접근을 어떻게 해야 할지 감이 안 옵니다
