# 백준 1654 - 랜선 자르기
k, n = map(int, input().split())
lens = []
for _ in range(k):
	lens.append(int(input()))
lens.sort()

# 가장 짧은 랜선보다 같거나 작아야 n개의 동일한 길이 랜선 제작 가능
keys = list(range(1, lens[0]+1))
result = []
start = 0
end = len(keys)-1
while start <= end:
	sum = 0
	mid = (start+end)//2
	for i in lens:
		sum += i // keys[mid]
	if sum >= n:
		result.append(keys[mid])
		start = mid + 1
	else:
		end = mid - 1
	# else:
	# 	start = mid+1
# print(result)
print(max(result))


# 틀렸다고 나오는데 왜 틀린 건지 모르겠음..
