# silver1 - 2447. 별 찍기 - 10

import sys
put = sys.stdin.readline

# 재귀로 별 찍기

n:int = int(put())
array:list = []
def star(n: int) -> str:
    if n == 3:
        array.append('***')
        array.append('* *')
        array.append('***')
        return array
    return star(n/3) + star(n/3)
print("\n".join(star(n)))
