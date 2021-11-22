def twoNumberSum(array, targetSum):
	hash_ = {}
	for index, value in enumerate(array):
		diff = targetSum - value
		if diff in hash_:
			return [diff, value]
		else:
			hash_[value] = True
	return []