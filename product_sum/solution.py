# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, level=1):
	sum = 0
	for i in array:
		if isinstance(i,(list,)):
			sum += productSum(i, level+1)
		else:
			sum += i
	return sum * level