def nonConstructibleChange(coins):
	change_sum = 0
	coins.sort()
	for coin in coins:
		if coin > change_sum+1:
			return change_sum+1
		else:
			change_sum+=coin
	return change_sum+1
