# 백준 16173 점프왕 쩰리

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,y):
	if x <= -1 or x >= n or y <= -1 or y >= n:
		return "Hing"
	num = graph[x][y]
	if num >= 0 and num <= 100:
		dfs(x+num, y)
		dfs(x, y+num)
		print((x,y),num)
		return "HaruHaru"

print(dfs(0,0))
if dfs(0,0) == -1:
	print("HaruHaru")
else:
	print("Hing")
  
# 못 풀겠습니다..
