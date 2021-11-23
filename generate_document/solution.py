def generateDocument(characters, document):
	character_map = {}
	for i in characters:
		if i not in character_map:
			character_map[i] = 1
		else:
			character_map[i] += 1
	doc_map = {}
	for i in document:
		if i not in doc_map:
			doc_map[i] = 1
		else:
			doc_map[i] += 1
	for k in document:
		if k not in character_map:
			return False
		elif doc_map[k] > character_map[k]:
			return False
	return True
		
