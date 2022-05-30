import sys
put = sys.stdin.readline

n = int(input())

length = [[0 for col in range(n)] for row in range(n)]
print(length)

for i in range(n-1):
    info = list(map(int, put().split()))
    length[info[0]-1][info[1]-1] = info[2]
    length[info[1]-1][info[0]-1] = info[2]

print(length)