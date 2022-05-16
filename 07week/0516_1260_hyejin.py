import sys
put = sys.stdin.readline

def dfs_bfs():
    n, m, v = map(int, put().split())
    for i in range(m):
        start, last = map(int, input().split())
        line.append((start, last))

line = []
dfs_bfs()
