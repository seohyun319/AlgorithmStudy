# 1260 DFS와 BFS
def dfs(graph, v, visited):
	visited[v] = True
	print(v, end=' ')
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

n, m, v = map(int,input().split()) #정점, 간선, 시작점
graph = [[] for _ in range(n + 1)]

for _ in range(m):
	v1, v2 = map(int, input().split())
	graph[v1].append(v2)
	graph[v2].append(v1)

#print(graph)
visited = [False]*9

dfs(graph, v, visited)
