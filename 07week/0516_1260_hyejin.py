def dfs_bfs():
    n, m, v = map(int, input().split())
    for i in range(m):
        start, last = map(int, input().split())
        line.append((start, last))

line = []
dfs_bfs()
