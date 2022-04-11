#10867
def quick_sort(array, start, end):
	if start >= end:
		return

	pivot = start
	left = start + 1
	right = end

	while left <= right:
		while left <= end and array[left] <= array[pivot]:
			left += 1

		while right > start and array[right] >= array[pivot]:
			right -= 1

		if left > right:
			array[right], array[pivot] = array[pivot], array[right]

		else:
			array[left], array[right] = array[right], array[left]

	quick_sort(array, start, right - 1)
	quick_sort(array, right + 1, end)

n = int(input())
array = list(map(int, input().split()))

quick_sort(array, 0, n-1)
array = set(array)
print(*array)
