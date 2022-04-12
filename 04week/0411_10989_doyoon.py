# 10989

n = int(input())
array = list()
for i in range(n):
    a = int(input())
    array.append(a)

def partition(a, start, end):
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    return i

def quick_sort_sub(a, start, end):
    if start < end:
        num = partition(a, start, end)
        quick_sort_sub(a, start, num-1)
        quick_sort_sub(a, num + 1, end)
    
def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)

quick_sort(array)

for i in array:
    print(i)
    
* 맞는 풀이 (사실상 정렬은 아닌 걸로)
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
