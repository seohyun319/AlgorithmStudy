# 23881
# n, k = list(map(int, input().split()))
# nums = list(map(int, input().split()))
# count = 0

# for i in range(0,n):
#     max_idx = i
#     for j in range(i+1,n):
#         if nums[max_idx] > nums[j]:
#             max_idx = j
#     nums[max_idx], nums[i] = nums[i], max_idx
#     count += 1
#     if count == k:
#         print(nums[i],nums[max_idx])

# if count < k:
#     print(-1)
    
    
    
def selection_sort(nums, n, k):
	count = 0
	for i in range(n-1, 0, -1):
		last_idx = i
		max_idx = i
		for j in range(0,i):
			if nums[max_idx] < nums[j]:
				max_idx = j
		if last_idx != max_idx:
			nums[last_idx], nums[max_idx] = nums[max_idx], nums[last_idx]
			count += 1
			if count == k:
				print(nums[max_idx], nums[last_idx])

	if count < k:
		print(-1)

n, k = map(int, input().split())
nums = list(map(int, input().split()))

selection_sort(nums,n,k)
