def quick_sort(a, start, end, k):
	global count

	if start<end:
		pos = partition(a, start, end, k)
		quick_sort(a, start, pos-1, k)
		quick_sort(a, pos+1, end, k)

def partition(a, start, end, k):
	global count
	global result1, result2

	pivot = a[end]
	#i = end-1
	i = start
	for j in range(start, end):
		if a[j]<= pivot:
			a[i], a[j] = a[j], a[i]
			i+=1
			count+=1
			print("count", count)
			print(array,a[i], a[j])
			if count==k:
				result1, result2 = a[i], a[j]
		# if i+1 != end: #i값이 바뀌었으면
		# 	a[i], a[end] = a[end], a[i]
	a[i], a[end] = a[end], a[i]
	count+=1
	print("count", count)
	print(array, a[i], a[j])
	if count == k:
		result1, result2 = a[i], a[j]
	return i #왜 i가 아니라 i+1?

count = 0
result1, result2 = 0, 0
n, k = map(int,input().split())
array = list(map(int, input().split()))

quick_sort(array, 0, n-1, k)

print("최종", array)
print(result1, result2)
