# -*- coding: utf8 -*-
# 별 찍기
from __future__ import print_function

def star(n):
    if n==3:
        for i in range(n):
            for j in range(n):
                if i==1 and j==1:
                    print(" ", end='')
                else:
                    print("*", end='')
            print("\n")
    if n>3:
        for i in range(n/3):
            for j in range(n/3):
                if i==n/3 and j==n/3:
                    print(" ", end='')
                else:
                    star(n/3)
            #print("\n")
        


star(9)