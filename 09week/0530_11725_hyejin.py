import sys
put = sys.stdin.readline

n = int(input())

connect = [[0 for col in range(n)] for row in range(n)]

for i in range(n-1):
    line = list(map(int, put().split()))
    connect[line[0]-1][line[1]-1] = 1
    connect[line[1]-1][line[0]-1] = 1

print(connect)

