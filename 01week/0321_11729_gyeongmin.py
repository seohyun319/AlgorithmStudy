# -*- coding: utf8 -*-
# 하노이 탑
# 2개: 1-2, 1-3, 2-3
# 원반 3개: 1-3, 1-2, 3-2, 1-3, 2-1, 2-3, 1-3
def hanoi(n, start, end, via):
    if n==1:
        print(start, end)
        return n
    hanoi(n-1,start, end, via)
    print(start, end)
    hanoi(n-1,end, via, start)
        
    
