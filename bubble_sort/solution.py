def bubbleSort(array):
	counter = 0
	is_sorted =True
	while is_sorted:
		is_sorted=False
		for i in range(len(array)-1-counter):
			if array[i] > array[i+1]:
				swap(i, i+1, array)
				is_sorted=True
		counter+=1
	return array

def swap(i, j,  array):
	array[i], array[j] = array[j], array[i]