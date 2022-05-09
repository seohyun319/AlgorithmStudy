# silver3. 랜선 자르기

import sys
put = sys.stdin.readline

k, n = map(int, put().split())
length = [int(put()) for _ in range(k)]
start = 1 # 0으로 하면 zeroDivisionError
end = max(length) # 최대 길이 구하기 위함
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in length:
        sum += i // mid        
    if sum >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
# def binary_search(a, x):
#     start = 0
#     end = len(a) - 1
#     while start <= end: # 탐색할 범위가 남아 있는 동안 반복
#         mid = (start + end) // 2 # 탐색 범위의 중간 위치
#         if x == a[mid]: # 찾으면 발견 위치 반환
#             return mid
#         elif x > a[mid]: # 찾는 값이 더 크면 오른쪽으로 범위를 좁혀 계속 탐색
#             start = mid + 1
#         else: # 찾는 값이 더 작으면 왼쪽으로 범위를 좁혀 계속 탐색
#             end = mid - 1
#     return -1 # 찾지 못하면 -1 반환