# 백준 2776 - 암기왕
t = int(input())

for i in range(t):
	n = int(input())
	nums1 = list(map(int, input().split()))
	m = int(input())
	nums2 = list(map(int, input().split()))

	nums1.sort()
	result = []

	for i in range(len(nums2)):
		key = nums2[i]
		start = 0
		end = len(nums1)-1
		while start <= end:
			mid = (start+end)//2
			if nums1[mid] == key:
				result.append(1)
				break
			else:
				if nums1[mid] > key:
					end = mid-1
				else:
					start = mid+1
		if len(result)<i+1:
			result.append(0)

	for i in range(len(result)):
		print(result[i])
