# 4963 섬의 개수
result= []
while True:
	w, h = map(int,input().split())
	if w == 0 and h == 0:
		break
	graph = []
	for i in range(h):
		graph.append(list(map(int,input().split())))
	result.append(graph)

print(result)

def dfs(x, y, result):
	if x <= -1 or x >= len(result) or y <= -1 or y >= len(result[0]):
		return False
	#print("dfs 안 result",result)
	if result[x][y] == 1:
		result[x][y] = 0
		dfs(x - 1, y, result)
		dfs(x, y - 1, result)
		dfs(x + 1, y, result)
		dfs(x, y + 1, result)
		return True
	return False

for i in range(len(result)):
	answer = 0
	#print(result[i])
	for j in range(len(result[i])):
		#print(result[i][j])
		for k in range(len(result[i][j])):
			#print(result[i][j][k])
			if dfs(j, k, result[i]) == True:
				answer += 1
	print(answer)
  
  
# 답 정확히 안   
