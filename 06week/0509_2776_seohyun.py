# silver4. 암기왕

# for i in num2 이 문장에서 for in이 O(N)이라서 시간초과난 듯

import sys
put = sys.stdin.readline

T: int = int(put())
for _ in range(T):
    n: int = int(put())
    num1: list = list(map(int, put().split()))
    m: int = int(put())
    num2: list = list(map(int, put().split()))
    for i in num2:
        if i in num1: print(1)
        else: print(0)