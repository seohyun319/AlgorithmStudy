# silver2. 트리의 부모 찾기

import sys
from collections import deque 
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n + 1) # 부모 테이블 초기화하기 

for _ in range(n - 1):					
    x, y = map(int, input().split())		
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    q = deque([start])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if parent[i] == 0:
                q.append(i)
                parent[i] = v

bfs(1)
for i in range(2, n + 1):
    print(parent[i])