# 1260 DFS와 BFS
from collections import deque

def dfs(graph, v, visited):
	visited[v] = True
	print(v, end=' ')
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

def bfs(graph, v, visited):
	queue = deque([v])
	visited[v] = True

	while queue:
		num = queue.popleft()
		print(num, end=' ')

		for i in graph[num]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True


n, m, v = map(int,input().split()) #정점, 간선, 시작점
graph = [[] for _ in range(n + 1)]

for _ in range(m):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)
#print(graph)


visited = [False for _ in range(n + 1)]

dfs(graph, v, visited)
print()
bfs(graph, v, visited)
