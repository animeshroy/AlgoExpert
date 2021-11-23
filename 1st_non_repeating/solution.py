def firstNonRepeatingCharacter(string):
    repeat_values = []
	non_repeat_values = []
	list_string = list(string)
	for index, value in enumerate(list_string):
		if value in list_string[index+1:]:
			repeat_values.append(value)
		if value not in repeat_values and value not in list_string[index+1:]:
			non_repeat_values.append([value,index])
	if len(non_repeat_values):
		return non_repeat_values[0][1]
	return -1