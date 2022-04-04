# 2750
n = int(input())
array = list()
for i in range(n):
    array.append(int(input()))

def insert_sort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j], array[j - 1] = array[j-1], array[j]
            else:
                break
insert_sort(array)
print(array)
