# 2751 

def merge_sort(array):
    n = len(array)
    if n <= 1:
        return
    mid = n // 2
    s1 = a[:mid]
    s2 = a[mid:]
    merge_sort(s1)
    merge_sort(s2)
    i1 = 0
    i2 = 0
    i3 = 0

    while i1 < len(s1) and i2 < len(s2):
        if s2[i1] < s2[i2]:
            array[i3] = s1[i1]
            i1 += 1
            i3 += 1
        else:
            array[i3] = s2[i2]
            i2 += 1
            i3 += 1
        
    while i1 < len(s1):
        array[i3] = s1[i1]
        i1 += 1
        i3 += 1
    
    while i2 < len(s2):
        array[i3] = s2[i2]
        i2 += 1
        i3 += 1

n = int(input())
A = list()
for i in range(n):
    int(input())

merge_sort(A)
print(A, sep='\n')