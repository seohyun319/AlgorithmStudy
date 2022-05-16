import sys
put = sys.stdin.readline

def can_win():
    jump_map = []
    n = int(input())
    for i in range(n):
        jump_map.append(list(map(int, put().split())))
             
can_win()