# silver2. DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split()) # 정점 개수, 간선 개수, 탐색 시작할 점점 번호
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):					
    x, y = map(int, input().split())		
    graph[x].append(y)
    graph[y].append(x)

# 문제 조건: 방문할 수 있는 정점이 여러 개면 작은 노드부터 방문해야 해서 정렬 해줘야함
# 이거 안 정해줘서 틀렸음
for i in range(len(graph)):
    graph[i].sort()

def dfs(start):
    # 현재 노드 방문
    visited[start] = True
    print(start, end=' ')
    # 현재 노드와 연결된 다른 노드를 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    q = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 반복
    while q:
        v = q.popleft()
        print(v, end=' ')
        # 현재 노드와 연결된 다른 노드를 방문
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(v)
visited = [False] * (n+1) # 다시 초기화
print()
bfs(v)