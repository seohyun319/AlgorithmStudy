n = int(input())
nums = []
for _ in range(n-1):
	nums.append((input().split()))

graph = [[0]*(n+1) for _ in range(n + 1)]

for i in range(n-1):
	x = int(nums[i][0])
	y = int(nums[i][1])
	graph[x][y] = nums[i][2]


print(graph)
