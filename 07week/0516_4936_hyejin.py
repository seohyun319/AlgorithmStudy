import sys
put = sys.stdin.readline

def island_num():
    island_map = []
    count = 0
    while True:
        w, h = map(int, put().split())
        
        if w == 0 and h == 0:
            break
        
        one_map = []
        for i in range(h):
            one_map.append(list(map(int, put().split())))

        island_map.append(one_map)
        
island_num()
