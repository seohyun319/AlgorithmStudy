"""
def test(list, num):
    max_result = 0
    for i in range(1, min(list)+1):
        sum = 0
        for elm in list:
            sum = sum + (elm // i)
        if sum == num:
            max_result = i
    return max_result
"""

def search(list, num):
    start = 1
    end = min(list)
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for elm in list:
            sum = sum + (elm // mid)
        if sum == num:
            return mid
        elif sum > num:
            start = mid + 1
        elif sum < num:
            end = mid - 1
    return -1


k, n = map(int, input().split())
len_list = []

if k <= n:
    for i in range(k):
        length = int(input())
        len_list.append(length)
print(search(len_list, n))
