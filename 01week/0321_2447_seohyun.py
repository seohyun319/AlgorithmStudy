# silver1 - 2447. 별 찍기 - 10

import sys
put = sys.stdin.readline

# 재귀로 별 찍기

def star(n: int) -> str:
    array:list = []
    if n == 3:
        return ['***', '* *', '***']
    
    # 이전 단계의 별
    star_list = star(n//3)

    for i in star_list:
        array.append(i*3)
    for i in star_list: # 공백은 i 크기만큼. 
        array.append(i + ' '*len(i) + i)
    for i in star_list:
        array.append(i*3)
    return array

n:int = int(put())
print("\n".join(star(n)))
