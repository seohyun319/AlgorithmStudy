import sys

n = int(input())

graph = [[] for _ in range(n + 1)]

# 그래프 만들기
for _ in range(n - 1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

# 진짜 모르겠어여 ...
