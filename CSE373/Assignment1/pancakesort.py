def flip(array, n):
	start = 0
	while start < n:
		temp = array[start]
		array[start] = array[n]
		array[n] = temp
		start+=1
		n-=1

def pancakeSort(array, n):
	for size in reversed(range(n), 1):
		maxIndex = findIndexOfLargestElement(array)
		if(maxIndex != size-1):
			flip(array, maxIndex)
			flip(arr, size-1)
