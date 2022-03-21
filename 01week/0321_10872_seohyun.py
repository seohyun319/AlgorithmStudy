# bronze2 - 10872. 팩토리얼

import sys
put = sys.stdin.readline

# 재귀로 팩토리얼

n:int = int(put())

def factorial(n: int) -> int:
    if n == 0 or n == 1: return 1
    return n*factorial(n-1)

print(factorial(n))