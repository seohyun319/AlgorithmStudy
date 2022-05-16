# silver5. 점프왕 쩰리 (Small)

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0]
dy = [0, 1]
q = deque()

def bfs():
    while q:
        x, y, dist = q.popleft()
        for i in range(2):
            nx, ny = x + dist*dx[i], y + dist*dy[i]
            if 0 <= nx <= n and 0 <= ny <= n and dist != 0:
                q.append([nx, ny])
                array[nx][ny] = array[x][y] + 1

bfs()

