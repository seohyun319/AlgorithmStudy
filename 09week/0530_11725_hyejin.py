import sys
put = sys.stdin.readline

n = int(input())

connect = [[0 for col in range(n)] for row in range(n)]

for i in range(n-1):
    line = list(map(int, put().split()))
    connect[line[0]-1][line[1]-1] = 1
    connect[line[1]-1][line[0]-1] = 1

parent = []
for i in range(1, n):
    exist = []
    #행렬을 확인해서
    for j in range(n):
        if connect[i][j] == 1:
            exist.append(j+1)
    print(exist)
    #1이 있으면 parent는 1
    if 1 in exist:
        parent.append(1)
    else:
        #값이 하나면 parent는 해당 값
        if len(exist) == 1:
            parent.append(exist[0])
        #값이 두개일 때
        else:
            parent.append(exist)

for i in range(len(parent)):
    print(parent[i])
