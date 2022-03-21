# silver1 - 2447. 별 찍기 - 10

import sys
put = sys.stdin.readline

# 재귀로 별 찍기

n: int = int(put())

# 가운데 뚫림. 
# 3^1일 땐 1 인덱스, 3으로 나눈 나머지 1
# 3^2일 땐 3 4 5 인덱스, 3으로 나눈 몫 1

def star(n: int, array: list) -> list:
    lists: list = []
    if n == 3:
        return array
    else: 
        for i in array:            
            lists.append(i*3)
            lists.append(i+" "+i)
            lists.append(i*3)
        return star(n//3, lists)

star_list = ["***", "* *", "***"]
print("\n".join(star(n, star_list)))
