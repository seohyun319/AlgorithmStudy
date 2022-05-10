import sys

t = int(input())
for _ in range(t):
    n = int(input())
    s1 = list(sys.stdin.readline().split())
    m = int(input())
    s2 = list(sys.stdin.readline().split())
    for s in s2:
        if s in s1:
            print(1)
        else:
            print(0)
           
# 시간 초과?! 

