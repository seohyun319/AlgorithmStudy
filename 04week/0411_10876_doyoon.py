n = int(input())
array = list(map(int, input().split()))

def quick(array, start, end):
    if start >= end: # 원소가 1개일 경우 종료하는 조건
        return 
    pivot = start # pivot, start = 0
    left = start + 1 # left = 1
    right = end # right = len(array)
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: 
            array[right], array[pivot] = array[pivot], array[right]
        else: 
            array[left], array[right] = array[right], array[left]

    quick(array, start, right - 1)
    quick(array, right + 1, end)
    
quick(array, 0, len(array)-1)
array = set(array) # 중복 제거

for i in array:
    print(i, end=" ")

# 코드는 잘 돌아가는데 백준에서는 틀렸다고 뜸. 왜 그럴까?