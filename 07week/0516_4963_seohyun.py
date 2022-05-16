# silver2. 섬의 개수

import sys
from collections import deque
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(h)]
    if w == 0 and h == 0:
        break
    print(array)
