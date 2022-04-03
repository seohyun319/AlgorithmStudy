def make_array():
    n = int(input())
    array = []
    for i in range(n):
        num = int(input())
        array.append(num)
    return array

def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        for j in range(i-1, -1, -1):
            if array[j] > key:
                array[j+1] = array[j]
                array[j] = key
    return array
            
print(insert_sort(make_array()))
