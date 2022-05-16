# 개념 이해를 위해 코드를 참고했습니다..

from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  m1, m2 = map(int, input().split())
  graph[m1][m2] = graph[m2][m1] = 1

# 너비 우선 탐색
def bfs(start):
  discoverd = [start]
  queue = deque() 
  queue.append(start)

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for w in range(len(graph[start])):
      if graph[v][w] == 1 and (w not in discoverd):
        discoverd.append(w)
        queue.append(w)

# 깊이 우선 탐색
def dfs(start, discoverd=[]):
  discoverd.append(start)
  print(start, end=' ')

  for w in range(len(graph[start])):
    if graph[start][w] == 1 and (w not in discoverd):
      dfs(w, discoverd)

dfs(V)
print()
