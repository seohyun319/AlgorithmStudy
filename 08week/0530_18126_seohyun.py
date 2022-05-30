# silver2. 너구리 구구
# 거리까지 포함된 걸 어떻게 하지..?

import sys
from collections import deque 
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(n - 1):					
    a, b, c = map(int, input().split())		
    graph[a].append([b, c])
    graph[b].append([a, c])

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(1)
