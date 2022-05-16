import sys
put = sys.stdin.readline

def dfs_bfs():
    n, m, v = map(int, put().split())
    
    line = []
    for i in range(m):
        line.append(list(map(int, put().split())))
    print(line)

dfs_bfs()
