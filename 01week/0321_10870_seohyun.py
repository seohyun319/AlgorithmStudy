# bronze3 - 10870. 피보나치 수 5

import sys
put = sys.stdin.readline

# 재귀로 피보나치

n:int = int(put())

def fibo(n:int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(n))