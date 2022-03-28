#23968
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(n-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            count +=1
    if count == k:
        print(nums[j+1], nums[j])

if count < k :
    print(-1)
