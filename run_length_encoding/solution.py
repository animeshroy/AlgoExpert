def runLengthEncoding(string):
	temp_char = string[0]
	char_count = 1
	new_string = ""
	for index in range(1,len(string)):
		if string[index] == temp_char:
			char_count+=1
		else:
			new_string += encode_char(char_count, temp_char)
			temp_char = string[index]
			char_count = 1
	
	new_string += encode_char(char_count, temp_char)
	return new_string
		
def encode_char(count, char):
	counts = []
	while count> 9:
		counts.append(9)
		count-=9
		if count > 9:
			continue
		else:
			counts.append(count)
	if not len(counts):
		counts.append(str(count))
	return ''.join([str(x)+char for x in counts])
